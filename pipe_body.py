import pygame


class PipeBody(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(PipeBody, self).__init__()
        self.img = pygame.image.load("./resources/images/pipe_body.png")

        self.rect = self.img.get_rect(topleft=(x, y))
        self.width = self.img.get_width()
        self.height = self.img.get_height()


    def body_height(self):
        return self.height

    def update(self, move_distance):
        self.rect.left -= move_distance