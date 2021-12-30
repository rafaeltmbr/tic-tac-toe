from packages.Board import Board


class Game:
    def __init__(self):
        print('Game instance')
        self.board = Board()

        self.board.draw_squares([
            'o', 'o', 'X',
            '', 'X', 'o',
            'X', '', 'x'
        ])

        self.board.on_mouse_click(self._mouse_click_handler)
        self.board.on_keyboard_press(self._keyboard_press_handler)
        self.board.loop()

    def _mouse_click_handler(self, coordinate):
        print('Clicked:', coordinate)

    def _keyboard_press_handler(self, keyinfo):
        print('Pressed:', keyinfo)
