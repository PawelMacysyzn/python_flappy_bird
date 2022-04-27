import threading
import pygame
import const  # declaration of constants

# initialize pygame
pygame.init()
# initialize game clock
clock = pygame.time.Clock()
# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)


# freezes the game
pause = False


class Buton():
    # Creates a button
    def __init__(self, sprite_location, how_many_images, alfa_color, scaling) -> None:
        self.sprite_location = sprite_location
        self.how_many_images = how_many_images
        self.alfa_color = alfa_color
        self.scaling = scaling

        self.images_from_sprite = []

        # self.preload_images_from_sprite()
        pass

    def preload_images_from_sprite(self):

        for which_frame in range(self.how_many_images):
            self.images_from_sprite.append(self.do_sprite(
                self.sprite_location, self.how_many_images, which_frame, self.alfa_color, self.scaling))

    def do_sprite(image, how_many_images, which_frame, alfa_color, scaling):
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

    def drawn_buton(self):
        # global mouse_is_over_the_button, music_button_plays
        # global music_trig, music_trig_before, p_trig_music

        # ---------------------------------------------------------------------
        # pos_mouse = pygame.mouse.get_pos()
        self.buton_mute_pos = (100, 750)

        if music_button_plays:
            buton_mute_surf = buton_mute_image[0]
        else:
            buton_mute_surf = buton_mute_image[1]

        buton_mute_rect = buton_mute_surf.get_rect(
            center=(self.buton_mute_pos))
        window.blit(buton_mute_surf, buton_mute_rect)


class Background():
    def __init__(self) -> None:
        # backgroud position x, position y is const == 0
        self.self.backgroud_pos_x = []
        # backgroud preload
        self.self.background_surface = pygame.image.load(
            'imgs\\background_full_width.png').convert_alpha()
        # Green color
        self.color_background = (124, 252, 0)
        # first and second surface poz
        self.backgroud_pos_x.append(0)
        self.backgroud_pos_x.append(0)
        # end
        pass

    def background_on_off(self, background_yes):
        if background_yes:
            # threading.Thread(target = moving_background, args=[]).start()
            self.moving_background()
        else:
            window.fill(self.color_background)

    def moving_background(self):
        window.blit(self.self.background_surface, (self.backgroud_pos_x[0], 0))
        # window.width == 800 - backgroud_poz_x[0]
        self.backgroud_pos_x[1] = self.background_surface.get_width() + \
            self.backgroud_pos_x[0]
        window.blit(self.background_surface, (self.backgroud_pos_x[1], 0))
        # first surface moving
        if not(delta_time == 0):
            self.backgroud_pos_x[0] -= 1
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



# Preload 





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
            click_button = True
        else:
            click_button = False

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
    # show_character_statistics('FPS')

    # drawn_buton()

    # count_points(True, True)
    # show_score()

    # key_pause(game_over_fun_active)
    # game_over(True)
    # threading.Thread(target=game_over, args=[True]).start()
    # key_resume()

    # -------------- Class variable ---------------------------

    # second_buton_mute.drawn_buton()

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
