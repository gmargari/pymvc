from typing import Callable, List


class Observable(object):
    def __init__(self) -> None:
        self.observers: List[Callable] = []

    def add_observer(self, callback: Callable) -> Callable:
        self.observers.append(callback)
        return callback

    def notify_observers(self, *args, **kwargs) -> None:
        for callback in self.observers:
            callback(*args, **kwargs)
