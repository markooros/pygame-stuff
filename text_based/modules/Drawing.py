class DrawingParameters(object):
    def __init__(self):
        self.colors = self.define_colors()

    def define_colors(self):
        colors = {}
        black = (0, 0, 0)
        grey = (100, 100, 100)
        red = (220, 20, 60)
        blue = (30, 144, 255)
        green = (50, 205, 50)
        colors['black'] = black
        colors['grey'] = grey
        colors['red'] = red
        colors['blue'] = blue
        colors['green'] = green
        return colors

    def get_colors(self):
        return self.colors