import pygame
import game_logic
import bird

class FlappyBird():
    WIDTH, HEIGHT = 640, 480


    def __init__(self):
        pygame.init()

        # set up display surface
        self.__title = "flappy_birds"
        self.__size = self.width, self.height = self.WIDTH,self.HEIGHT
        self.__display_surf = pygame.display.set_mode(self.__size, 0, 32)
        pygame.display.set_caption(self.__title)

        # load resources
        self.font = pygame.font.Font(None, 24)

        # load image
        # back_ground image is actually a piece of blue block, so we need to mix the white background
        self.background_img = pygame.image.load("./resources/images/background.png")
        self.gameover_img = pygame.image.load("./resources/images/gameover.png")

        # load music
        self.jump_sound = pygame.mixer.Sound("./resources/audios/jump.wav")
        self.jump_sound.set_volume(6)


        # a field used to initiate a new game
        self.__new_game = True

        # check if the game is still in running state
        self.is_running = True

        # check if to pause the game
        self.__pause = False

        self.Bird = None
        self.Pipes = []
        self.__score = 0
        self.max_score = 0


    # used to init a new game
    def reset_game(self):
        self.__new_game = False
        self.__score = 0
        # create a bird
        self.Bird = bird.Bird(self.height, self.width)

        # play back ground music
        pygame.mixer.music.load('./resources/audios/moonlight.wav')
        # use loop = -1 to set the music play infinitely
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(12)



    def on_pause(self):
        pygame.mixer.music.pause()
        pass

    def on_resume(self):
        pygame.mixer.music.unpause()
        pass

    def on_clean_up(self):
        pygame.quit()

    # do calculation
    def on_loop(self):
        pass

    # do rendering
    def on_render(self):
        # render background
        self.__display_surf.fill(0)
        for x in range(self.width//self.background_img.get_width()+1):
            for y in range(self.height//self.background_img.get_height()+1):
                self.__display_surf.blit(self.background_img,(x*self.background_img.get_width(),y*self.background_img.get_height()))

        # render bird
        self.__display_surf.blit( *(self.Bird.get_bird_surf()) )


        pygame.display.update()


    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

                # refresh the game
                elif event.key == pygame.K_r:
                    self.__new_game = True
                    pass

                # pause the game
                elif event.key == pygame.K_p:
                    self.__pause = not self.__pause


    def on_execute(self):
        while self.is_running:
            if self.__new_game:
                self.reset_game()
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_clean_up()




if __name__ == '__main__':
    flappy_bird = FlappyBird()
    flappy_bird.on_execute()

