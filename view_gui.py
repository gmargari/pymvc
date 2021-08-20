from typing import List, Tuple
import PySimpleGUI as sg  # type: ignore
from view import View


class GUIView(View):
    def __init__(self) -> None:
        super().__init__()
        layout = [
            [sg.Input(key='fruit'), sg.Button('Add'), sg.Button('Remove')],
            [sg.Button('Show')],
            [sg.Text('', key='fruits_label')],
        ]
        self.window = sg.Window('Fruit Database', layout)

    def show_objects(self, objects: List[Tuple[str, int]]) -> None:
        self.window['fruits_label'].update('\n'.join('%-10s: %3d' % (name, num) for name, num in objects))

    def main_loop(self) -> None:
        while True:
            event, values = self.window.read()

            if event == 'Add':
                fruit = values['fruit']
                self.notify_observers('add', fruit)
            elif event == 'Remove':
                fruit = values['fruit']
                self.notify_observers('remove', fruit)
            elif event == 'Show':
                self.notify_observers('show')
            elif event == sg.WINDOW_CLOSED or event == 'Quit':
                self.notify_observers('quit')
                break

    def quit(self) -> None:
        self.window.close()