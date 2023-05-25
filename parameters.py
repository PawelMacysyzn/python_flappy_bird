# FILE CONFIG FOR VAR, FOR GAME SETTINGS

class Color:

    GREEN_SCREEN = (124, 252, 0)   # Green color for screen
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED   = (255, 0, 0)
    GREAN = (0, 255, 0)
    ALPHA = (0)


class GameParameters:

    FRAMERATE = 60
    NAME_OF_LOG = "My Gmae"


    class Windows:

        SIZE_X = 800 # (int) - game screen width (default value: 800)
        SIZE_Y = 800 # (int) - game screen height (default value: 800)


    class Player:

        IMAGE = r'imgs\flappy_sprite.png' # (str) - location of the .png file
        IMAGE_COLUMNS = 4     # (int) - how many columns in sprite
        IMAGE_ROWS = 1        # (int) - how many rows in sprite
        IMAGE_ALFA_COLOR = 'RED'    # (str) - base color
        IMAGE_SCALING = 0.25        # (float or int) - scaling by this value

        STARTING_SCORE = 0          # The player's starting score


    class Obstacle:

        GAP = 400           # (int) - sets the spacing between another walls
        WALL_SPEED = 100    # (int) - sets speed of moving walls
        OBSTACLE_IMAGE = r'imgs\pipe-green.png'  # (str) - location of the .png file


    class Button:

        IMAGE = r'imgs\\mute_sprite.png' # (str) - location of the .png file
        IMAGE_COLUMNS = 2                # (int) - how many columns in sprite
        IMAGE_ROWS = 1                   # (int) - how many rows in sprite
        IMAGE_ALFA_COLOR = 'BLACK'       # (str) - base color
        IMAGE_SCALING = 1                # (float or int) - scaling by this value


    class Background:

        IMAGE = r'imgs\\background_full_width.png' # (str) - location of the .png file
        BASE_BACKGROUND = Color.GREEN_SCREEN

    class MusicBackground:

        SOUND_PATH = 'music\\bensound-summer_ogg_music.ogg' # (str) - location of the .ogg file

    class Fonts:

        class Digits:

            FIRST_IMAGE =  r'imgs\digits\game-font-pixel-art-8bit-style-numbers.png' # (str) - location of the .png file
            SECOND_IMAGE = r'imgs\digits\pixel-alphabet-font-numbers-set-video-computer-game-retro-8-bit-style.png' # (str) - location of the .png file

        class Letters:

            FIRST_IMAGE =  r'imgs\letters\game-font-pixel-art-8bit-style-letters.png' # (str) - location of the .png file
            SECOND_IMAGE = r'imgs\letters\pixel-alphabet-font-letters-set-video-computer-game-retro-8-bit-style.png' # (str) - location of the .png file




    class Fonts_EXPANDED:

        class FIRST_Digits:

            SPRITE =  r'imgs\digits\game-font-pixel-art-8bit-style-numbers.png' # (str) - location of the .png file
            HOW_MANY_COLUMNS = 10
            HOW_MANY_ROWS = 1
            ALFA_COLOR = Color.GREEN_SCREEN
            SCALING = 2

        class SECOND_Digits:

            SPRITE = r'imgs\digits\pixel-alphabet-font-numbers-set-video-computer-game-retro-8-bit-style.png' # (str) - location of the .png file
            HOW_MANY_COLUMNS = 10
            HOW_MANY_ROWS = 1
            ALFA_COLOR = Color.ALPHA
            SCALING = 1/3 

        class FIRST_Letters:    
            
            SPRITE = r'imgs\letters\game-font-pixel-art-8bit-style-letters.png' # (str) - location of the .png file
            HOW_MANY_COLUMNS = 9
            HOW_MANY_ROWS = 3
            ALFA_COLOR = Color.WHITE
            SCALING = 3 

        class SECOND_Letters:    
            
            SPRITE = r'imgs\letters\pixel-alphabet-font-letters-set-video-computer-game-retro-8-bit-style.png' # (str) - location of the .png file
            HOW_MANY_COLUMNS = 9
            HOW_MANY_ROWS = 4
            ALFA_COLOR = Color.ALPHA
            SCALING = 1/3 

































        