import threading
import pygame
from pygame import mixer  # for import music
import const  # declaration of constants

# initialize pygame
pygame.init()
# initialize game clock
clock = pygame.time.Clock()
# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)


# freezes the game
pause = False
# clik button state
click_mouse = None


class Button():
    # Creates a button
    def __init__(self, sprite_location, how_many_images, alfa_color, scaling) -> None:
        self.sprite_location = sprite_location
        self.how_many_images = how_many_images
        self.alfa_color = alfa_color
        self.scaling = scaling

        self.trig_0, self.trig_1, self.p_trig, self.counter_trig = None, None, None, 0

        self.current_state = 1
        self.images_from_sprite = []
        self.preload_images_from_sprite()

    def preload_images_from_sprite(self):
        for which_frame in range(self.how_many_images):
            self.images_from_sprite.append(self.do_sprite(
                self.sprite_location, self.how_many_images, which_frame, self.alfa_color, self.scaling))

    def do_sprite(self, image, how_many_images, which_frame, alfa_color, scaling):
        spride_sheet_image = pygame.image.load(image).convert_alpha()

        if alfa_color.upper() == 'WHITE':
            alfa_color = (255, 255, 255)
        elif alfa_color.upper() == 'BLACK':
            alfa_color = (0, 0, 0)
        elif alfa_color.upper() == 'RED':
            alfa_color = (255, 0, 0)

        width = spride_sheet_image.get_width()/how_many_images
        height = spride_sheet_image.get_height()

        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(spride_sheet_image, (0, 0),
                   ((which_frame*width), 0, width, height))
        image = pygame.transform.scale(image, (width*scaling, height*scaling))
        image.set_colorkey(alfa_color)
        return image

    def draw_button(self):

        self.button_surf = self.images_from_sprite[self.current_state]

        # button position
        pos_x = window.get_width() - self.button_surf.get_width()
        pos_y = window.get_height() - self.button_surf.get_height()
        self.pos_button = pos_x, pos_y
        # draw button
        window.blit(self.button_surf, self.pos_button)

    def mouse_is_over_the_button(self):
        buton_rect = self.button_surf.get_rect(topleft=(self.pos_button))
        buton_mask = pygame.mask.from_surface(self.button_surf)

        # pos_mouse = pygame.mouse.get_pos(center=(buton_mute_rect))
        pos_mouse = pygame.mouse.get_pos()

        pos_in_mask = pos_mouse[0] - buton_rect.x, pos_mouse[1] - buton_rect.y

        if buton_rect.collidepoint(*pos_mouse) and buton_mask.get_at(pos_in_mask):
            mouse_is_over_the_button = True
        else:
            mouse_is_over_the_button = False
        return mouse_is_over_the_button

    def change_of_state(self):
        mouse_in_target = self.mouse_is_over_the_button()
        # do once
        if mouse_in_target and click_mouse:
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


class Background():
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
            window.fill(self.color_background)

    def moving_background(self, speed):
        global delta_time, pause
        # if there is a pause, the fast tempo is zero
        if delta_time == 0 or pause:
            speed = 0
        window.blit(self.background_surface, (self.backgroud_pos_x[0], 0))
        # window.width == 800 - backgroud_poz_x[0]
        self.backgroud_pos_x[1] = self.background_surface.get_width() + \
            self.backgroud_pos_x[0]
        window.blit(self.background_surface, (self.backgroud_pos_x[1], 0))
        # first surface moving
        self.backgroud_pos_x[0] -= 1 * speed
        if self.backgroud_pos_x[1] == 0:
            self.backgroud_pos_x[0] = 0


def clock_support():
    global delta_time, pause
    # const.framerate = 60
    # dt show how many milliseconds have passed since the previous call
    # the program will never run at more than const.framerate frames per second
    if pause:
        delta_time = 0
    else:
        delta_time = clock.tick(const.framerate)
    # print(delta_time, " ms")
    # print("{:.1f} FPS".format(clock.get_fps()))
    pass


def show_character_statistics(what):
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
            str("{:.1f}".format(clock.get_fps())), 1, color_font)

        position_x -= next_width
        window.blit(
            label_7, (const.windows_size[0] - position_x - 15, position_y))
        window.blit(
            label_8, (const.windows_size[0] - position_x + label_7.get_width() - 10, position_y))

        if not what == 2:
            label_1 = font.render("X:", 1, color_font)
            label_2 = font.render(str(pos_x), 1, color_font)
            label_3 = font.render("Y:", 1, color_font)
            label_4 = font.render(str("{:.1f}".format(pos_y)), 1, color_font)
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
            window.blit(
                label_1, (const.windows_size[0] - position_x, position_y))
            window.blit(
                label_2, (const.windows_size[0] - position_x + next_width_1, position_y))
            # next stat Y
            position_x -= next_width
            window.blit(
                label_3, (const.windows_size[0] - position_x, position_y))
            window.blit(
                label_4, (const.windows_size[0] - position_x + next_width_1, position_y))

            # NEXT LINE
            position_y += 50

            # next line R
            position_x += next_width
            window.blit(
                label_5, (const.windows_size[0] - position_x, position_y))
            window.blit(
                label_6, (const.windows_size[0] - position_x + next_width_1, position_y))

            # NEXT LINE
            position_y += 50

            # next stat V
            # next stat speed_y
            window.blit(
                label_9, (const.windows_size[0] - position_x, position_y))
            window.blit(
                label_10, (const.windows_size[0] - position_x + next_width_1 + 75, position_y))

            # NEXT LINE
            position_y += 50

            # next stat counter_jump
            position_x += next_width
            window.blit(
                label_11, (const.windows_size[0] - position_x + 100, position_y))
            window.blit(
                label_12, (const.windows_size[0] - position_x + next_width_1 + 225, position_y))


class BackgroundMusic():
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
            print("music.play")
        else:
            pygame.mixer.music.stop()
            print("music.stop")

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


# Preload background layer 0
background_layer_0 = Background()

# Preload button mute
button_mute = Button('imgs\\mute_sprite.png', 2, 'BLACK', 1)

# Preload background music
song_background = BackgroundMusic('music\\bensound-summer_ogg_music.ogg')

running = True
while running:

    ### CLOCK ###
    clock_support()

    ### EVENTS ###

    # death sound effectw
    # player_death_sound_event(True)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handling button "X"
            running = False
        # button operation
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_mouse = True
        else:
            click_mouse = False

    ### MATHS ###

    # Generate walls
    # generate_walls_with_gap(600)

    # Remove walls after they reach end of screen
    # remove_walls()

    # # Move Walls
    # move_walls()

    ### DRAWING ####

    # Fill the background

    # Draw walls
    # threading.Thread(target=draws_obstacles, args=[
    #                  walls_image[0], walls_image[1]]).start()

    # move_character()
    # drawn_character()

    # drawn_buton()

    # count_points(True, True)
    # show_score()

    # key_pause(game_over_fun_active)
    # game_over(True)
    # threading.Thread(target=game_over, args=[True]).start()
    # key_resume()

    # -------------- Class variable ---------------------------
    pause = False

    # draws the background layer
    background_layer_0.background_on_off(True, 1)

    # FPS statistics
    show_character_statistics('FPS')

    # draw buton mute
    button_mute.draw_button()
    button_mute.change_of_state()
    if button_mute.current_state == 1:
        song_background.do_music(True)
    else:
        song_background.do_music(False)

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
