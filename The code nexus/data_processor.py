from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._counter = 0
        self._data_store: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data_store:
            raise IndexError("No data to output")
        return self._data_store.pop(0)


class NumericProcessor(DataProcessor):

    def _is_numeric(self, x: Any) -> bool:
        return isinstance(x, (int, float)) and not isinstance(x, bool)

    def validate(self, data: Any) -> bool:
        if self._is_numeric(data):
            return True
        if isinstance(data, list):
            return all(self._is_numeric(x) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data_store.append((self._counter, str(item)))
                self._counter += 1
        else:
            self._data_store.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):

    def _is_valid_text(self, x: Any) -> bool:
        return isinstance(x, str)

    def validate(self, data: Any) -> bool:
        if self._is_valid_text(data):
            return True

        if isinstance(data, list):
            return all(self._is_valid_text(x) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data_store.append((self._counter, item))
                self._counter += 1
        else:
            self._data_store.append((self._counter, data))
            self._counter += 1


class LogProcessor(DataProcessor):

    def _is_valid_dict(self, data: dict[str, str]) -> bool:
        return all(
            isinstance(k, str) and isinstance(v, str) for k, v in data.items())

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._is_valid_dict(data)

        if isinstance(data, list):
            return all(
                isinstance(d, dict) and self._is_valid_dict(d) for d in data)

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def _format_entry(d: dict[str, str]) -> str:
            return f"{d["log_level"]}: {d["log_message"]}"

        if isinstance(data, list):
            for item in data:
                self._data_store.append((self._counter, _format_entry(item)))
                self._counter += 1
        else:
            self._data_store.append((self._counter, _format_entry(data)))
            self._counter += 1


if __name__ == "__main__":
    print("=== Code Nexus- Data Processor ===")

    np = NumericProcessor()

    print("Testing Numeric Processor...")
    print(f"Trying to validate input ’42’: {np.validate(42)}")
    print(f"Trying to validate input ’Hello’: {np.validate('Hello')}")

    print("Test invalid ingestion of string ’foo’ without prior validation:")
    try:
        np.ingest("foo")
    except ValueError:
        print("Got exception: Improper numeric data")

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for i in range(3):
        rank, value = np.output()
        print(f"Numeric value {i}: {value}")

    print("\nTesting Text Processor...")

    tp = TextProcessor()

    print(f"Trying to validate input ’42’: {tp.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")

    tp.ingest(text_data)

    print("Extracting 1 value...")

    _, value = tp.output()

    print(f"Text value 0: {value}")

    print("\nTesting Log Processor...")

    lp = LogProcessor()

    print(f"Trying to validate input ’Hello’: {lp.validate('Hello')}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]

    print(f"Processing data: {log_data}")

    lp.ingest(log_data)

    print("Extracting 2 values...")

    for i in range(2):
        _, value = lp.output()
        print(f"Log entry {i}: {value}")
