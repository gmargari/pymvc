from model import Model
import sys
from typing import List
import threading
import time
from view import View


class Controller:
    def __init__(self, model: Model, views: List[View]) -> None:
        self.model = model
        self.views = views

    def view_changed(self, *args, **kwargs) -> None:
        raise NotImplemented

    def run(self) -> None:
        # If any of the views is modified, call view_changed()
        for view in self.views:
            view.register(self.view_changed)

        # Run each view in its own thread
        self.threads = []
        for view in self.views:
            thread = threading.Thread(target=view.run, daemon=True)
            thread.start()
            self.threads.append(thread)

        # Wait all threads
        for thread in self.threads:
            thread.join()

    def quit(self) -> None:
        # Gracefully terminate each view
        for view in self.views:
            view.quit()

        # Terminate program
        sys.exit(0)
