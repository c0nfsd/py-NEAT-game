#from turtle import window_width
import pygame
import neat
import os
import time
import random

#setting window size
WIN_WIDTH = 600
WIN_HEIGHT = 800

#loading images from image folder
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("asset-images", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(
    os.path.join("asset-images", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("asset-images", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("asset-images", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("asset-images", "base.png")))
BG_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("asset-images", "bg.png")))


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x #represent starting position of bird
        self.y = y  #represent starting position of bird
        self.tilt = 0 #when bird is not moving it look flat
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1


# while True:
#     bird.move()
