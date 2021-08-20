from typing import List, Tuple


class Model(object):
    def __init__(self) -> None:
        pass

    def add_object(self, object: str) -> None:
        raise NotImplemented

    def remove_object(self, object: str) -> None:
        raise NotImplemented

    def get_objects(self) -> List[Tuple[str, int]]:
        raise NotImplemented


