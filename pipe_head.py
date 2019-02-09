import pygame


class PipeHead(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(PipeHead, self).__init__()
        self.img = pygame.image.load("./resources/images/pipe_head.png")

        self.rect = self.img.get_rect(topleft = (x,y))

        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def update(self, move_distance):
        self.rect.left -= move_distance