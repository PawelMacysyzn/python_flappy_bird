from pickle import FALSE
import threading
import pygame
from pygame import mixer  # for import music
from random import randint  # for generate walls
import const


class Trig:
    def __init__(self) -> None:
        self.__trig_on, self.__p_trig_on, self.__counter_trig_on = None, None, 0
        self.__trig_off, self.__p_trig_off, self.__counter_trig_off = None, None, 0
        self.__pulse = None
        self.__curent_state = 0
        pass

    def return_curent_state(self, event, how_many_state):
        if self.return_trig(event):
            self.__curent_state += 1

        if self.__curent_state > how_many_state - 1:
            self.__curent_state = 0
        return bool(self.__curent_state)

    def return_trig(self, event):
        # ----- for test ------
        show_statistics = False
        # ---------It IS ONLY PERFORMED ONCE------------
        self.__pulse = False
        # -----------pulse trig on----------------
        if event:
            # self.__trig_on_0 = True
            if not self.__trig_on:
                self.__trig_on = True
                self.__p_trig_on = True
            pass
        else:
            # self.__trig_on_0 = False
            self.__trig_on = False
            pass

        if self.__p_trig_on:
            if show_statistics:
                self.__counter_trig_on += 1
                print("return_trig_(on ): ", self.__counter_trig_on)

            self.__pulse = True

            self.__p_trig_on = False
        # -----------pulse trig off----------------
        if not event:
            # self.__trig_off_0 = True
            if not self.__trig_off:
                self.__trig_off = True
                self.__p_trig_off = True
            pass
        else:
            # self.__trig_off_0 = False
            self.__trig_off = False
            pass

        if self.__p_trig_off:
            if show_statistics:
                self.__counter_trig_off += 1
                print("return_trig_(off): ", self.__counter_trig_off)
            ### negative trig ###
            self.__p_trig_off = False
        # -----------------------------
        return self.__pulse

    def reset(self):
        self.__curent_state = 0


