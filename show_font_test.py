import pygame
import time


class Picture:
    '''
    # Convert sprite to list<Surface>
    '''

    def __init__(self, sprite_location, how_many_columns, how_many_rows, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_columns (int) - how many columns in sprite
        * how_many_rows (int) - how many rows in sprite
        * alfa_color (str) - base color
        * scaling (float or int) - scaling by this value
        '''
        self.sprite_location = sprite_location
        self.how_many_columns = how_many_columns
        self.how_many_rows = how_many_rows
        self.how_many_frames = self.how_many_columns * self.how_many_rows
        self.alfa_color = alfa_color
        self.scaling = scaling

        self.current_state = 1
        self.list_of_images = self.preload_images_from_sprite()

    def preload_images_from_sprite(self) -> list:
        '''
        return list of Surface
        '''
        return [self.do_sprite(self.sprite_location, self.how_many_columns, self.how_many_rows, which_frame, self.how_many_frames, self.alfa_color, self.scaling) for which_frame in range(self.how_many_frames)]

    @staticmethod
    def do_sprite(image, how_many_columns, how_many_rows, which_frame, how_many_frames, alfa_color, scaling) -> pygame.Surface:
        spride_sheet_image = pygame.image.load(image).convert_alpha()

        set_colorkey = True
        if alfa_color.upper() == 'WHITE':
            alfa_color = (255, 255, 255)
        elif alfa_color.upper() == 'BLACK':
            alfa_color = (0, 0, 0)
        elif alfa_color.upper() == 'RED':
            alfa_color = (255, 0, 0)
        elif alfa_color.upper() == 'FALSE':
            set_colorkey = False

        width = spride_sheet_image.get_width() / how_many_columns
        height = spride_sheet_image.get_height() / how_many_rows

        # retur current row
        current_column, current_row = Picture.get_current_row(
            which_frame, how_many_columns, how_many_rows)

        image = pygame.Surface((width, height)).convert_alpha()

        image.blit(spride_sheet_image, (0, 0),
                   ((current_column*width),  (current_row*height), width, height))

        image = pygame.transform.scale(image, (width*scaling, height*scaling))

        if set_colorkey:
            image.set_colorkey(alfa_color)
        return image

    @staticmethod
    def get_current_row(frame: int, how_many_columns: int, how_many_rows: int):
        '''
        # retur current column and row
        '''
        frame += 1
        for row in range(how_many_rows):
            if frame > (how_many_columns * row) and frame <= (how_many_columns * (row+1)):
                column = frame - (how_many_columns * row)
                return column - 1, row

############################################


image_path_digits = r'imgs\digits\game-font-pixel-art-8bit-style-numbers.jpg'
image_path_letters = r'imgs\letters\game-font-pixel-art-8bit-style-letters.jpg'


pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fonts test")


digits = Picture(image_path_digits, 10, 1, 'BLACK', 1)
iter_digits = iter(digits.list_of_images)

letters = Picture(image_path_letters, 9, 3, 'BLACK', 1)
iter_letters = iter(letters.list_of_images)


def show_animation(window: pygame.surface, list_of_picture: iter):
    window.blit(next(list_of_picture), (0, 0))


def show_vertical(window: pygame.surface, list_of_picture: list, how_many_columns: int, how_many_rows: int, space: int = 5, verbose: bool = False):

    frame = 0
    sbc = 0 # space between columns
    width = list_of_picture[frame].get_width()
    height = list_of_picture[frame].get_height()
    if verbose:
        print(f'{width} x {height}')

    for row in range(how_many_rows):
        for column in range(how_many_columns):
            if row: # for row > 0
                sbc = space
            window.blit(list_of_picture[frame], ((width + sbc )* row , height * column))
            frame += 1


while True:
    # event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit pygame
            pygame.quit()

    ####################
    ##   CODE HERE    ##
    ####################

    # show_animation(window, iter_digits)
    show_animation(window, iter_letters)
    # show_vertical(window, digits.list_of_images, 10, 1)
    # show_vertical(window, letters.list_of_images, 9, 3)

    # wait
    time.sleep(0.5)

    # Update the display
    pygame.display.flip()
