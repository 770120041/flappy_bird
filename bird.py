import pygame


class Bird(pygame.sprite.Sprite):
    X_POS = 150

    def __init__(self, board_heigth, board_width):
        super(Bird, self).__init__()

        self.game_board_height = board_heigth
        self.game_board_width = board_width

        # benchmark
        self.ori_bird_image = pygame.image.load("./resources/images/bird.png")

        # rotated bird
        self.rotated_brid = pygame.image.load("./resources/images/bird.png")

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.rotated_brid.get_rect()
        self.bird_width = self.rotated_brid.get_width()
        self.bird_height = self.rotated_brid.get_height()

        # the x and y pos of the bird
        self.x = self.y = 0
        self.reset_bird()

    def cal_bird_pos(self):
        self.rect.left, self.rect.top = self.x, self.y

    def get_bird_surf(self):
        return self.rotated_brid, self.rect

    # refresh the bird to initial pos
    def reset_bird(self):
        self.x = self.X_POS
        self.y = (self.game_board_height - self.ori_bird_image.get_height())/2
        self.cal_bird_pos()

    def update(self):


        self.cal_bird_pos()



