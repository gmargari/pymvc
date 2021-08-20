import asyncio
from model import Model
import sys
from typing import List
import threading
import time
from view import View


class Controller(object):
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def view_changed(self, *args, **kwargs) -> None:
        raise NotImplemented

    def run(self) -> None:
        # If view is modified, call view_changed()
        self.view.register(self.view_changed)

        # Run view
        self.view.main_loop()

    def quit(self) -> None:
        # Gracefully terminate each view
        self.view.quit()

        # Terminate program
        sys.exit(0)
