import threading
import pygame
from pygame import mixer  # for import music
import const


class Game():
    def __init__(self) -> None:
        # initialize pygame
        pygame.init()
        # initialize game clock
        self.clock = pygame.time.Clock()
        # Set up the drawing window
        self.window = pygame.display.set_mode(const.windows_size)

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
        if game.pause:
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
            # button operation
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click_mouse = True
            else:
                self.click_mouse = False
            pass

    def logic_gameover_pause_resume(self):
        # pause key
        self.pause = key_pause.return_curent_state()

        # test gameover key ! to delete !
        self.gameover = key_test_gameover.return_curent_state()

        # resume key
        self.resume = key_resume.return_trig()

        if self.gameover:
            key_pause.reset()
            button_mute.reset(True)
        else:
            button_mute.reset(False)

        if self.gameover and self.resume:
            self.gameover = False
            key_test_gameover.curent_state = 0
            key_test_gameover.reset()
            button_mute.set_state()

    def logic_buton_mute(self):
        # draw button mute
        button_mute.draw_button()
        button_mute.change_of_state()
        if button_mute.current_state == 1:
            song_background.do_music(True)
        else:
            song_background.do_music(False)

# class Pulse():
#     def __init__(self) -> None:
#         self.trig_on_0, self.trig_on_1, self.p_trig_on, self.counter_trig_on = None, None, None, 0
#         self.pulse = None
#     pass

#     def return_trig(self):
#         key = pygame.key.get_pressed()
#         self.pulse = False
#         # do once
#         # -----------------------------
#         if key[self.key]:
#             self.trig_on_0 = True
#             if not self.trig_on_1:
#                 self.trig_on_1 = True
#                 self.p_trig_on = True
#             pass
#         else:
#             self.trig_on_0 = False
#             self.trig_on_1 = False
#             pass

#         if self.p_trig_on:
#             # self.counter_trig_on += 1
#             # print("button_action_", self.designation_key,
#             #   "_(on ): ", self.counter_trig_on)

#             self.pulse = True

#             self.p_trig_on = False
#         # -----------------------------
#         return self.pulse


class Button():
    # Creates a button
    def __init__(self, sprite_location, how_many_images, alfa_color, scaling) -> None:
        self.sprite_location = sprite_location
        self.how_many_images = how_many_images
        self.alfa_color = alfa_color
        self.scaling = scaling

        self.trig_0, self.trig_1, self.p_trig, self.counter_trig = None, None, None, 0
        self.res_trig_0, self.res_trig_1, self.res_p_trig, self.res_counter_trig = None, None, None, 0

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
            game.window.fill(self.color_background)

    def moving_background(self, speed):
        global delta_time
        # if there is a pause, the fast tempo is zero
        if game.delta_time == 0 or game.pause:
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


class MusicBackground():
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


class KeyFromKeyboard():
    def __init__(self, key, how_many_state) -> None:
        self.key = key
        self.curent_state = 0
        self.how_many_state = how_many_state

        if self.key.upper() == 'P':
            self.designation_key = self.key.upper()
            self.key = pygame.K_p
        elif self.key.upper() == 'R':
            self.designation_key = self.key.upper()
            self.key = pygame.K_r
        elif self.key.upper() == 'G':
            self.designation_key = self.key.upper()
            self.key = pygame.K_g
        else:
            pass

        self.trig_on_0, self.trig_on_1, self.p_trig_on, self.counter_trig_on = None, None, None, 0
        self.trig_off_0, self.trig_off_1, self.p_trig_off, self.counter_trig_off = None, None, None, 0
        self.pulse = None
        pass

    def return_curent_state(self):
        self.return_trig()
        if self.curent_state > self.how_many_state - 1:
            self.curent_state = 0
        # print(bool(self.curent_state))
        return bool(self.curent_state)

    def return_trig(self):
        key = pygame.key.get_pressed()
        self.pulse = False
        # do once
        # -----------------------------
        if key[self.key]:
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
            # self.counter_trig_on += 1
            # print("button_action_", self.designation_key,
            #   "_(on ): ", self.counter_trig_on)

            self.pulse = True
            self.curent_state += 1

            self.p_trig_on = False
        # -----------------------------
        if not key[self.key]:
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
            # print("button_action_", self.designation_key,"_(off): ", self.counter_trig_off)
            ###
            self.p_trig_off = False
        # -----------------------------
        return self.pulse

    def reset(self):
        self.curent_state = 0


class GameTexts():
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


# Preload game
game = Game()
game.name_of_log("My Gmae")


# Preload background layer 0
background_layer_0 = Background()

# Preload button mute
button_mute = Button('imgs\\mute_sprite.png', 2, 'BLACK', 1)

# Preload background music
song_background = MusicBackground('music\\bensound-summer_ogg_music.ogg')

# -----------game texts-----------------------------------
image_game_texts = [
    'imgs\Pause.png', 'imgs\Game_over.png', 'imgs\\resume.png']
# Preload game text pause
pause_text = GameTexts(image_game_texts[0], 2/3, (40, -125))

# Preload game text gameover
gameover_text = GameTexts(image_game_texts[1], 2/3, (25, -200))

# Preload game text resume
resume_text = GameTexts(image_game_texts[2], 2/3, (25, 45))
# --------------------------------------------------------

# defining the pause button
key_pause = KeyFromKeyboard('P', 2)

# defining the reset button
key_resume = KeyFromKeyboard('R', 2)

# defining the reset button
key_test_gameover = KeyFromKeyboard('G', 2)


while game.running:

    ### CLOCK ###
    game.clock_support()

    ### EVENTS ###

    # death sound effectw
    # player_death_sound_event(True)

    # event handling
    game.event_handling()

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

    # drawn_button()

    # count_points(True, True)
    # show_score()

    # key_pause(game_over_fun_active)
    # game_over(True)
    # threading.Thread(target=game_over, args=[True]).start()
    # key_resume()

    # -------------- Class variable ---------------------------
    # logic
    game.logic_gameover_pause_resume()

    # draws the background layer
    background_layer_0.background_on_off(True, 1)

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
