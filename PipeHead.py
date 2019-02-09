import pygame


class PipeHead(pygame.sprite.Sprite):
    def __init__(self):
        super(PipeHead, self).__init__()
        self.head_image = pygame.image.load("./resources/pipe_head.png")

        self.rect = self.head_image.get_head()

        self.width = self.head_image.get_width()
        self.height = self.head_image.get_height()
