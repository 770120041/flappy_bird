import pygame
import bird
import pipe



class FlappyBird():
    WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
    BACKGROUND_MUSIC = {
        "moonlight":'./resources/audios/moonlight.wav',
        "pigechang": './resources/audios/pigechang.mp3',
        "soundofdestiny": './resources/audios/soundofdestiny.mp3',
    }

    def __init__(self):
        pygame.init()
        self.cur_bg_music = "moonlight"
        # set up display surface
        self.__title = "flappy_birds"
        self.__size = self.width, self.height = self.WINDOW_WIDTH, self.WINDOW_HEIGHT
        self.__display_surf = pygame.display.set_mode(self.__size, 0, 32)
        pygame.display.set_caption(self.__title)

        self.load_resources()

        # the state of the game
        # either "NEWGAME" "RUNNING", "PAUSE", "DEAD" and  "END"
        self.game_state = "NEWGAME"

        self.Bird = bird.Bird(self.height, self.width)
        self.Pipes = []
        self.__score = 0
        self.max_score = 0
        self.clock = pygame.time.Clock()

    def load_bg_music(self, name="moonlight"):
        # play back ground music
        pygame.mixer.music.load(self.BACKGROUND_MUSIC[name])
        # use loop = -1 to set the music play infinitely
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(12)

    def load_resources(self):
        # load resources
        self.font = pygame.font.Font(None, 24)

        # load image
        # back_ground image is actually a piece of blue block, so we need to mix the white background
        self.background_img = pygame.image.load("./resources/images/background.png")
        self.gameover_img = pygame.image.load("./resources/images/gameover.png")

        # load music
        self.jump_sound = pygame.mixer.Sound("./resources/audios/jump.wav")
        self.jump_sound.set_volume(3)

    # used to init a new game
    def reset_game(self):
        self.game_state = "RUNNING"
        self.max_score = max(self.__score, self.max_score)

        self.__score = 0
        # create a bird
        self.Bird.reset_bird()
        self.Pipes = []
        self.load_bg_music(self.cur_bg_music)

    def on_pause(self):
        pygame.mixer.music.pause()
        paused = True
        while paused:
            self.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state = "END"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                    elif event.key == pygame.K_r:
                        paused = False
                        self.game_state = "NEWGAME"

        pygame.mixer.music.unpause()

    def on_clean_up(self):
        pygame.quit()

    # do calculation
    def on_loop(self):
        if self.game_state != "RUNNING":
            return

        # how many milliseconds have passed since last call
        time_passed = self.clock.tick()

        # generate a pipe every 3s
        if time_passed//1000 % 3 == 0:
            self.Pipes.append(pipe.Pipe(self.WINDOW_HEIGHT, self.WINDOW_WIDTH))

        for i, Pipe in enumerate(self.Pipes):
            Pipe.update(time_passed)
            if self.Bird.rect.left > Pipe.x + Pipe.pipe_head_width and not Pipe.bird_passed:
                self.__score += Pipe.passed()
            if Pipe.x + Pipe.pipe_head_width < 0:
                self.Pipes.pop(i)
            # if pygame.sprite.spritecollide(self.Bird, Pipe, False, None):
            #     if bird.rect.left < Pipe.x + (Pipe.pipe_head_width + Pipe.pipe_body_width) / 2:
            #         self.game_state = "DEAD"

        # update bird
        self.Bird.update(time_passed)
        self.Bird.cal_bird_pos()
        if self.Bird.is_dead():
            self.game_state = "DEAD"

    # do rendering
    def on_render(self):

        # render background
        self.__display_surf.fill(0)
        for x in range(self.width//self.background_img.get_width()+1):
            for y in range(self.height//self.background_img.get_height()+1):
                self.__display_surf.blit(self.background_img, (x*self.background_img.get_width(),y*self.background_img.get_height()))



        self.__display_surf.blit(*(self.Bird.get_bird_img()))

        # display score
        score_text= self.font.render('Score: ' + str(self.__score), True, (0, 0, 0))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = [10, 10]
        self.__display_surf.blit(score_text, score_text_rect)

        # display score
        max_score_text = self.font.render('Max Score: ' + str(self.__score), True, (0, 0, 0))
        max_score_rect = score_text.get_rect()
        max_score_rect.topleft = [10, 30]
        self.__display_surf.blit(max_score_text, max_score_rect)


        for Pipe in self.Pipes:
            for p in Pipe.pipe_group:
                self.__display_surf.blit(p.img, p.rect)




        # if dead, show dead image
        if self.game_state == "DEAD":
            self.__display_surf.blit(self.gameover_img, (0, 0))

        pygame.display.update()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = "END"
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game_state == "RUNNING":
                    self.jump_sound.play()
                    self.Bird.jump()

                # refresh the game
                elif event.key == pygame.K_r:
                    self.game_state = "NEWGAME"
                    pass

                # pause the game
                elif event.key == pygame.K_p:
                    self.on_pause()

                elif event.key == pygame.K_1:
                    self.load_bg_music()

                elif event.key == pygame.K_2:
                    self.cur_bg_music = "pigechang"
                    self.load_bg_music(self.cur_bg_music)

                elif event.key == pygame.K_3:
                    self.cur_bg_music = "soundofdestiny"
                    self.load_bg_music(self.cur_bg_music)

                # elif event.key == pygame.K_o:
                #     self.game_state = "DEAD"

    def on_execute(self):
        while self.game_state != "END":
            if self.game_state == "NEWGAME":
                self.reset_game()
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_clean_up()

if __name__ == '__main__':
    game_app = FlappyBird()
    game_app.on_execute()

