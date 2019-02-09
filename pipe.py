import pygame
import pipe_body
import pipe_head
import random


# a General class managing all Pipes
class Pipe():
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width

        # places for birds to cross
        self.interval_length = 8

        self.pipe_body_image = pygame.image.load("./resources/images/pipe_body.png")
        self.pipe_head_image = pygame.image.load("./resources/images/pipe_head.png")

        self.pipe_body_height, self.pipe_body_width = self.pipe_body_image.get_height(), self.pipe_body_image.get_width()
        self.pipe_head_height, self.pipe_head_width = self.pipe_head_image.get_height(), self.pipe_head_image.get_width()
        self.max_pip_body_number = (self.board_height - 2 * self.pipe_head_height) // self.pipe_body_height

        # body number
        self.up_body_number = random.randint(0, self.max_pip_body_number - self.interval_length)
        self.down_body_number = self.max_pip_body_number - self.up_body_number - self.interval_length

        # the initial pos and spped of the pipe
        self.x = 600
        self.speed = 0.1

        self.pipe_group = None
        self.bird_passed = False
        self.construct_pipe()

    def construct_pipe(self):
        self.pipe_group = pygame.sprite.Group()
        pipe_vertical_x = self.x - (self.pipe_head_width - self.pipe_body_width) / 2

        # up pipe
        for i in range(self.up_body_number):
            up_pipe_body = pipe_body.PipeBody(self.x, i*self.pipe_body_height)
            self.pipe_group.add(up_pipe_body)
        self.pipe_group.add( pipe_head.PipeHead(pipe_vertical_x, self.up_body_number * self.pipe_body_height))

        # down pipe
        for i in range(self.down_body_number):
            down_pipe_body = pipe_body.PipeBody(self.x, self.board_height-(i+ 1)*self.pipe_body_height)
            self.pipe_group.add(down_pipe_body)
        self.pipe_group.add(pipe_head.PipeHead(pipe_vertical_x, self.board_height - self.down_body_number * self.pipe_body_height - self.pipe_head_height))


    # if not passed this pipe, then set to Pass
    # return the score for the birds
    def passed(self):
        if self.bird_passed == False:
            self.bird_passed = True
            return 1
        else:
            return 0

    def update(self, time_passed):
        self.pipe_group.update(time_passed * self.speed)


