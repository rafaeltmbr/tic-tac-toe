import tkinter

from .board_config import config
from .board_config import squares_coordinates
from .board_config import image_padding


class Board:
    def __init__(self):
        self.tk = tkinter.Tk()
        self._start()

    def _start(self):
        self.tk.title('Tic-tac-toe')

        self.canvas = tkinter.Canvas(
            self.tk,
            width=config['dimensions']['board'],
            height=config['dimensions']['board'],
            bg=config['colors']['board'],
        )

        self.canvas.pack()

        self.images = {
            'x':    tkinter.PhotoImage(file='assets/images/x_small.png'),
            'o':    tkinter.PhotoImage(file='assets/images/o_small.png'),
        }

        self.draw_squares(['', '', '', '', '', '', '', '', ''])

        self.tk.mainloop()

    def draw_squares(self, squares):
        # clear the canvas
        self.canvas.delete('all')

        # draw each square
        for i in range(0, 9):
            square_coordinate = squares_coordinates[i]
            square_type = squares[i]
            self._draw_square(square_coordinate, square_type)

    def _draw_square(self, square_coordinate, square_type):
        self._draw_rectangle(square_coordinate, square_type)

        if square_type.lower() == 'x':
            self._draw_image(square_coordinate, 'x')
        elif square_type.lower() == 'o':
            self._draw_image(square_coordinate, 'o')

    def _draw_rectangle(self, square_coordinate, square_type):
        self.canvas.create_rectangle(
            square_coordinate['x'],
            square_coordinate['y'],
            square_coordinate['x'] + config['dimensions']['square'],
            square_coordinate['y'] + config['dimensions']['square'],
            fill=self._get_square_color(square_type),
            outline=self._get_square_color(square_type)
        )

    def _draw_image(self, square_coordinate, image_type):
        self.canvas.create_image(
            square_coordinate['x'] + image_padding,
            square_coordinate['y'] + image_padding,
            image=self.images[image_type],
            anchor='nw'
        )

    def _get_square_color(self, type):
        return config['colors']['square_highlight'] \
            if type.isupper() \
            else config['colors']['square']