import pygame


class Trig:
    '''
    # class Trig
    Is used to store and return the current state of an object,
    includes methods to trigger it
    * return_curent_state
    * return_trig
    * save_the_condition
    * reset
    '''

    def __init__(self, how_many_state: int = 2) -> None:
        '''
        * how many state have key (int)  "default 2 states"
        '''

        self.__trig_on, self.__p_trig_on, self.__counter_trig_on = None, None, 0
        self.__trig_off, self.__p_trig_off, self.__counter_trig_off = None, None, 0
        self.__pulse = None
        self.curent_state = 0
        self.how_many_state = how_many_state

        self.__condition = None

    def return_curent_state(self, event: bool) -> bool:
        if self.return_trig(event):
            self.curent_state += 1

        if self.curent_state > self.how_many_state - 1:
            self.curent_state = 0

        return bool(self.curent_state)

    def return_trig(self, event: bool) -> bool:
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

    def save_the_condition(self, event: bool) -> bool:
        if event:
            self.__condition = True
        return self.__condition

    def reset(self):
        self.curent_state = 0
        self.__condition = False


class KeyFromKeyboard(Trig):
    '''
    Is responsible for the button handle
    '''

    def __init__(self, key) -> None:
        '''
        * key - which key ( str_symbolic_name e.g. 'P', 'R', 'G', 'SPACE', 'ENTER', 'LEFT', 'RIGHT', 'UP', 'DOWN')
        '''
        super().__init__()
        # or
        # Trig.__init__(self)
        self.key = key
        self.key_name = key
        self.how_many_state = 2
        self.key_deactivate = False
        self.counter = 0

        if self.key.upper() == 'P':
            self.key = pygame.K_p

        elif self.key.upper() == 'R':
            self.key = pygame.K_r

        elif self.key.upper() == 'G':
            self.key = pygame.K_g

        elif self.key.upper() == 'SPACE':
            self.key = pygame.K_SPACE

        elif self.key.upper() == 'ENTER':
            self.key = pygame.K_RETURN

        elif self.key.upper() == 'ESC':
            self.key = pygame.K_ESCAPE

        elif self.key.upper() == 'LEFT':
            self.key = pygame.K_LEFT

        elif self.key.upper() == 'RIGHT':
            self.key = pygame.K_RIGHT

        elif self.key.upper() == 'UP':
            self.key = pygame.K_UP

        elif self.key.upper() == 'DOWN':
            self.key = pygame.K_DOWN
        else:
            pass
        pass

    def deactivate_key(self):
        '''
        # ! Deactivate the button !
        '''
        self.key_deactivate = True

    def do_event(self):
        if self.key_deactivate:
            return False
        key = pygame.key.get_pressed()
        return key[self.key]

    def return_curent_state(self):
        '''
        Returns the current state of the button
        '''
        if self.key_deactivate:
            return False
        return super().return_curent_state(self.do_event())

    def key_return_trig(self):
        '''
        Returns trig (pulse) from button
        '''
        if self.key_deactivate:
            return False
        if super().return_trig(self.do_event()):
            self.counter += 1
            return True

    ############################################
    # FOR Test CLASS Trig and KeyFromKeyboard  #
    ############################################


### FOR TEST ###
def main():

    key_P = KeyFromKeyboard('P')
    key_R = KeyFromKeyboard('R')
    key_ENTER = KeyFromKeyboard('ENTER')
    key_ESC = KeyFromKeyboard('ESC')
    key_LEFT = KeyFromKeyboard('LEFT')
    key_RIGHT = KeyFromKeyboard('RIGHT')
    key_UP = KeyFromKeyboard('UP')
    key_DOWN = KeyFromKeyboard('DOWN')

    trig = Trig()

    i = 0
    state = None

    pygame.init()
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Fonts test")

    while True:
        # event handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit pygame
                pygame.quit()

        ####################
        ##   CODE HERE    ##
        ####################

        ### TEST ###
        # import pdb
        ### TEST ###
        # if trig.return_trig(key_ESC.key_return_trig()):
        ### TEST ###
        # pdb.set_trace()  # tak testuje sie kod w cmd
        ### TEST ###
        if trig.return_trig(key_ESC.key_return_trig()):
            i += 1
            print(
                f'key_{key_ESC.key_name} {key_ESC.counter}')  # {i}')  # state: Trig = {trig.curent_state} KeyFromKeyboard = {key_ESC.curent_state}')

        ####################
        ##     UNTIL      ##
        ####################

        # Update the display
        pygame.display.flip()


################
if __name__ == "__main__":
    main()
