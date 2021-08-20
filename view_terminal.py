from typing import List, Tuple
from view import View
import sys


class TerminalView(View):
    def __init__(self) -> None:
        super().__init__()

    def show_objects(self, objects: List[Tuple[str, int]]) -> None:
        print('\n'.join('%-10s: %3d' % (name, num) for name, num in objects))

    def main_loop(self) -> None:
        while True:
            print('-' * 30)
            print('a <fruit>: add fruit\nr <fruit>: remove fruit\ns: show fruits\nq: quit')
            print('-' * 30)

            words = input().split()

            if not len(words):
                continue
            if words[0] == 'a':
                fruit = words[1]
                self.notify_observers('add', fruit)
            elif words[0] == 'r':
                fruit = words[1]
                self.notify_observers('remove', fruit)
            elif words[0] == 's':
                self.notify_observers('show')
            elif words[0] == 'q':
                self.notify_observers('quit')
                break

    def quit(self) -> None:
        pass
