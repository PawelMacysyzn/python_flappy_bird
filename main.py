import pygame  # game library
import const  # declaration of constants
from random import randint
import threading  # manage threads in Operation System

# initialize pygame
pygame.init()
# initialize game clock
clock = pygame.time.Clock()
# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)

# collecting beginning set up position of character
pos_x = const.x_ch
pos_y = const.y_ch
# list containing all walls
walls = []

# to delete
var_global = 0


def name_of_log(name_str):
    pygame.display.set_caption(name_str.upper())
    # to do, show session and user in bar


def generate_walls():
    threading.Timer(const.new_wall_timer, generate_walls).start()
    position = randint(const.corridor_range[0], const.corridor_range[1])
    # upper wall - x position, y position, x size, y size
    walls.append(pygame.Rect(
        const.windows_size[0], 0, const.wall_width, position - const.corridor_size/2))
    # lower wall - x position, y position, x size, y size
    walls.append(pygame.Rect(
        const.windows_size[0], position + const.corridor_size/2, const.wall_width, const.windows_size[1] - position))


def show_character_statistics():
    font = pygame.font.SysFont('Comic Gecko', 30)
    position_x = 180
    position_y = 10
    next_width = 100
    next_width_1 = 25
    label_1 = font.render("X:", 1, (0, 0, 0))
    label_2 = font.render(str(pos_x), 1, (0, 0, 0))
    label_3 = font.render("Y:", 1, (0, 0, 0))
    label_4 = font.render(str(pos_y), 1, (0, 0, 0))
    label_5 = font.render("R:", 1, (0, 0, 0))
    label_6 = font.render(str(const.rotate), 1, (0, 0, 0))
    label_7 = font.render("V:", 1, (0, 0, 0))
    label_8 = font.render(str(var_global), 1, (0, 0, 0))

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
    window.blit(label_7, (const.windows_size[0] - position_x, position_y + 50))
    window.blit(
        label_8, (const.windows_size[0] - position_x + next_width_1, position_y + 50))


def rotate(var):
    multip = 2
    jump_ch = 5
    max_rotate = 45
    global var_global
    var_global = var
    if (var > 0):
        if (const.rotate <= max_rotate):
            const.rotate += 1 * multip * jump_ch
    else:
        if (const.rotate >= -max_rotate):
            const.rotate -= 1 * multip


def move_character():
    keys = pygame.key.get_pressed()
    multiplier = 1
    global pos_y
    if keys[pygame.K_SPACE]:
        if pos_y >= 0:
            # up
            pos_y -= 7 * multiplier
            rotate(1)
    else:
        if ((pos_y <= const.windows_size[1])):
            # down
            pos_y += 2 * multiplier
            rotate(0)


def drawn_character():

    character = pygame.image.load('imgs\\flappy.png')
    character = pygame.transform.scale(
        character, (character.get_width()*const.scale, character.get_height()*const.scale))
    character = pygame.transform.rotate(character, const.rotate)
    window.blit(character, (pos_x-(character.get_width()/2),
                pos_y-(character.get_height()/2)))

    # collision
    # rect_character = character.get_rect(center = (pos_x , pos_y ))
    rect_character = pygame.Rect(pos_x-character.get_width()/2,
                                 pos_y - character.get_height()/2,
                                 character.get_width(), character.get_height())

    color1 = (0, 255, 0)
    for wall in walls:
        if wall.colliderect(rect_character):
            color1 = (255, 0, 0)
    pygame.draw.rect(window, color1, rect_character, 1)


###---------------------------------GAMING-LOOP---------------------------------###
# Preparation functions
generate_walls()
counter = []

name_of_log("My GAmE")

running = True
while running:

    ### CLOCK ###
    dt = clock.tick(const.framerate)

    ### EVENTS ###

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handling button "X"
            running = False

    ### MATHS ###

    # Remove walls after they reach end of screen
    #walls = [wall for wall in walls if wall.right >= 0]

    for wall in walls:
        if wall.right < 0:
            walls.remove(wall)

    # Move Walls
    for wall in walls:
        wall.move_ip(-const.wall_speed * dt, 0)

    # Collision
    # for wall in walls

    ### DRAWING ####

    # Fill the background
    window.fill(const.color_background)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(window, const.color_rect, wall)

    # Draw character
    move_character()
    drawn_character()
    show_character_statistics()

    ### DISPLAY ###

    # Update the display
    pygame.display.update()

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
