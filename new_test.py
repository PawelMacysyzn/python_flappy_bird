import pygame


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
        self.images_from_sprite = self.preload_images_from_sprite()

    def preload_images_from_sprite(self) -> list:
        '''
        return list of Surface
        '''
        return [self.do_sprite(self.sprite_location, self.how_many_images, which_frame, self.alfa_color, self.scaling) for which_frame in range(self.how_many_images)]

    @staticmethod
    def do_sprite(image, how_many_images, which_frame, alfa_color, scaling) -> pygame.Surface:
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


pygame.init()
windows_size = (800, 800)
window = pygame.display.set_mode(windows_size)

pikture_player = Picture(r'imgs\flappy_sprite.png', 4, 'RED', 0.25)

print(pikture_player.images_from_sprite)

stop_game = True
while(stop_game):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handling button "X"
            stop_game = False


pygame.quit()
