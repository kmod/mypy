from typing import Tuple

class EnumTypeWrapper(object):
    def Name(self, number: int) -> str: ...
    def Value(self, name: str) -> int: ...
    def keys(self) -> List[str]: ...
    def values(self) -> List[int]: ...
    def items(self) -> List[Tuple[str, int]]: ...
    @staticmethod
    def items() -> List[Tuple[str, int]]: ...