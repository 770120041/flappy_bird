import pygame

"""
    Birds only needs to rotate, its X position is fixed,
    while its Y position will drop, if it drops out of the windows, then it is deemed as dead
"""


class Bird(pygame.sprite.Sprite):
    X_POS = 150
    MAX_ANGLE = 15

    def __init__(self, board_height, board_width):
        super(Bird, self).__init__()

        self.game_board_height = board_height
        self.game_board_width = board_width

        # benchmark
        self.ori_bird_image = pygame.image.load("./resources/images/bird.png")

        # rotated bird
        self.rotated_bird = pygame.image.load("./resources/images/bird.png")

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.rotated_bird.get_rect()
        self.bird_width = self.rotated_bird.get_width()
        self.bird_height = self.rotated_bird.get_height()

        # the x and y pos of the bird
        self.x = self.y = 0
        self.reset_bird()
        self.jump_speed = 3
        self.down_speed = 0.2

        # the rotation status of the bird
        self.angle = 0
        self.angle_speed = 0.3

        # set up jumping
        self.is_jumping = False

    def reset_bird(self):
        self.angle = 0
        self.is_jumping = False
        self.x = self.X_POS
        self.y = (self.game_board_height - self.ori_bird_image.get_height())/2

    def jump(self):
        self.is_jumping = True

    def is_dead(self):
        if self.y >= self.game_board_height:
            return True
        return False

    # cal bird pos according to the angle
    def cal_bird_pos(self):
        self.rotated_bird = pygame.transform.rotate(self.ori_bird_image,self.angle)
        delta_width = (self.rotated_bird.get_rect().width - self.ori_bird_image.get_rect().width) / 2
        delta_height = (self.rotated_bird.get_rect().width - self.ori_bird_image.get_rect().height) / 2
        self.rect.left, self.rect.top = self.x - delta_width, self.y - delta_height


    # refresh the bird to initial pos

    def update(self, time_passed):
        if self.angle > -self.MAX_ANGLE:
            self.angle = max(-self.MAX_ANGLE, self.angle - self.angle_speed * time_passed)
            return
        if self.is_jumping:
            if self.angle < self.MAX_ANGLE:
                self.angle = min(time_passed * self.angle_speed, self.MAX_ANGLE)
            self.y = max(0, self.y - time_passed * self.jump_speed)
            self.is_jumping = False
        else:
            self.y += self.down_speed * time_passed

    # return the necessary image and pos for display the bird
    def get_bird_img(self):
        return self.rotated_bird, self.rect


