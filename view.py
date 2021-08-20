from typing import List, Tuple, Union
from observable import Observable

class View(Observable):
    def __init__(self) -> None:
        super().__init__()

    def show_objects(self, objects: List[Tuple[str, int]]) -> None:
        raise NotImplemented

    def run(self) -> None:
        raise NotImplemented

    def quit(self) -> None:
        raise NotImplemented

