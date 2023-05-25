import pygame
import time

################### PARAMETERS ######################
from parameters import GameParameters as GP
from parameters import Color
#####################################################

################# FOR TEST ##########################
from module_Trig_and_Key import Trig, KeyFromKeyboard
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
        ######### TEST #########
        self.key_ENTER = KeyFromKeyboard('ENTER')
        self.execute_once = True
        self.sprite = None
        ########################

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

    def test_show_photos_animation(self, window: pygame.surface, scale: int = 1, time_for_displaying: int = 5/10, verbose: bool = True):
        '''
        Show animation of photos one by one

        * window (pygame.surface) - indicate the plane on which the animation is to be displayed
        * scale (int) - value 1 is default
        * time_for_displaying (int) - time for displaying, by default 0,5 sec
        * verbose (bool) - information about the width and height of the image
        '''

        scaled_surface, width, height = self.test_scale_the_image(scale)

        if verbose:
            print(f'{width} x {height}')

        window.blit(scaled_surface, (0, 0))

        # wait
        time.sleep(time_for_displaying)

    def test_press_enter_to_show_next_photo(self, window: pygame.surface, scale: int = 1, verbose: bool = True):
        '''
        Press enter to view the next photo

        * window (pygame.surface) - indicate the plane on which the animation is to be displayed
        * scale (int) - value 1 is default
        * verbose (bool) - information about the width and height of the image        
        '''

        if (self.key_ENTER.key_return_trig() or self.execute_once):

            self.execute_once = False

            self.sprite, width, height = self.test_scale_the_image(scale)

            if verbose:
                print(f'{width} x {height}')

        window.blit(self.sprite, (0, 0))

    def test_scale_the_image(self, scale: int):
        '''
        Method returned scaled surface also do gives width and height of original picture 

        * scale (int)
        '''

        scaled_surface = next(self)
        width = scaled_surface.get_width()
        height = scaled_surface.get_height()

        scaled_surface = pygame.transform.scale(
            scaled_surface, (width*scale, height*scale))

        return scaled_surface, width, height

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

    ############################################
    #####           Only for test (main)    ####
    ############################################


def main():

    ############################################
    ###        FOR Test CLASS Picture        ###
    ############################################

    pygame.init()
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Fonts test")

    font_digits_one = Picture.init_from_dataclass(
        GP.Fonts_EXPANDED.FIRST_Digits)

    font_letters_one = Picture.init_from_dataclass(
        GP.Fonts_EXPANDED.FIRST_Letters)

    font_digits_two = Picture.init_from_dataclass(
        GP.Fonts_EXPANDED.SECOND_Digits)

    font_letters_two = Picture.init_from_dataclass(
        GP.Fonts_EXPANDED.SECOND_Letters)

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

        ####################################################################
        # • Checked: imgs\digits\game-font-pixel-art-8bit-style-numbers.png
        if False:  # showing all image of:                                                  imgs\digits\game-font-pixel-art-8bit-style-numbers.png
            font_digits_one.test_show_vertically_side_by_side(window, 5, True)
        if False:  # showing continuous animation of:                                       imgs\digits\game-font-pixel-art-8bit-style-numbers.png
            font_digits_one.test_show_photos_animation(window)
        if False:  # displaying picture by picture after pressing enter:                     imgs\digits\game-font-pixel-art-8bit-style-numbers.png
            font_digits_one.test_press_enter_to_show_next_photo(window, 3)
        ####################################################################

        ####################################################################
        # • Checked:  imgs\letters\game-font-pixel-art-8bit-style-letters.png
        if False:  # showing all image of:                                              imgs\letters\game-font-pixel-art-8bit-style-letters.png
            font_letters_one.test_show_vertically_side_by_side(window, 5, True)
        if False:  # showing continuous animation of:                                   imgs\letters\game-font-pixel-art-8bit-style-letters.png
            font_letters_one.test_show_photos_animation(window, 5)
        if False:  # displaying picture by picture after pressing enter:                 imgs\letters\game-font-pixel-art-8bit-style-letters.png
            font_letters_one.test_press_enter_to_show_next_photo(window, 3)
        ####################################################################

        ####################################################################
        # • In Progress:  imgs\digits\pixel-alphabet-font-numbers-set-video-computer-game-retro-8-bit-style.png
        if False:  # showing all image of:                                            imgs\digits\pixel-alphabet-font-numbers-set-video-computer-game-retro-8-bit-style.png
            font_digits_two.test_show_vertically_side_by_side(window, 5, True)
        if False:  # displaying picture by picture after pressing enter:              imgs\digits\pixel-alphabet-font-numbers-set-video-computer-game-retro-8-bit-style.png
            font_digits_two.test_press_enter_to_show_next_photo(window, 3)
        ####################################################################

        ####################################################################
        # • In Progress:  imgs\letters\pixel-alphabet-font-letters-set-video-computer-game-retro-8-bit-style.png
        if False:  # showing all image of:                                           imgs\letters\pixel-alphabet-font-letters-set-video-computer-game-retro-8-bit-style.png
            font_letters_two.test_show_vertically_side_by_side(window, 5, True)
        if True:  # displaying picture by picture after pressing enter:              imgs\letters\pixel-alphabet-font-letters-set-video-computer-game-retro-8-bit-style.png
            font_letters_two.test_press_enter_to_show_next_photo(window, 3)
        ####################################################################

        ####################
        ##     UNTIL      ##
        ####################

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
