import pygame  # game library
import const  # declaration of constants
from random import randint
import threading  # manage threads in Operation System
from pygame import mixer  # for import music

# initialize pygame
pygame.init()
# initialize game clock
clock = pygame.time.Clock()
# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)

# how many times the program has been run
program_counter = 0
drawn_frame = False
delta_time = 0

# ------------for player----------------------------
# list containing all frames
character_frames = []
speed_y = 0
jump_y_bool = False
counter_jump = 0
p_trig_key_space = False
# collecting beginning set up position of character
pos_x = const.x_ch
pos_y = const.y_ch
# global variable, current player frame in animation
current_player_frame = 0
# global variable, character death animation
kill_player = False
# global variable, character death sound, it allows to create the effect one at a time
play_loop_kill_player_sound = True

# ------------for walls----------------------------
# list containing all walls
walls = []
walls_image = []


# ------------for butons-----------------------------
# list containing all state of button mute
buton_mute_image = []

hit_buton_mute = False
# allows to play music only once in a game loop
play_loop_music = True
# turns music on and off
music_off_on = False
# ------------for others-----------------------------
trig_screenshot = True
i = 0

key_space_down = False
key_space_up = False
key_space_down_before = False
# ---------------------------------------------------


def play_music(play):
    # Initialize Mixer in the program
    mixer.init()
    pygame.mixer.music.load('music\\bensound-summer_ogg_music.ogg')
    if play:
        pygame.mixer.music.play(-1)


def name_of_log(name_str):
    # to do, show session and user in bar
    pygame.display.set_caption(name_str.upper())


def once_generate_walls():
    position = randint(const.corridor_range[0], const.corridor_range[1])
    # upper wall - x position, y position, x size, y size
    walls.append(pygame.Rect(
        const.windows_size[0], 0, const.wall_width, position - const.corridor_size/2))
    # lower wall - x position, y position, x size, y size
    walls.append(pygame.Rect(
        const.windows_size[0], position + const.corridor_size/2, const.wall_width, const.windows_size[1] - position))


def generate_walls_with_gap(gap):
    if len(walls) > 0:
        if walls[len(walls)-1].left < window.get_width() - gap:
            threading.Thread(target=once_generate_walls, args=[]).start()


def draws_obstacles(obstacle_image_down, obstacle_image_up):
    for wall in walls:
        # draw pipes shadows
        # pygame.draw.rect(window, const.color_of_walls, wall)
        if wall[1] == 0:
            window.blit(obstacle_image_up, (wall[0], wall[3] - 800))
        else:
            window.blit(obstacle_image_down, (wall[0], wall[1]))


def show_character_statistics():
    font = pygame.font.SysFont('Comic Gecko', 30)
    position_x = 180
    position_y = 10
    next_width = 100
    next_width_1 = 25
    label_1 = font.render("X:", 1, (0, 0, 0))
    label_2 = font.render(str(pos_x), 1, (0, 0, 0))
    label_3 = font.render("Y:", 1, (0, 0, 0))
    label_4 = font.render(str("{:.1f}".format(pos_y)), 1, (0, 0, 0))
    label_5 = font.render("R:", 1, (0, 0, 0))
    label_6 = font.render(str("{:.1f}".format(const.rotate)), 1, (0, 0, 0))
    label_7 = font.render("FPS:", 1, (0, 0, 0))
    label_8 = font.render(str("{:.1f}".format(clock.get_fps())), 1, (0, 0, 0))
    label_9 = font.render("speed_y:", 1, (0, 0, 0))
    label_10 = font.render(str("{:.1f}".format(speed_y)), 1, (0, 0, 0))
    label_11 = font.render("counter_jump:", 1, (0, 0, 0))
    label_12 = font.render(str(counter_jump), 1, (0, 0, 0))

    # next stat X
    window.blit(label_1, (const.windows_size[0] - position_x, position_y))
    window.blit(
        label_2, (const.windows_size[0] - position_x + next_width_1, position_y))
    # next stat Y
    position_x -= next_width
    window.blit(label_3, (const.windows_size[0] - position_x, position_y))
    window.blit(
        label_4, (const.windows_size[0] - position_x + next_width_1, position_y))
    # next line R
    position_x += next_width
    window.blit(label_5, (const.windows_size[0] - position_x, position_y + 50))
    window.blit(
        label_6, (const.windows_size[0] - position_x + next_width_1, position_y + 50))
    # next stat V
    position_x -= next_width
    window.blit(
        label_7, (const.windows_size[0] - position_x - 25, position_y + 50))
    window.blit(
        label_8, (const.windows_size[0] - position_x + next_width_1, position_y + 50))
    # next stat speed_y
    position_x += next_width
    window.blit(
        label_9, (const.windows_size[0] - position_x, position_y + 100))
    window.blit(
        label_10, (const.windows_size[0] - position_x + next_width_1 + 75, position_y + 100))
    # next stat counter_jump
    position_x += next_width
    window.blit(
        label_11, (const.windows_size[0] - position_x + 100, position_y + 150))
    window.blit(
        label_12, (const.windows_size[0] - position_x + next_width_1 + 225, position_y + 150))


