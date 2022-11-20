class GameParameters:

    FRAMERATE = 60
    NAME_OF_LOG = "My Gmae"

    class Player:

        IMAGE = r'imgs\flappy_sprite.png' # (str) - location of the .png file
        IMAGE_COLUMNS = 4     # (int) - how many columns in sprite
        IMAGE_ROWS = 1        # (int) - how many rows in sprite
        IMAGE_ALFA_COLOR = 'RED'    # (str) - base color
        IMAGE_SCALING = 0.25        # (float or int) - scaling by this value

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













































        