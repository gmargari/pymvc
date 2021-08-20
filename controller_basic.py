from controller import Controller
from model import Model
from typing import List
from view import View


class BasicController(Controller):
    def __init__(self, model: Model, views: List[View]) -> None:
        super().__init__(model, views)

    def view_changed(self, *args, **kwargs) -> None:
        if args[0] == 'add':
            fruit = args[1]
            self.add_fruit(fruit)
        elif args[0] == 'remove':
            fruit = args[1]
            self.remove_fruit(fruit)
        elif args[0] == 'show':
            self.show_fruits()
        elif args[0] == 'quit':
            self.quit()

    def add_fruit(self, fruit: str) -> None:
        self.model.add_object(fruit)

    def remove_fruit(self, fruit: str) -> None:
        self.model.remove_object(fruit)

    def show_fruits(self) -> None:
        for view in self.views:
            view.show_objects(self.model.get_objects())
