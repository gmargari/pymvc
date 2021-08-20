from typing import Dict, List, Tuple

from model import Model


class BasicModel(Model):
    def __init__(self) -> None:
        super().__init__()
        self.objects: Dict[str, int] = {}

    def add_object(self, object: str) -> None:
        if object in self.objects:
            self.objects[object] += 1
        else:
            self.objects[object] = 1

    def remove_object(self, object: str) -> None:
        if object in self.objects and self.objects[object] > 0:
            self.objects[object] -= 1

    def get_objects(self) -> List[Tuple[str, int]]:
        return sorted(list((name, num) for name, num in self.objects.items() if num > 0))
