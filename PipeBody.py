import pygame


class PipeBody(pygame.sprite.Sprite):
    def __init__(self):
        super(PipeBody, self).__init__()
        self.body_image = pygame.image.load("./resources/pipe_body.png")

        self.rect = self.body_image.get_rect()
        self.width = self.body_image.get_width()
        self.height = self.body_image.get_height()
