import pygame
import time

################### PARAMETERS ######################
from parameters import GameParameters as GP
from parameters import Color
#####################################################


class DataClassSprite:

    SPRITE: str
    HOW_MANY_COLUMNS: int
    HOW_MANY_ROWS: int
    ALFA_COLOR: tuple
    SCALING: int


class Picture:
    '''
    # Convert sprite to list<Surface>

    It also includes test methods:
    * test_show_photos_animation(self, window: pygame.surface)
    * test_show_vertically_side_by_side(self, window: pygame.surface, space: int = 5, verbose: bool = False)
    * test_show_background_color(window: pygame.surface)
    '''

    def __init__(self, sprite_location, how_many_columns, how_many_rows, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_columns (int) - how many columns in sprite
        * how_many_rows (int) - how many rows in sprite
        * alfa_color (str) - base color from: ['WHITE', 'BLACK', 'RED', 'FALSE', '']
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
        self.i = 0

    def __next__(self):
        if self.i == len(self.list_of_images):
            raise StopIteration()

        ret = self.list_of_images[self.i]
        self.i += 1
        return ret

    def __iter__(self):
        return self

    def preload_images_from_sprite(self) -> list:
        '''
        return list of Surface
        '''
        return [self.do_sprite(self.sprite_location, self.how_many_columns, self.how_many_rows, which_frame, self.alfa_color, self.scaling) for which_frame in range(self.how_many_frames)]

    def test_show_photos_animation(self, window: pygame.surface):
        '''
        Show animation of photos one by one

        * window (pygame.surface) - indicate the plane on which the animation is to be displayed

        '''
        window.blit(next(self), (0, 0))

    def test_show_vertically_side_by_side(self, window: pygame.surface, space: int = 5, verbose: bool = False):
        '''
        Show pictures vertically side by side

        * window (pygame.surface) - indicate the plane on which the animation is to be displayed
        * space (int) - set blank area between columns of photos
        * verbose (bool) - information about the width and height of the image

        '''
        frame = 0
        sbc = 0  # space between columns
        width = self.list_of_images[frame].get_width()
        height = self.list_of_images[frame].get_height()
        if verbose:
            print(f'{width} x {height}')

        for row in range(self.how_many_rows):
            for column in range(self.how_many_columns):
                if row:  # for row > 0
                    sbc = space
                window.blit(self.list_of_images[frame],
                            ((width + sbc) * row, height * column))
                frame += 1

    @classmethod
    def init_from_dataclass(cls, spriteData: DataClassSprite = None) -> None:
        '''
        * spriteData (DataClassSprite) - DataClassSprite object
        '''
        return cls(
            sprite_location=spriteData.SPRITE,
            how_many_columns=spriteData.HOW_MANY_COLUMNS,
            how_many_rows=spriteData.HOW_MANY_ROWS,
            alfa_color=spriteData.ALFA_COLOR,
            scaling=spriteData.SCALING)

    @staticmethod
    def test_show_background_color(window: pygame.surface):
        '''
        Show background color, important !!!
        # ! Call first !

        * window (pygame.surface) - indicate the plane on which the animation is to be displayed
        '''

        # Initialing RGB Color
        color = Color.RED

        window.fill(color)
        pass

    @staticmethod
    def do_sprite(image, how_many_columns, how_many_rows, which_frame, alpha_color, scaling) -> pygame.Surface:

        spride_sheet_image = pygame.image.load(image)

        # everything besides int and tuple
        if not(type(alpha_color) is (int) or type(alpha_color) is (tuple)):

            if alpha_color.upper() == 'WHITE':
                alpha_color = Color.WHITE
            elif alpha_color.upper() == 'BLACK':
                alpha_color = Color.BLACK
            elif alpha_color.upper() == 'RED':
                alpha_color = Color.RED
            elif alpha_color.upper() == 'GREAN':
                alpha_color = Color.GREAN
            elif alpha_color.upper() == 'GREEN SCREEN':
                alpha_color = Color.GREEN_SCREEN
            elif alpha_color.upper() == ('FALSE'):
                alpha_color = Color.ALPHA
            elif alpha_color == (''):
                alpha_color = Color.ALPHA

        width = spride_sheet_image.get_width() / how_many_columns
        height = spride_sheet_image.get_height() / how_many_rows

        # retur current current_column, current_row
        current_column, current_row = Picture.get_current_row(
            which_frame, how_many_columns, how_many_rows)

        image = pygame.Surface((width, height))  # .convert_alpha()

        image.blit(spride_sheet_image, (0, 0),
                   ((current_column*width),  (current_row*height), width, height))

        image = pygame.transform.scale(
            image, (width*scaling, height*scaling))  # .convert_alpha()

        image.set_colorkey(alpha_color)

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


def main():

    ############################################
    ###        FOR Test CLASS Picture        ###
    ############################################
    TIME_FOR_DISPLAYING = 5/10  # s

    pygame.init()
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Fonts test")

    # font_digits_one = Picture(GP.Fonts.Digits.FIRST_IMAGE, 10, 1, '', 3)  # OLD
    font_digits_one = Picture.init_from_dataclass(
        GP.Fonts_EXPANDED.FIRST_Digits)  # NEW ONE

    font_letters_one = Picture(GP.Fonts.Letters.FIRST_IMAGE, 9, 3, 'WHITE', 1)

    font_digits_two = Picture(GP.Fonts.Digits.SECOND_IMAGE, 10, 1, '', 1/3)

    font_letters_two = Picture(
        GP.Fonts.Letters.SECOND_IMAGE, 9, 4, 'WHITE', 1/3)

    while True:
        # event handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit pygame
                pygame.quit()

        ####################
        ##   CODE HERE    ##
        ####################
        # TO ADD CANAL ALFA !!!

        Picture.test_show_background_color(window)

        # font_digits_one.test_show_vertically_side_by_side(window, 5, True)
        font_digits_one.test_show_photos_animation(window)

        # font_letters_one.test_show_vertically_side_by_side(window, 5, True)
        # font_letters_one.test_show_photos_animation(window)

        # font_digits_two.test_show_vertically_side_by_side(window, 5, True)
        # font_digits_two.test_show_photos_animation(window)

        # font_letters_two.test_show_vertically_side_by_side(window, 5, True)
        # font_letters_two.test_show_photos_animation(window)

        # image = pygame.image.load(GP.Fonts.Digits.FIRST_IMAGE).convert_alpha()
        # rect = image.get_rect()
        # print(rect)
        # window.blit(image, (100,100))

        ####################
        ##     UNTIL      ##
        ####################

        # wait
        time.sleep(TIME_FOR_DISPLAYING)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
