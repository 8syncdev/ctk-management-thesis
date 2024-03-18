from typing import Generic, TypeVar 
from abc import ABC, abstractmethod
from app.ui.base.base_ui import BaseUI

_T = TypeVar('_T', bound=BaseUI)

class InterfaceDAO(ABC):
    def get(self, id: int) -> Generic[_T]:
        pass

    def get_all(self) -> list[Generic[_T]]:
        pass

    def create(self, obj: Generic[_T]) -> Generic[_T]:
        pass

    def update(self, obj: Generic[_T]) -> Generic[_T]:
        pass

    def delete(self, obj: Generic[_T]) -> bool:
        pass

    def delete_all(self) -> bool:
        pass

    def count(self) -> int:
        pass



