config = {
    'dimensions': {
        'board': 400,
        'square': 130,
        'image': 80
    },
    'colors': {
        'board': '#4D51A3',
        'square': '#282A31',
        'square_highlight': '#333562'
    }
}

division_width = round((config['dimensions']['board'] -
                       (config['dimensions']['square'] * 3)) / 2)

image_padding = round(
    (config['dimensions']['square'] - config['dimensions']['image']) / 2)

start_square_coordinate = 0
middle_square_coordinate = config['dimensions']['square'] + \
    division_width
end_square_coordinate = 2 * middle_square_coordinate

squares_coordinates = [
    {'x': start_square_coordinate, 'y': start_square_coordinate},
    {'x': middle_square_coordinate, 'y': start_square_coordinate},
    {'x': end_square_coordinate, 'y': start_square_coordinate},
    {'x': start_square_coordinate, 'y': middle_square_coordinate},
    {'x': middle_square_coordinate, 'y': middle_square_coordinate},
    {'x': end_square_coordinate, 'y': middle_square_coordinate},
    {'x': start_square_coordinate, 'y': end_square_coordinate},
    {'x': middle_square_coordinate, 'y': end_square_coordinate},
    {'x': end_square_coordinate, 'y': end_square_coordinate},
]
