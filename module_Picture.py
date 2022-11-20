import pygame
import time


class Picture:
    '''
    # Convert sprite to list<Surface>
    It also includes test methods:
    * show_photos_animation(self, window: pygame.surface)
    '''

    def __init__(self, sprite_location, how_many_columns, how_many_rows, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_columns (int) - how many columns in sprite
        * how_many_rows (int) - how many rows in sprite
        * alfa_color (str) - base color from: ['WHITE', 'BLACK', 'RED', 'FALSE']
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

    @staticmethod
    def test_show_background_color(window: pygame.surface):
        '''
        Show background color, important !!!
        # ! Call first !

        * window (pygame.surface) - indicate the plane on which the animation is to be displayed
        '''

        # Initialing RGB Color
        color = (255, 0, 0)

        window.fill(color)
        pass

    @staticmethod
    def do_sprite(image, how_many_columns, how_many_rows, which_frame, alfa_color, scaling) -> pygame.Surface:
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


def main():

    ############################################
    ###        FOR Test CLASS Picture        ###
    ############################################
    TIME_FOR_DISPLAYING = 5/10  # s

    pygame.init()
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Fonts test")

    image = r'imgs\digits\game-font-pixel-art-8bit-style-numbers.jpg'
    digits1 = Picture(image, 10, 1, 'WHITE', 1)

    image = r'imgs\letters\game-font-pixel-art-8bit-style-letters.jpg'
    letters1 = Picture(image, 9, 3, 'WHITE', 1)

    image = r'imgs\digits\pixel-alphabet-font-numbers-set-video-computer-game-retro-8-bit-style.jpg'
    digits2 = Picture(image, 10, 1, 'WHITE', 1/3)

    image = r'imgs\letters\pixel-alphabet-font-letters-set-video-computer-game-retro-8-bit-style.jpg'
    letters2 = Picture(image, 9, 4, 'WHITE', 1/3)

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

        # digits1.test_show_photos_animation(window)
        # digits1.test_show_vertically_side_by_side(window, 5, True)

        # letters1.test_show_photos_animation(window)
        # letters1.test_show_vertically_side_by_side(window, 5, True)

        # digits2.test_show_photos_animation(window)
        # digits2.test_show_vertically_side_by_side(window, 5, True)

        # letters2.test_show_vertically_side_by_side(window, 5, True)
        # letters2.test_show_photos_animation(window)

        ####################
        ##     UNTIL      ##
        ####################

        # wait
        time.sleep(TIME_FOR_DISPLAYING)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
