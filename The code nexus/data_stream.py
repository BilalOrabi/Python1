from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._counter = 0
        self._total_processed = 0
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

    def total_processed(self) -> int:
        return self._total_processed

    @property
    def remaining(self) -> int:
        return len(self._data_store)


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
                self._total_processed += 1
        else:
            self._data_store.append((self._counter, str(data)))
            self._counter += 1
            self._total_processed += 1


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
                self._total_processed += 1
        else:
            self._data_store.append((self._counter, data))
            self._counter += 1
            self._total_processed += 1


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
                self._total_processed += 1
        else:
            self._data_store.append((self._counter, _format_entry(data)))
            self._counter += 1
            self._total_processed += 1


class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:

        for element in stream:
            processed = False

            for proc in self._processors:

                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    f"DataStream error- Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:

        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:

            name = proc.__class__.__name__.replace("Processor", " Processor")

            print(
                f"{name}: total {proc.total_processed()} items processed, "
                f"remaining {proc.remaining} on processor"
            )


if __name__ == "__main__":

    print("=== Code Nexus- Data Stream ===")

    stream = DataStream()

    print("Initialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")

    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {batch}")

    stream.process_stream(batch)

    stream.print_processors_stats()

    print("\nRegistering other data processors")

    text = TextProcessor()
    logs = LogProcessor()

    stream.register_processor(text)
    stream.register_processor(logs)

    print("Send the same batch again")

    stream.process_stream(batch)

    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        logs.output()

    stream.print_processors_stats()