def rotate(var, multip_1, multip_2):
    max_rotate_plus = 25
    max_rotate_minus = -45
    # leveling = 1


    if (var > 0):
        if (const.rotate <= max_rotate_plus):
            const.rotate += 1 * multip_1
    elif (var < 0):
        if (const.rotate >= max_rotate_minus):
            const.rotate -= 1 * multip_2
    else:
        const.rotate = 0
        # pass


def move_character():
    keys = pygame.key.get_pressed()
    top_edge = 25
    bottom_edge = window.get_height() - 34 # 800 - 35
    gravity_constant = 1/2
    power_jump = 1.5
    set_counter = 8
    x = 2.85 * 2
    y = 1.05 * 2
    rotation = None
    global pos_y, speed_y, jump_y_bool, counter_jump, p_trig_key_space
    global key_space_down, key_space_down_before
    # global i

    # the button is performed only once per press
    if keys[pygame.K_SPACE]:
        key_space_down = True
        if not key_space_down_before:
            # i+=1
            # print("Spacja: ",i)
            # necessary for the proper operation of the jump
            speed_y = 0
            key_space_down_before = True
            p_trig_key_space = True
    else:
        key_space_down = False
        key_space_down_before = False

    # counter to hold down the button
    if p_trig_key_space:
        counter_jump += 1
    if counter_jump > set_counter:
        counter_jump = 0
        p_trig_key_space = False

    # if K_SPACE is trig
    if p_trig_key_space:
        if speed_y > -16:
            if pos_y > top_edge:
                speed_y -= 1 * power_jump
        pos_y += speed_y
        rotation = 1
        # rotate(1, power_jump*x, gravity_constant*y)

    else:  # No kay_space
        if speed_y < 12:
            speed_y += 1 * gravity_constant
        if pos_y < bottom_edge:
            pos_y += speed_y
            rotation = -1
        else:
            rotation = 0
            # rotate(0, power_jump*x, gravity_constant*y)
        # rotate(-1, power_jump*x, gravity_constant*y)
    
    rotate(rotation, power_jump*x, gravity_constant*y)



def drawn_character():
    global kill_player
    how_many_frame = 4

    player_frame_animation(kill_player, how_many_frame, 3)

    if True:
        rotate_character = pygame.transform.rotate(
            character_frames[current_player_frame], const.rotate)
    else:
        rotate_character = character_frames[current_player_frame]

    # drwan character
    window.blit(rotate_character, (pos_x-(rotate_character.get_width()/2),
                pos_y-(rotate_character.get_height()/2)))

    # collision
    rect_character = pygame.Rect(pos_x-rotate_character.get_width()/2,
                                 pos_y - rotate_character.get_height()/2,
                                 rotate_character.get_width(), rotate_character.get_height())
    mask_character = pygame.mask.from_surface(rotate_character)

    # if there is no collision
    kill_player = False
    color1 = (0, 255, 0)

    for wall in walls:
        surf_wall = pygame.Surface((wall[2], wall[3])).convert_alpha()
        mask_wall = pygame.mask.from_surface(surf_wall)
        offset_x = wall[0] - rect_character[0]
        offset_y = wall[1] - rect_character[1]

        if mask_character.overlap(mask_wall, (offset_x, offset_y)):
            # color for Box collision
            color1 = (255, 0, 0)
            kill_player = True

    # Box for collision
    pygame.draw.rect(window, color1, rect_character, 1)


def drawn_buton(pos_mouse, music_off_on):
    buton_mute_pos = (750, 750)

    if music_off_on:
        buton_mute_surf = buton_mute_image[0]
        pass
    else:
        buton_mute_surf = buton_mute_image[1]
        pass

    buton_mute_rect = buton_mute_surf.get_rect(center=(buton_mute_pos))
    window.blit(buton_mute_surf, buton_mute_rect)
    buton_mute_mask = pygame.mask.from_surface(buton_mute_surf)
    pos_in_mask = pos_mouse[0] - \
        buton_mute_rect.x, pos_mouse[1] - buton_mute_rect.y
    if buton_mute_rect.collidepoint(*pos_mouse) and buton_mute_mask.get_at(pos_in_mask):
        return True
    else:
        return False


