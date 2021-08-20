from controller import Controller
from model import Model
from typing import List
from view import View


class BasicController(Controller):
    def __init__(self, model: Model, views: List[View]) -> None:
        super().__init__(model, views)

    def add_fruit(self, fruit: str) -> None:
        self.model.add_object(fruit)

    def remove_fruit(self, fruit: str) -> None:
        self.model.remove_object(fruit)
