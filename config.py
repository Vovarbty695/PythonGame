import pygame as p

#GENERAL

WIDTH = 800
HEIGHT = 600

BACKGROUND = (231, 221, 255)
TILE_SIZE = 20
screen = p.display.set_mode((WIDTH, HEIGHT))
icon = p.image.load("images/icons/icon.png")
#PLAYER

player_pos = p.Vector2(300, 300)
speed = 1

#WORLD

GRASS = (0, 255, 30)
STONE = (160, 160, 160)
OAK = (141, 111, 100)