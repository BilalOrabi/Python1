from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self: DataProcessor, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True

        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                for k, v in d.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
            return True
        return False


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
