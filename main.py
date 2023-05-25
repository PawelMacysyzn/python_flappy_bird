import threading
import pygame
from pygame import mixer  # for import music
from random import randint  # for generate walls
from typing import Dict, List

################### MODULES #########################
from module_Picture import Picture
from module_Trig_and_Key import Trig, KeyFromKeyboard

################### PARAMETERS ######################
from parameters import GameParameters as GameParam
from parameters import Color
#####################################################


class Game:
    '''
     # Creates a game # 
     * initialize pygame
     * initialize game clock
     * configures the game window
    '''

    def __init__(self,
                 windows_size_x: int = GameParam.Windows.SIZE_X,
                 windows_size_y: int = GameParam.Windows.SIZE_Y
                 ) -> None:
        '''
        * windows_size_x (int) - game screen width
        * windows_size_y (int) - game screen height

        '''

        # initialize pygame
        pygame.init()
        # initialize game clock
        self.clock = pygame.time.Clock()

        self.windows_size = (windows_size_x, windows_size_y)  # width X height
        # configures the game window
        self.window = pygame.display.set_mode(self.windows_size)

        #### PARAMETERS ####

        self.framerate = GameParam.FRAMERATE

        ####################

        # freezes the game
        self.pause = False
        # game over
        self.gameover = False
        # resume
        self.resume = False
        # infinite loop game
        self.running = True
        # shows frames in ms
        self.delta_time = None
        # clik button state
        self.click_mouse = None

        # TO DISPLAY THE SCORE TO THE PLAYER #
        self.show_score = Score(self.windows_size)

        pass

    def name_of_log(self, name_str):
        # to do, show session and user in bar
        pygame.display.set_caption(name_str.upper())

    def clock_support(self):
        # self.framerate = 60
        # dt show how many milliseconds have passed since the previous call
        # the program will never run at more than self.framerate frames per second
        # if pause or game over is pressed freeze the game
        if game.pause or game.gameover:
            self.delta_time = 0
        else:
            self.delta_time = self.clock.tick(self.framerate)
        # print(delta_time, " ms")
        # print("{:.1f} FPS".format(clock.get_fps()))
        pass

    def show_character_statistics(self, what):
        # temporary
        pos_x, pos_y = 0, 0
        speed_y, counter_jump = 0, 0

        if what.upper() == 'ALL':
            what = 1
        elif what.upper() == 'FPS':
            what = 2
        elif what.upper() == 'NONE':
            what = 0

        if not what == 0:
            font = pygame.font.SysFont('Comic Gecko', 30)
            position_x = 180
            position_y = 10
            next_width = 100
            next_width_1 = 25
            color_font = (255, 255, 255)

            label_7 = font.render("FPS:", 1, color_font)
            label_8 = font.render(
                str("{:.1f}".format(game.clock.get_fps())), 1, color_font)

            position_x -= next_width
            self.window.blit(
                label_7, (self.windows_size[0] - position_x - 15, position_y))
            self.window.blit(
                label_8, (self.windows_size[0] - position_x + label_7.get_width() - 10, position_y))

            if not what == 2:
                label_1 = font.render("X:", 1, color_font)
                label_2 = font.render(str(pos_x), 1, color_font)
                label_3 = font.render("Y:", 1, color_font)
                label_4 = font.render(
                    str("{:.1f}".format(pos_y)), 1, color_font)
                label_5 = font.render("R:", 1, color_font)
                label_6 = font.render(
                    str("{:.1f}".format(1)), 1, color_font)
                label_9 = font.render("speed_y:", 1, color_font)
                label_10 = font.render(
                    str("{:.1f}".format(speed_y)), 1, color_font)
                label_11 = font.render("counter_jump:", 1, color_font)
                label_12 = font.render(str(counter_jump), 1, color_font)

                # NEXT LINE
                position_y += 50
                position_x += next_width
                # next stat X
                self.window.blit(
                    label_1, (self.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_2, (self.windows_size[0] - position_x + next_width_1, position_y))
                # next stat Y
                position_x -= next_width
                self.window.blit(
                    label_3, (self.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_4, (self.windows_size[0] - position_x + next_width_1, position_y))

                # NEXT LINE
                position_y += 50

                # next line R
                position_x += next_width
                self.window.blit(
                    label_5, (self.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_6, (self.windows_size[0] - position_x + next_width_1, position_y))

                # NEXT LINE
                position_y += 50

                # next stat V
                # next stat speed_y
                self.window.blit(
                    label_9, (self.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_10, (self.windows_size[0] - position_x + next_width_1 + 75, position_y))

                # NEXT LINE
                position_y += 50

                # next stat counter_jump
                position_x += next_width
                self.window.blit(
                    label_11, (self.windows_size[0] - position_x + 100, position_y))
                self.window.blit(
                    label_12, (self.windows_size[0] - position_x + next_width_1 + 225, position_y))

    def show_character_score(self, character_score: int) -> None:

        self.show_score.show_score(character_score)

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # handling button "X"
                self.running = False
            # mouse button operation
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click_mouse = True
            else:
                self.click_mouse = False
            pass

    def logic_gameover_pause_resume(self):
        '''
        handling:   \n
        - pause key   (freezes the game, allow for re-opening)      \n
        - gameover    (freezes the game)                            \n
        - resume game (clear all obsticles; resume the game)        \n
        '''
        # pause key
        if not self.gameover:
            self.pause = key_pause.return_curent_state()

        # test gameover key ! to deactivate !
        if not self.pause:
            self.gameover = key_test_gameover.return_curent_state(
            ) or player.outside_player_is_kill_and_game_over

        # resume key
        self.resume = key_resume.key_return_trig()

        if self.gameover:
            key_pause.reset()
            button_mute.reset(True)

        else:
            button_mute.reset(False)

        if self.gameover and self.resume:
            self.gameover = False
            key_test_gameover.reset()
            button_mute.set_state()

            player.player_reset_score()

            # clear all obsticles
            obstacle.remove_all_items()
            # print("P:", self.pause, " G:", self.gameover, " R:", self.resume)
            pass

    def logic_buton_mute(self):
        # draw button mute
        button_mute.draw_button()
        button_mute.change_of_state()
        if button_mute.current_state == 1:
            song_background.do_music(True)
        else:
            song_background.do_music(False)


class Button(Picture):
    """
    # Creates a button
    """

    def __init__(self, sprite_location, how_many_columns, how_many_rows, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_images (int) - how many images in sprite
        * alfa_color (str) - base color
        * scaling (float or int) - scaling by this value
        '''

        self.trig_0, self.trig_1, self.p_trig, self.counter_trig = None, None, None, 0
        self.res_trig_0, self.res_trig_1, self.res_p_trig, self.res_counter_trig = None, None, None, 0

        self.current_state = 1
        self.how_many_images = how_many_columns * how_many_rows
        self.images = Picture(
            sprite_location, how_many_columns, how_many_rows, alfa_color, scaling)

    def draw_button(self):

        self.button_surf = self.images.list_of_images[self.current_state]

        # button position
        pos_x = game.window.get_width() - self.button_surf.get_width()
        pos_y = game.window.get_height() - self.button_surf.get_height()
        self.pos_button = pos_x, pos_y
        # draw button
        game.window.blit(self.button_surf, self.pos_button)

    def mouse_is_over_the_button(self):
        button_rect = self.button_surf.get_rect(topleft=(self.pos_button))
        button_mask = pygame.mask.from_surface(self.button_surf)

        # pos_mouse = pygame.mouse.get_pos(center=(button_mute_rect))
        pos_mouse = pygame.mouse.get_pos()

        pos_in_mask = pos_mouse[0] - \
            button_rect.x, pos_mouse[1] - button_rect.y

        if button_rect.collidepoint(*pos_mouse) and button_mask.get_at(pos_in_mask):
            mouse_is_over_the_button = True
        else:
            mouse_is_over_the_button = False
        return mouse_is_over_the_button

    def change_of_state(self):
        mouse_in_target = self.mouse_is_over_the_button()
        # do once
        if mouse_in_target and game.click_mouse:
            self.trig_0 = True
            if not self.trig_1:
                self.trig_1 = True
                self.p_trig = True
            pass
        else:
            self.trig_0 = False
            self.trig_1 = False
            pass

        if self.p_trig:
            # self.counter_trig += 1
            # print("Clik: ", self.counter_trig)
            if self.current_state >= 1:
                self.current_state = 0
            else:
                self.current_state += 1
            self.p_trig = False

    def reset(self, arg):
        # do once
        if arg:
            self.res_trig_0 = True
            if not self.res_trig_1:
                self.res_trig_1 = True
                self.res_p_trig = True
            pass
        else:
            self.res_trig_0 = False
            self.res_trig_1 = False
            pass

        if self.res_p_trig:
            # self.res_counter_trig += 1
            # print("reset: ", self.res_counter_trig)
            self.current_state = 0
            self.res_p_trig = False

    def set_state(self):
        self.current_state = 1


class Background:
    def __init__(self) -> None:
        # backgroud position x, position y is const == 0
        self.backgroud_pos_x = []
        # backgroud preload
        self.background_surface = pygame.image.load(
            GameParam.Background.IMAGE).convert_alpha()
        # Green color
        self.base_background = GameParam.Background.BASE_BACKGROUND
        # first and second surface poz
        self.backgroud_pos_x.append(0)
        self.backgroud_pos_x.append(0)
        # end
        pass

    def background_on_off(self, background_yes: bool = True, speed: int = 1):
        '''
        # Background display #
        * background_yes (bool) - turns the background on and off
        * speed (int) - background speed
        '''
        self.background_yes = background_yes
        self.speed = speed

        if background_yes:
            # threading.Thread(target = moving_background, args=[]).start()
            self.moving_background(self.speed)
        else:
            game.window.fill(self.base_background)

    def moving_background(self, speed):

        # if there is a pause, the fast tempo is zero
        if game.delta_time == 0 or game.pause or game.gameover:
            speed = 0
        game.window.blit(self.background_surface, (self.backgroud_pos_x[0], 0))
        # window.width == 800 - backgroud_poz_x[0]
        self.backgroud_pos_x[1] = self.background_surface.get_width() + \
            self.backgroud_pos_x[0]
        game.window.blit(self.background_surface, (self.backgroud_pos_x[1], 0))
        # first surface moving
        self.backgroud_pos_x[0] -= 1 * speed
        if self.backgroud_pos_x[1] == 0:
            self.backgroud_pos_x[0] = 0


class MusicBackground:
    '''
    class responsible for:
    # Music Background
    '''

    def __init__(self, sound_path) -> None:
        '''
        sound_path (str) - location of the .ogg file
        '''
        self.trig_on_0, self.trig_on_1, self.p_trig_on, self.counter_trig_on = None, None, None, 0
        self.trig_off_0, self.trig_off_1, self.p_trig_off, self.counter_trig_off = None, None, None, 0

        self.sound_path = sound_path
        # Initialize Mixer in the program
        mixer.init()
        # background music
        pygame.mixer.music.load(self.sound_path)

    def do_play_music(self, play):
        if play:
            # The -1 argument makes the background music forever loop when it reaches the end of the sound file
            pygame.mixer.music.play(-1)
            # print("music.play")
        else:
            pygame.mixer.music.stop()
            # print("music.stop")

    def do_music(self, var):
        self.var = var
        # do once
        # -----------------------------
        if self.var:
            self.trig_on_0 = True
            if not self.trig_on_1:
                self.trig_on_1 = True
                self.p_trig_on = True
            pass
        else:
            self.trig_on_0 = False
            self.trig_on_1 = False
            pass

        if self.p_trig_on:
            self.counter_trig_on += 1
            # print("do_music(on):  ", self.counter_trig_on)
            self.do_play_music(True)
            self.p_trig_on = False
        # -----------------------------
        if not self.var:
            self.trig_off_0 = True
            if not self.trig_off_1:
                self.trig_off_1 = True
                self.p_trig_off = True
            pass
        else:
            self.trig_off_0 = False
            self.trig_off_1 = False
            pass

        if self.p_trig_off:
            # self.counter_trig_off += 1
            # print("do_music(off): ", self.counter_trig_off)
            self.do_play_music(False)
            self.p_trig_off = False
        # -----------------------------
        pass


class GameTexts:
    def __init__(self, game_texts_image, scale, co_ordinates) -> None:
        self.game_texts_image = game_texts_image
        self.scale = scale
        self.co_ordinates = co_ordinates
        self.text_surface = self.game_texts_image_preload()
        self.text_center_pos = self.game_texts_center_pos_preload()
        pass

    def game_texts_image_preload(self):
        text_surface = pygame.image.load(self.game_texts_image).convert_alpha()
        text_surface = pygame.transform.scale(
            text_surface, (text_surface.get_width()*self.scale, text_surface.get_height()*self.scale))
        return text_surface

    def game_texts_center_pos_preload(self):
        # window center position (middle)
        window_center_pos = game.window.get_width()/2, game.window.get_height()/2

        text_surface_rect = self.text_surface.get_rect(
            center=(self.co_ordinates))
        text_center_pos = window_center_pos[0] + \
            text_surface_rect.x, window_center_pos[1]+text_surface_rect.y
        return text_center_pos

    def show_text(self, show):
        if show:
            game.window.blit(self.text_surface, self.text_center_pos)
        pass


class Obstacle:
    '''
    Obstacle - is responsible for generating the obstacle
    '''

    def __init__(self, gap: int, wall_speed: int, obstacle_image: str, corridor_range: int = 150, wall_width: int = 60, corridor_size: int = 250) -> None:
        '''
        * gap (int) -               sets the spacing between another walls  \n
        * wall_speed (int) -        sets speed of moving walls              \n
        * obstacle_image (str) -    location of the .png file               \n
        Optional:
        * corridor_range (int) -    isthmus between the pipes               \n
        * wall_width (int) -        pipes thickness                         \n
        * corridor_size (int)                                               \n
        '''
        # PARAMETERS #

        self.corridor_range = corridor_range    # isthmus between the pipes
        self.wall_width = wall_width
        self.corridor_size = corridor_size

        ##############

        self.walls = []  # adding new wall (up and down site)
        self.gap = gap
        self.wall_speed_x = wall_speed
        self.wall_speed_y = 0  # because no move in y directions
        self.obstacle_image_down = pygame.image.load(
            obstacle_image).convert_alpha()
        self.obstacle_image_up = pygame.transform.flip(
            self.obstacle_image_down, False, True)

    def once_generate_walls(self) -> None:

        position = randint(self.corridor_range,
                           game.windows_size[1] - self.corridor_range)
        # upper wall - x position, y position, x size, y size
        self.walls.append(pygame.Rect(
            game.windows_size[0], 0, self.wall_width, position - self.corridor_size/2))
        # lower wall - x position, y position, x size, y size
        self.walls.append(pygame.Rect(
            game.windows_size[0], position + self.corridor_size/2, self.wall_width, game.windows_size[1] - position))

    def generate_walls_with_gap(self) -> None:
        # if amount of obstacles is 0 then
        if len(self.walls) == 0:
            self.once_generate_walls()

        if len(self.walls) > 0:
            if self.walls[len(self.walls)-1].left < game.window.get_width() - self.gap:
                threading.Thread(
                    target=self.once_generate_walls(), args=[]).start()

    def draws_obstacles(self) -> None:
        for wall in self.walls:
            # draw pipes shadows
            # pygame.draw.rect(window, const.color_of_walls, wall)
            if wall[1] == 0:
                game.window.blit(self.obstacle_image_up,
                                 (wall[0], wall[3] - 800))
            else:
                game.window.blit(self.obstacle_image_down, (wall[0], wall[1]))

    def remove_walls(self) -> None:
        for wall in self.walls:
            if wall.right < 0:
                self.walls.remove(wall)

    def move_walls(self) -> None:
        for wall in self.walls:
            if not(game.delta_time == 0):
                wall.move_ip(-self.wall_speed_x /
                             game.delta_time, self.wall_speed_y)

    def remove_all_items(self) -> None:
        self.walls.clear()


class Player(Picture):
    '''
    # Create new player
    For correct operation, the methods must be called in a specific order:
        * move_character
        * drawn_character
        * event_character
    '''

    def __init__(self, sprite_location, how_many_columns, how_many_rows, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_columns (int) - how many columns in sprite
        * how_many_rows (int) - how many rows in sprite
        * alfa_color (str) - base color
        * scaling (float or int) - scaling by this value
        '''

        # Preload image from sprite
        self.how_many_images = how_many_columns * how_many_rows

        #  uses the class Picture to load photos
        self.player_list_of_images = Picture(
            sprite_location, how_many_columns, how_many_rows, alfa_color, scaling).list_of_images

        # Creating a dictionary containing angle as key and list of rotated images as value
        self.max_rotate_plus = 35
        self.max_rotate_minus = -45
        self.angle_step = 2

        self.dictionary_of_player_images_and_angles = self.dictionary_with_rotated_Surfaces(
            self.player_list_of_images, self.how_many_images, self.max_rotate_plus, self.max_rotate_minus, self.angle_step)

        # For game handling
        self.player_is_dead = False
        # uses the trig class to  save the state
        self.player_wait_for_game_over = Trig()
        self.outside_player_is_kill_and_game_over = False

        # Parameters of movement
        self.pos_y = 0
        self.pos_x = 0 + 100
        self.speed_y = 0
        self.desired_rotation = 0
        self.resulting_rotation = 0
        self.jump_activated = False
        self.max_up = -10  # how high the figure will jump

        # self.bottom_edge - is bottom limit of movement for player
        self.bottom_edge = game.window.get_height() - 30  # 770
        self.gravity_constant = 1/2

        # For animation
        self.current_player_frame = 0
        self.speed_of_animation = 10 / 5  # 5 is demanded speed
        self.program_counter_player_frame_animation = 0

        self.player_image = None

        # For sounds effect
        self.flip = False
        self.once_death_sound_event = Trig()  # uses the trig class to get a score

        # Player stats #
        self.player_score = GameParam.Player.STARTING_SCORE
        self.player_score_trigg = Trig()  # uses the trig class to get a pulse

    def move_character(self, key_state) -> None:
        '''
        * key_state (bool) - output of the button
        '''
        # for sounds effect
        self.flip = key_state

        if not(game.delta_time == 0):
            self.set_counter = 8
            self.x_enhancement = 2.85 * 2
            self.y_enhancement = 1.05 * 2
            self.power_jump = 1.5

            if self.jump_activated or key_state:  # if key SPACE is trig
                if not self.jump_activated:
                    self.speed_y = 0
                self.jump_activated = True

                if self.speed_y > self.max_up:
                    self.speed_y -= 1 * self.power_jump
                else:
                    self.jump_activated = False
                self.desired_rotation = 1

            elif not self.jump_activated:       # not self.jump:
                if self.speed_y < 12:
                    self.speed_y += 1 * self.gravity_constant
                self.desired_rotation = -1

            #   setting a limit on the move
            if self.pos_y <= self.bottom_edge or self.pos_y <= self.bottom_edge:   # < 770
                self.pos_y += self.speed_y
                if self.bottom_edge < self.pos_y:  # if > 770 then setup for 769
                    self.pos_y = self.bottom_edge - 1

    def drawn_character(self, rotate: bool = True):
        '''
        # Draws a character and rotate character\n
        * rotate (bool) - turns rooting features on and off, if True player rotate
        '''

        self.current_player_frame = self.player_frame_animation()

        angle = self.player_rotate(self.desired_rotation, self.power_jump *
                                   self.x_enhancement, self.gravity_constant*self.y_enhancement)

        simplified_angle = self.angle_formatting_plug(
            angle, self.max_rotate_minus, self.max_rotate_plus, self.angle_step)

        if rotate:
            self.player_image = self.dictionary_of_player_images_and_angles[
                simplified_angle][self.current_player_frame]

        else:
            self.player_image = self.dictionary_of_player_images_and_angles[
                0][self.current_player_frame]

        game.window.blit(self.player_image, (self.pos_x-(self.player_image.get_width()/2),
                         self.pos_y-(self.player_image.get_height()/2)))

    def event_character(self, God_mode: bool = False, box_collision: bool = False, mute_wing_sound: bool = False, mute_death_sound: bool = False, mute_score_sound: bool = False) -> None:
        '''
        # Event handling \n

        Optional:
        * God_mode (bool) - if True player is immortal  \n

        * box_collision (bool) - if True draws the collision box
        * mute_wing_sound (bool) - if True sound of the wings is muted
        * mute_death_sound (bool) - if True sound of the player death is muted
        * mute_score_sound (bool) - if True sound of the score sound is muted
        * color_box (str)
        '''

        # Player_game_over #
        self.player_game_over(God_mode)

        # Box collision #
        self.player_draw_box_collision(box_collision)

        # Counting points #
        self.player_count_score(mute_score_sound)

        game.show_character_score(self.player_score)

        # Death sound #
        self.player_sound_event([r'music\no_tak_srednio.ogg', r'music\uuu.ogg'],
                                self.once_death_sound_event.return_trig(self.player_is_dead), mute_death_sound, 1)

        # Wings sound #
        self.player_sound_event(
            [r'music\audio_wing.ogg'], self.flip, mute_wing_sound, 0)

    def player_collision(self, surface_player: pygame.Surface) -> bool:
        '''
        # Player collision return <bool>
        * surface_player (Surface)
        '''

        self.rect_character = pygame.Rect(self.pos_x - surface_player.get_width()/2,
                                          self.pos_y - surface_player.get_height()/2,
                                          surface_player.get_width(), surface_player.get_height())

        mask_character = pygame.mask.from_surface(surface_player)

        self.player_is_dead = False
        for wall in obstacle.walls:
            surf_wall = pygame.Surface((wall[2], wall[3])).convert_alpha()
            mask_wall = pygame.mask.from_surface(surf_wall)
            self.offset_x = int(wall[0]) - int(self.rect_character[0])
            self.offset_y = int(wall[1]) - int(self.rect_character[1])

            if mask_character.overlap(mask_wall, (self.offset_x, self.offset_y)):
                self.player_is_dead = True

        return self.player_is_dead

    def player_game_over(self, God_mode: bool) -> None:

        self.player_is_dead = self.player_collision(self.player_image)

        # it would be worth taking a look here, because sometimes the player dies and the game does not stop, to do later
        self.player_wait_for_game_over.save_the_condition(self.player_is_dead)

        if not God_mode:
            if self.player_is_dead:
                self.current_player_frame = 3
            # there #
            self.outside_player_is_kill_and_game_over = self.player_wait_for_game_over.save_the_condition(
                self.player_is_dead)
            #########
        else:
            self.outside_player_is_kill_and_game_over = False
        # there #
        if game.resume:
            self.player_wait_for_game_over.reset()
        #########
        pass

    def player_draw_box_collision(self, box_collision) -> None:
        '''
        * box_collision (bool) - if True draws the collision box 
        * color_box (str)
        '''
        if not box_collision:
            return 0

        if self.player_is_dead:
            pygame.draw.rect(game.window, Color.RED, self.rect_character, 1)
        else:  # (124,252,0) 'GREAN'
            pygame.draw.rect(game.window, Color.GREAN, self.rect_character, 1)

    def player_frame_animation(self) -> int:
        '''
        # Player frame animation
        * return returns each successive frame, creating an animation
        '''

        if not(game.delta_time == 0):

            self.program_counter_player_frame_animation += 1

            if self.program_counter_player_frame_animation >= game.delta_time/self.speed_of_animation:
                self.program_counter_player_frame_animation = 0

                if not self.player_is_dead:

                    # wing support handling
                    if self.jump_activated or self.speed_y < 0:
                        self.current_player_frame += 1
                    else:
                        self.current_player_frame = 0

                    if self.current_player_frame >= self.how_many_images - 1:
                        self.current_player_frame = 0
                else:
                    # last frame is dead player
                    self.current_player_frame = self.how_many_images - 1

        return self.current_player_frame

    def player_count_score(self, mute_score_sound: bool = False) -> None:
        '''
        # Count score and get score sound   \n
        Optional: \n
            * mute_score_sound (boll)              - if True is muted

        '''
        if len(obstacle.walls):
            if self.player_score_trigg.return_trig(obstacle.walls[0].left < self.pos_x and obstacle.walls[0].left > 0):
                self.player_score += 1
                # Score sound #
                self.player_sound_event(
                    [r'music\audio_point.ogg'], True, mute_score_sound)

    def player_reset_score(self):
        self.player_score = 0

    def player_death_sound_event(self, trigger: bool, mute: bool = False) -> None:

        if not mute:
            if trigger:
                print("UUU")
                sound_list_tag = [
                    r'music\no_tak_srednio.ogg', r'music\uuu.ogg']
                effect = pygame.mixer.Sound(sound_list_tag[1])
                effect.play()

    def player_sound_event(self, list_of_ogg: List[str], trigger: bool, mute: bool = False, which_sound: int = 0) -> None:
        '''
        # The method allows you to play the sound from the *.ogg list \n

            * list_of_ogg (list<str>)  -  <str> as the path to the *.ogg file
            * trigger (boll)           -  an event that allows you to generate sound \n
            Optional: \n
            * mute (boll)              - if True is muted
            * which_sound (int)        - select a sound from the list

        '''
        # To do (put it in a better place)  #
        if not (game.pause or game.gameover):
            #####################################
            if not mute:
                if trigger:
                    effect = pygame.mixer.Sound(list_of_ogg[which_sound])
                    effect.play()

    def player_rotate(self, direction, rising_enhancement, fall_enhancement) -> int:
        '''
        # This method is responsible for player rotation \n
        * direction ( int )
            * if 1 then player rising flies up
            * if -1 then player rising flies down
        * rising_enhancement (int or float)
        * fall_enhancement (int or float)
        '''

        if (direction > 0 and game.delta_time):
            if (self.resulting_rotation <= self.max_rotate_plus):
                self.resulting_rotation += 1 * rising_enhancement
        elif (direction < 0 and game.delta_time):
            if (self.resulting_rotation >= self.max_rotate_minus):
                self.resulting_rotation -= 1 * fall_enhancement

        return int(self.resulting_rotation)

    @staticmethod
    def dictionary_with_rotated_Surfaces(list_of_Surfaces: List[pygame.Surface], how_many_images: int, max_rotate_plus: int, max_rotate_minus: int, angle_step: int) -> Dict[int, List[pygame.Surface]]:
        '''
            # Return dict < angle : list of Surface rotated by angle> \n

            * list_of_Surfaces list <pygame.Surface>
            * how_many_images (int)
            * angle (int) - assigned angle
            * max_rotate_plus  (abs(int))
            * max_rotate_minus (int)
            * angle_step (int)
        '''

        player_angle_and_state = dict()

        for angle in range(max_rotate_minus, max_rotate_plus + angle_step, angle_step):

            list = []

            for current_frame in range(how_many_images):
                list.append(pygame.transform.rotate(
                    list_of_Surfaces[current_frame], angle))
                list[current_frame].set_alpha(None)

            player_angle_and_state[angle] = list

        return player_angle_and_state

    @staticmethod
    def angle_formatting_plug(angle: int, max_rotate_minus: int, max_rotate_plus, angle_step: int) -> int:
        for num in range(max_rotate_minus, max_rotate_plus + angle_step, angle_step):

            if angle < max_rotate_minus:
                return max_rotate_minus
            if num >= max_rotate_plus:
                return max_rotate_plus
            if angle >= num - 1 and angle < num + 1:
                return num


class Score:

    def __init__(self, window_size: tuple[int, int],  text_height: int = -325, scale: int = 1) -> None:
        '''
        * window_Surface (tuple) - window

        Optional:
        * text_height (int) - starting from the middle, where "-" goes up and "+" goes down
        * scale (int) - scale 

        '''
        self.window_size = window_size

        # TO DO FONTS #
        self.list_of_numbers_images = self.get_font_for_the_result(2)

        self.game_score_center_pos = self.game_score_center_pos_preload(
            text_height)

    def get_font_for_the_result(self, font: int, scale: int = 1) -> List[pygame.Surface]:
        '''
        what font for the result
        * font (int):
        * 1 font..  White
        * 2 font..  Own 1
        * 3 font..  Own 2
        '''

        match font:
            case 1:
                return self.preload_game_score_image(scale)
            case 2:
                return Picture.init_from_dataclass(GameParam.Fonts_EXPANDED.FIRST_Digits).list_of_images
            case 3:
                return Picture(GameParam.Fonts.Digits.SECOND_IMAGE, 10, 1, '', 0.65).list_of_images
            case _:
                raise ValueError("Bad choice for the font")

    def preload_game_score_image(self, scale: int) -> List[pygame.Surface]:
        '''
        Very basic white letters
        '''

        digit_images = ['imgs\digits\\0.png', 'imgs\digits\\1.png', 'imgs\digits\\2.png', 'imgs\digits\\3.png', 'imgs\digits\\4.png',
                        'imgs\digits\\5.png', 'imgs\digits\\6.png', 'imgs\digits\\7.png', 'imgs\digits\\8.png', 'imgs\digits\\9.png']

        list_images = list()

        for image in digit_images:
            # .convert_alpha()) # is not needed
            list_images.append(pygame.image.load(image))

        for idx, scaled_image in enumerate(list_images):
            list_images[idx] = pygame.transform.scale(
                scaled_image, (scaled_image.get_width() * scale, scaled_image.get_height() * scale))

        return list_images

    def show_score(self, score: int):

        if score < 10:
            game.window.blit(
                self.list_of_numbers_images[score], (self.game_score_center_pos[0]))

        elif score >= 10 and score < 100:
            # [x][]
            game.window.blit(
                self.list_of_numbers_images[score // 10], (self.game_score_center_pos[2]))
            # [][x]
            game.window.blit(
                self.list_of_numbers_images[score % 10], (self.game_score_center_pos[1]))

        elif score >= 100 and score < 1000:
            # [x][][]
            game.window.blit(
                self.list_of_numbers_images[score // 100], (self.game_score_center_pos[5]))
            # [][x][]
            game.window.blit(
                self.list_of_numbers_images[score // 10 % 10], (self.game_score_center_pos[4]))
            # [][][x]
            game.window.blit(
                self.list_of_numbers_images[score % 10], (self.game_score_center_pos[3]))

    def game_score_center_pos_preload(self, text_height: int) -> List[tuple]:

        game_score_center_pos = list()

        # window center position
        window_center_pos = (self.window_size[0] /
                             2), (self.window_size[1] / 2)

        # Pause center position on window -> game_texts_center_pos[0]
        digit_0_pause_surface_rect = self.list_of_numbers_images[0].get_rect(
            center=(0, text_height))

        # game_score_center_pos[0]
        digit0_center_pos = window_center_pos[0] + \
            digit_0_pause_surface_rect.x, window_center_pos[1] + \
            digit_0_pause_surface_rect.y
        game_score_center_pos.append(digit0_center_pos)

        # Pause center position on window -> game_texts_center_pos[00]
        digit_0_pause_surface_rect = self.list_of_numbers_images[0].get_rect(
            center=(50, text_height))
        digit_1_pause_surface_rect = self.list_of_numbers_images[0].get_rect(
            center=(-50, text_height))
        # game_score_center_pos[1]
        digit0_center_pos = window_center_pos[0] + \
            digit_0_pause_surface_rect.x, window_center_pos[1] + \
            digit_0_pause_surface_rect.y
        game_score_center_pos.append(digit0_center_pos)
        # game_score_center_pos[2]
        digit00_center_pos = window_center_pos[0] + \
            digit_1_pause_surface_rect.x, window_center_pos[1] + \
            digit_1_pause_surface_rect.y
        game_score_center_pos.append(digit00_center_pos)

        # Pause center position on window -> game_texts_center_pos[000]
        digit_0_pause_surface_rect = self.list_of_numbers_images[0].get_rect(
            center=(100, text_height))
        digit_1_pause_surface_rect = self.list_of_numbers_images[0].get_rect(
            center=(0, text_height))
        digit_2_pause_surface_rect = self.list_of_numbers_images[0].get_rect(
            center=(-100, text_height))
        # game_score_center_pos[3]
        digit0_center_pos = window_center_pos[0] + \
            digit_0_pause_surface_rect.x, window_center_pos[1] + \
            digit_0_pause_surface_rect.y
        game_score_center_pos.append(digit0_center_pos)
        # game_score_center_pos[4]
        digit00_center_pos = window_center_pos[0] + \
            digit_1_pause_surface_rect.x, window_center_pos[1] + \
            digit_1_pause_surface_rect.y
        game_score_center_pos.append(digit00_center_pos)
        # game_score_center_pos[5]
        digit000_center_pos = window_center_pos[0] + \
            digit_2_pause_surface_rect.x, window_center_pos[1] + \
            digit_2_pause_surface_rect.y
        game_score_center_pos.append(digit000_center_pos)

        return game_score_center_pos


###############################################################
####################    PRELOAD GAME    #######################
###############################################################

# Preload game
game = Game()
game.name_of_log(GameParam.NAME_OF_LOG)

# Preload obstacle
obstacle = Obstacle(
    GameParam.Obstacle.GAP,
    GameParam.Obstacle.WALL_SPEED,
    GameParam.Obstacle.OBSTACLE_IMAGE)

# Defining the space key
key_space = KeyFromKeyboard('SPACE')

# Preload player
player = Player(
    GameParam.Player.IMAGE,
    GameParam.Player.IMAGE_COLUMNS,
    GameParam.Player.IMAGE_ROWS,
    GameParam.Player.IMAGE_ALFA_COLOR,
    GameParam.Player.IMAGE_SCALING)

# Preload background layer 0
background_layer_0 = Background()

# Preload button mute
button_mute = Button(
    GameParam.Button.IMAGE,
    GameParam.Button.IMAGE_COLUMNS,
    GameParam.Button.IMAGE_ROWS,
    GameParam.Button.IMAGE_ALFA_COLOR,
    GameParam.Button.IMAGE_SCALING)

# Preload background music
song_background = MusicBackground(
    GameParam.MusicBackground.SOUND_PATH)

# -----------game texts-----------------------------------
image_game_texts = ['imgs\Pause.png', 'imgs\Game_over.png', 'imgs\\resume.png']
# Preload game text pause
pause_text = GameTexts(image_game_texts[0], 2/3, (40, -125))

# Preload game text gameover
gameover_text = GameTexts(image_game_texts[1], 2/3, (25, -200))

# Preload game text resume
resume_text = GameTexts(image_game_texts[2], 2/3, (25, 45))
# --------------------------------------------------------

# Defining the pause key
key_pause = KeyFromKeyboard('P')

# Defining the reset key
key_resume = KeyFromKeyboard('R')


# ------------- FOR TEST -------------------

# Defining the gameover key
key_test_gameover = KeyFromKeyboard('G')
# Deactivate the button
key_test_gameover.deactivate_key()

# ------------------------------------------


while game.running:

    # -------------- Class variable ---------------------------

    ### CLOCK ###
    game.clock_support()

    ### EVENTS ###
    game.event_handling()

    ### LOGIC ###
    game.logic_gameover_pause_resume()

    obstacle.generate_walls_with_gap()

    # draws the background layer
    background_layer_0.background_on_off()

    # draw obstacle
    obstacle.draws_obstacles()

    # move walls
    obstacle.move_walls()

    # remove the obstacles after crossing the edge of the screen
    obstacle.remove_walls()

    # FPS statistics
    game.show_character_statistics('FPS')

    # draw button mute
    button_mute.draw_button()
    game.logic_buton_mute()

    # show text pause
    pause_text.show_text(game.pause)

    # show text gameover
    gameover_text.show_text(game.gameover)
    # show text resume
    resume_text.show_text(game.gameover)

    # do not change the calls sequence of player's methods
    player.move_character(key_space.key_return_trig())
    player.drawn_character()
    player.event_character(False, False)

    # ---------------------------------------------------------

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
