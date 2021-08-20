from model_basic import BasicModel
from view_terminal import TerminalView
from view_gui import GUIView
from controller_basic import BasicController


class MyApp(object):
    def __init__(self) -> None:
        model = BasicModel()
        view = TerminalView()
        #view = GUIView()
        self.controller = BasicController(model, view)

    def run(self) -> None:
        self.controller.run()

app = MyApp()
app.run()