class Game:
    '''
     # Creates a game # 
     * initialize pygame
     * initialize game clock
     * configures the game window
    '''

    def __init__(self, windows_size_x=800, windows_size_y=800) -> None:
        '''
        * windows_size_x (int) - game screen width (default value: 800)
        * windows_size_y (int) - game screen height (default value: 800)

        '''

        # initialize pygame
        pygame.init()
        # initialize game clock
        self.clock = pygame.time.Clock()

        self.windows_size = (windows_size_x, windows_size_y)  # width X height
        # configures the game window
        self.window = pygame.display.set_mode(self.windows_size)

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
        pass

    def name_of_log(self, name_str):
        # to do, show session and user in bar
        pygame.display.set_caption(name_str.upper())

    def clock_support(self):
        # const.framerate = 60
        # dt show how many milliseconds have passed since the previous call
        # the program will never run at more than const.framerate frames per second
        # if pause or game over is pressed freeze the game
        if game.pause or game.gameover:
            self.delta_time = 0
        else:
            self.delta_time = self.clock.tick(const.framerate)
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
                label_7, (const.windows_size[0] - position_x - 15, position_y))
            self.window.blit(
                label_8, (const.windows_size[0] - position_x + label_7.get_width() - 10, position_y))

            if not what == 2:
                label_1 = font.render("X:", 1, color_font)
                label_2 = font.render(str(pos_x), 1, color_font)
                label_3 = font.render("Y:", 1, color_font)
                label_4 = font.render(
                    str("{:.1f}".format(pos_y)), 1, color_font)
                label_5 = font.render("R:", 1, color_font)
                label_6 = font.render(
                    str("{:.1f}".format(const.rotate)), 1, color_font)
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
                    label_1, (const.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_2, (const.windows_size[0] - position_x + next_width_1, position_y))
                # next stat Y
                position_x -= next_width
                self.window.blit(
                    label_3, (const.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_4, (const.windows_size[0] - position_x + next_width_1, position_y))

                # NEXT LINE
                position_y += 50

                # next line R
                position_x += next_width
                self.window.blit(
                    label_5, (const.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_6, (const.windows_size[0] - position_x + next_width_1, position_y))

                # NEXT LINE
                position_y += 50

                # next stat V
                # next stat speed_y
                self.window.blit(
                    label_9, (const.windows_size[0] - position_x, position_y))
                self.window.blit(
                    label_10, (const.windows_size[0] - position_x + next_width_1 + 75, position_y))

                # NEXT LINE
                position_y += 50

                # next stat counter_jump
                position_x += next_width
                self.window.blit(
                    label_11, (const.windows_size[0] - position_x + 100, position_y))
                self.window.blit(
                    label_12, (const.windows_size[0] - position_x + next_width_1 + 225, position_y))

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

        # test gameover key ! to delete !
        if not self.pause:
            self.gameover = key_test_gameover.return_curent_state()

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


class Picture:
    '''
    # Conver sprite to list<Surface>
    '''

    def __init__(self, sprite_location, how_many_images, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_images (int) - how many images in sprite
        * alfa_color (str) - base color
        * scaling (float or int) - scaling by this value
        '''
        self.sprite_location = sprite_location
        self.how_many_images = how_many_images
        self.alfa_color = alfa_color
        self.scaling = scaling

        self.current_state = 1
        self.list_of_images = self.preload_images_from_sprite()

    def preload_images_from_sprite(self) -> list:
        '''
        return list of Surface
        '''
        return [self.do_sprite(self.sprite_location, self.how_many_images, which_frame, self.alfa_color, self.scaling) for which_frame in range(self.how_many_images)]

    @staticmethod
    def do_sprite(image, how_many_images, which_frame, alfa_color, scaling) -> pygame.Surface:
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

        width = spride_sheet_image.get_width()/how_many_images
        height = spride_sheet_image.get_height()

        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(spride_sheet_image, (0, 0),
                   ((which_frame*width), 0, width, height))
        image = pygame.transform.scale(image, (width*scaling, height*scaling))
        if set_colorkey:
            image.set_colorkey(alfa_color)
        return image


class Button(Picture):
    """
    # Creates a button
    """

    def __init__(self, sprite_location, how_many_images, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_images (int) - how many images in sprite
        * alfa_color (str) - base color
        * scaling (float or int) - scaling by this value
        '''

        self.trig_0, self.trig_1, self.p_trig, self.counter_trig = None, None, None, 0
        self.res_trig_0, self.res_trig_1, self.res_p_trig, self.res_counter_trig = None, None, None, 0

        self.current_state = 1
        self.how_many_images = how_many_images
        self.images = Picture(
            sprite_location, how_many_images, alfa_color, scaling)


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
            'imgs\\background_full_width.png').convert_alpha()
        # Green color
        self.color_background = (124, 252, 0)
        # first and second surface poz
        self.backgroud_pos_x.append(0)
        self.backgroud_pos_x.append(0)
        # end
        pass

    def background_on_off(self, background_yes, speed):
        self.background_yes = background_yes
        self.speed = speed

        if background_yes:
            # threading.Thread(target = moving_background, args=[]).start()
            self.moving_background(self.speed)
        else:
            game.window.fill(self.color_background)

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
    def __init__(self, sound_path) -> None:
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


class KeyFromKeyboard(Trig):
    '''
    Is responsible for the button handle
    '''

    def __init__(self, key, how_many_state) -> None:
        '''
        * key - which key ( str_symbolic_name )
        * how_many_state - how many states does the button have ( int )
        '''
        super().__init__()
        self.key = key
        self.how_many_state = how_many_state

        if self.key.upper() == 'P':
            # self.designation_key = self.key.upper()
            self.key = pygame.K_p
        elif self.key.upper() == 'R':
            # self.designation_key = self.key.upper()
            self.key = pygame.K_r
        elif self.key.upper() == 'G':
            # self.designation_key = self.key.upper()
            self.key = pygame.K_g
        elif self.key.upper() == 'SPACE':
            # self.designation_key = self.key.upper()
            self.key = pygame.K_SPACE
        else:
            pass
        pass

    def do_event(self):
        key = pygame.key.get_pressed()
        return key[self.key]

    def return_curent_state(self):
        return super().return_curent_state(self.do_event(), self.how_many_state)

    def key_return_trig(self):
        return super().return_trig(self.do_event())


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

    def __init__(self, gap, wall_speed, obstacle_image) -> None:
        '''
        gap - sets the spacing between the walls \n
        wall_speed - sets speed of moving walls \n
        obstacle_image - location of the .png file \n

        '''
        self.walls = []  # adding new wall (up and down site)
        self.gap = gap
        self.wall_speed_x = wall_speed
        self.wall_speed_y = 0  # because no move in y directions
        self.obstacle_image_down = pygame.image.load(
            obstacle_image).convert_alpha()
        self.obstacle_image_up = pygame.transform.flip(
            self.obstacle_image_down, False, True)

    def once_generate_walls(self):
        position = randint(const.corridor_range[0], const.corridor_range[1])
        # upper wall - x position, y position, x size, y size
        self.walls.append(pygame.Rect(
            const.windows_size[0], 0, const.wall_width, position - const.corridor_size/2))
        # lower wall - x position, y position, x size, y size
        self.walls.append(pygame.Rect(
            const.windows_size[0], position + const.corridor_size/2, const.wall_width, const.windows_size[1] - position))

    def generate_walls_with_gap(self):
        # if amount of obstacles is 0 then
        if len(self.walls) == 0:
            self.once_generate_walls()

        if len(self.walls) > 0:
            if self.walls[len(self.walls)-1].left < game.window.get_width() - self.gap:
                threading.Thread(
                    target=self.once_generate_walls(), args=[]).start()

    def draws_obstacles(self):
        for wall in self.walls:
            # draw pipes shadows
            # pygame.draw.rect(window, const.color_of_walls, wall)
            if wall[1] == 0:
                game.window.blit(self.obstacle_image_up,
                                 (wall[0], wall[3] - 800))
            else:
                game.window.blit(self.obstacle_image_down, (wall[0], wall[1]))

    def remove_walls(self):
        for wall in self.walls:
            if wall.right < 0:
                self.walls.remove(wall)

    def move_walls(self):
        for wall in self.walls:
            if not(game.delta_time == 0):
                wall.move_ip(-self.wall_speed_x /
                             game.delta_time, self.wall_speed_y)

    def remove_all_items(self):
        self.walls.clear()
        pass


class Player(Picture):
    '''
    Create new player
    '''

    def __init__(self, sprite_location, how_many_images, alfa_color, scaling) -> None:
        '''
        * sprite_location (str) - path of sprite
        * how_many_images (int) - how many images in sprite
        * alfa_color (str) - base color
        * scaling (float or int) - scaling by this value
        '''
        # parameters of movement
        self.pos_y = 0
        self.pos_x = 0 + 100
        self.speed_y = 0
        self.desired_rotation = 0
        self.resulting_rotation = 0
        self.jump_activated = False
        self.max_up = -11

        # self.bottom_edge - is bottom limit of movement for player
        self.bottom_edge = game.window.get_height() - 30  # 770
        self.gravity_constant = 1/2

        # preload image from sprite
        self.how_many_images = how_many_images
        self.images = Picture(
            sprite_location, how_many_images, alfa_color, scaling)

        # for animation
        self.current_player_frame = 0
        self.speed_of_animation = 10 / 5  # 5 is demanded speed
        self.program_counter_player_frame_animation = 0
        self.is_the_player_dead = False

    def move_character(self, key_state):
        '''
        * key_state (bool) - output of the button
        '''
        if not(game.delta_time == 0):
            self.set_counter = 8
            self.x = 2.85 * 2
            self.y = 1.05 * 2
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

    def drawn_character_(self):
        '''
        * draws a character
        * rotate character
        '''

        current_player_frame = self.player_frame_animation()

        angle = self.player_rotate(
            self.desired_rotation, self.power_jump*self.x, self.gravity_constant*self.y)

        if True:
            rotate_character = pygame.transform.rotate(
                self.images.list_of_images[current_player_frame], angle)
            alfa_colo_red = (255, 0, 0)
            rotate_character.set_colorkey(alfa_colo_red)
        else:
            rotate_character = self.images.list_of_images[current_player_frame]

        game.window.blit(rotate_character, (self.pos_x-(rotate_character.get_width()/2),
                         self.pos_y-(rotate_character.get_height()/2)))

    def drawn_character(self):

        self.player_frame_animation()

        if False:
            rotate_character = pygame.transform.rotate(
                self.character_frames[current_player_frame], const.rotate)
        else:
            rotate_character = self.character_frames[self.current_player_frame]

        # drwan character
        game.window.blit(rotate_character, (self.pos_x-(rotate_character.get_width()/2),
                                            self.pos_y-(rotate_character.get_height()/2)))

        # collision
        rect_character = pygame.Rect(self.pos_x-rotate_character.get_width()/2,
                                     self.pos_y - rotate_character.get_height()/2,
                                     rotate_character.get_width(), rotate_character.get_height())
        mask_character = pygame.mask.from_surface(rotate_character)

        # if there is no collision
        kill_player = False
        color = (0, 255, 0)

        for wall in obstacle.walls:
            surf_wall = pygame.Surface((wall[2], wall[3])).convert_alpha()
            mask_wall = pygame.mask.from_surface(surf_wall)
            offset_x = wall[0] - rect_character[0]
            offset_y = wall[1] - rect_character[1]

            if mask_character.overlap(mask_wall, (offset_x, offset_y)):
                # color for Box collision
                color1 = (255, 0, 0)
                kill_player = True

        # Box for collision
        pygame.draw.rect(game.window, color1, rect_character, 1)

    def player_frame_animation(self):
        '''

        '''

        if not(game.delta_time == 0):
            self.program_counter_player_frame_animation += 1
            if self.program_counter_player_frame_animation >= game.delta_time/self.speed_of_animation:
                self.program_counter_player_frame_animation = 0

                if not self.is_the_player_dead:

                    # wing support handling
                    if self.jump_activated:
                        self.current_player_frame += 1
                    else:
                        self.current_player_frame = 0

                    if self.current_player_frame >= self.how_many_images - 1:
                        self.current_player_frame = 0
                else:
                    # last frame is dead player
                    self.current_player_frame = 3
        return self.current_player_frame

    def player_death_sound_event(no_mute):
        if no_mute:
            global play_loop_kill_player_sound, kill_player

            if play_loop_kill_player_sound and kill_player:
                sound_list_tag = [
                    'music\\no_tak_srednio.ogg', 'music\\uuu.ogg']

                effect = pygame.mixer.Sound(sound_list_tag[1])
                effect.play()
                play_loop_kill_player_sound = False
            # refresh the sound of death
            if not play_loop_kill_player_sound and not kill_player:
                play_loop_kill_player_sound = True
        else:
            pass

    def player_wing_sound_event(self, no_mute):
        # global i
        if no_mute:
            if True:
                sound_list_tag = ['music\\audio_wing.ogg']
                effect = pygame.mixer.Sound(sound_list_tag[0])
                effect.play()
                # i+=1
                # print("wing_sound: ",i)
        else:
            pass

    def player_rotate(self, direction, rising_enhancement, fall_enhancement) -> int:
        '''
        # This method is responsible for player rotation 
        * direction ( int )\n
            * if 1 then player rising flies up
            * if -1 then player rising flies down
        * rising_enhancement (int or float)
        * fall_enhancement (int or float)
        '''

        max_rotate_plus = 25
        max_rotate_minus = -45

        if (direction > 0 and game.delta_time):
            if (self.resulting_rotation <= max_rotate_plus):
                self.resulting_rotation += 1 * rising_enhancement
        elif (direction < 0 and game.delta_time):
            if (self.resulting_rotation >= max_rotate_minus):
                self.resulting_rotation -= 1 * fall_enhancement

        return int(self.resulting_rotation)


##########################################################################################
# Preload game
game = Game()
game.name_of_log("My Gmae")

# Preload obstacle
obstacle = Obstacle(400, 100, r'imgs\pipe-green.png')

# defining the reset key
key_space = KeyFromKeyboard('SPACE', 2)

# Preload player
player = Player(r'imgs\flappy_sprite.png', 4, 'FALSE', 0.25)
# player = Player(r'imgs\flappy.png', 1, 'RED', 0.25)


# Preload background layer 0
background_layer_0 = Background()

# Preload button mute
button_mute = Button('imgs\\mute_sprite.png', 2, 'BLACK', 1)

# Preload background music
song_background = MusicBackground('music\\bensound-summer_ogg_music.ogg')

# -----------game texts-----------------------------------
image_game_texts = ['imgs\Pause.png', 'imgs\Game_over.png', 'imgs\\resume.png']
# Preload game text pause
pause_text = GameTexts(image_game_texts[0], 2/3, (40, -125))

# Preload game text gameover
gameover_text = GameTexts(image_game_texts[1], 2/3, (25, -200))

# Preload game text resume
resume_text = GameTexts(image_game_texts[2], 2/3, (25, 45))
# --------------------------------------------------------

# defining the pause key
key_pause = KeyFromKeyboard('P', 2)

# defining the reset key
key_resume = KeyFromKeyboard('R', 2)


# ----------- TEST ------------------------

# defining the gameover key
key_test_gameover = KeyFromKeyboard('G', 2)

# # defining rhe test key for Trig class
# key_test_for_Trig_class = Trig()

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
    background_layer_0.background_on_off(True, 1)

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

    ### TEST ###

    player.move_character(key_space.key_return_trig())
    player.drawn_character_()

    # print('x: {}, y: {}, speed: {}, {}'.format(
    #     player.pos_x, player.pos_y, player.speed_y, player.jump))

    # ---------------------------------------------------------

    # make screenshot after 0.5 sec
    # screenshot_fun(0.5)
    # Update the display
    pygame.display.flip()
    # how many times the program has been run
    # program_counter += 1

    # to delete
    # pygame.time.delay(1)


# Quit pygame
pygame.quit()