def do_sprite(image, how_many_frame, which_frame, scale, alfa_color):
    spride_sheet_image = pygame.image.load(image).convert_alpha()

    if alfa_color.upper() == 'WHITE':
        alfa_color = (255, 255, 255)
    elif alfa_color.upper() == 'BLACK':
        alfa_color = (0, 0, 0)
    elif alfa_color.upper() == 'RED':
        alfa_color = (255, 0, 0)

    width = spride_sheet_image.get_width()/how_many_frame
    height = spride_sheet_image.get_height()

    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(spride_sheet_image, (0, 0),
               ((which_frame*width), 0, width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(alfa_color)

    return image


def clock_support():
    global delta_time
    # const.framerate = 60
    # dt show how many milliseconds have passed since the previous call
    # the program will never run at more than const.framerate frames per second
    delta_time = clock.tick(const.framerate)
    # print(delta_time, " ms")
    # print("{:.1f} FPS".format(clock.get_fps()))
    pass


def player_frame_animation(will_player_be_killed, how_many_frame, speed):
    global program_counter, delta_time, current_player_frame

    if program_counter >= delta_time/speed:
        program_counter = 0
        if not will_player_be_killed:
            current_player_frame += 1

            if current_player_frame >= how_many_frame - 1:
                current_player_frame = 0
        else:
            # the player is dead
            current_player_frame = 3


def player_death_sound_event():
    global play_loop_kill_player_sound, kill_player

    if play_loop_kill_player_sound and kill_player:
        sound_list_tag = ['music\\no_tak_srednio.ogg', 'music\\uuu.ogg']

        effect = pygame.mixer.Sound(sound_list_tag[1])
        effect.play()
        play_loop_kill_player_sound = False
    # refresh the sound of death
    if not play_loop_kill_player_sound and not kill_player:
        play_loop_kill_player_sound = True


def remove_walls():
    for wall in walls:
        if wall.right < 0:
            walls.remove(wall)


def move_walls():
    for wall in walls:
        # pos y no move
        const.y_no_mpve = 0
        wall.move_ip(-const.wall_speed / delta_time, const.y_no_mpve)


def moving_background():
    global backgroud_poz_x, load_once, background_surface
    if True:  # problems with the smoothness of the game
        if load_once:
            # first and second surface poz
            backgroud_poz_x.append(0)
            backgroud_poz_x.append(0)
            # end
            load_once = False

    window.blit(background_surface, (backgroud_poz_x[0], 0))
    # window.width == 800 - backgroud_poz_x[0]
    backgroud_poz_x[1] = background_surface.get_width() + backgroud_poz_x[0]
    window.blit(background_surface, (backgroud_poz_x[1], 0))
    # first surface moving
    backgroud_poz_x[0] -= 1
    if backgroud_poz_x[1] == 0:
        backgroud_poz_x[0] = 0
    pass


def background_on_off(background_yes):
    if background_yes:
        threading.Thread(target=moving_background, args=[]).start()
    else:
        window.fill(const.color_background)


def image_walls_preload():
    walls_image.append(pygame.image.load(
        "imgs\pipe-green.png").convert_alpha())
    walls_image.append(pygame.transform.flip(walls_image[0], False, True))


def sprite_image_preload(sprite_list, image, how_many_frame, scale, alfa_color):
    for frame in range(how_many_frame):
        sprite_list.append(do_sprite(image,
                                     how_many_frame, frame, scale, alfa_color).convert_alpha())


def screenshot_fun(time):
    global trig_screenshot

    def screenshot():
        pygame.image.save(window, "imgs\page_presentation\screenshot.jpeg")
        print("Screenshot !")

    if trig_screenshot:
        threading.Timer(time, screenshot).start()
        trig_screenshot = False


###---------------------------------GAMING-LOOP---------------------------------###
# Preparation functions
threading.Thread(target=once_generate_walls, args=[]).start()

image_walls_preload()

background_surface = pygame.image.load(
    'imgs\\background_full_width.png').convert_alpha()

# character sprite preload
sprite_image_preload(
    character_frames, 'imgs\\flappy_sprite.png', 4, const.scale, 'RED')


# buton_mute sprite preload
sprite_image_preload(buton_mute_image, 'imgs\\mute_sprite.png', 2, 1, 'WHITE')


load_once = True
counter, backgroud_poz_x = [], []
name_of_log("My GAmE")

running = True
while running:

    ### CLOCK ###
    clock_support()

    ### EVENTS ###
    if play_loop_music:
        play_music(music_off_on)
        play_loop_music = False

    # death sound effectw
    player_death_sound_event()

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handling button "X"
            running = False
        # button operation
        if event.type == pygame.MOUSEBUTTONDOWN:
            # press button mute
            if hit_buton_mute and music_off_on:
                music_off_on = False
                play_loop_music = True
            elif hit_buton_mute and not music_off_on:
                music_off_on = True
                play_loop_music = True

    ### MATHS ###

    # Generate walls
    generate_walls_with_gap(600)

    # Remove walls after they reach end of screen
    remove_walls()

    # Move Walls
    move_walls()

    ### DRAWING ####

    # Fill the background
    background_on_off(True)

    # Draw walls
    threading.Thread(target=draws_obstacles, args=[
                     walls_image[0], walls_image[1]]).start()

    # Draw character
    # move_character()
    move_character()
    drawn_character()
    show_character_statistics()

    hit_buton_mute = drawn_buton(pygame.mouse.get_pos(), music_off_on)

    screenshot_fun(0.5)

    # Update the display
    pygame.display.flip()
    # how many times the program has been run
    program_counter += 1

    # to delete
    pygame.time.delay(1)


# Quit pygame
pygame.quit()
'''
    start = time.time()
    end = time.time()
    counter.append(end - start)
    count = 0
    for el in counter:
        count += el
    print(f"{(count/len(counter)):.9f}")
'''
