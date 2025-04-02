import pygame as p
import random
from config import WIDTH, HEIGHT, TILE_SIZE, GRASS, STONE, OAK



world = [[0 for _ in range(HEIGHT // TILE_SIZE)] for _ in range(WIDTH // TILE_SIZE)]

def generate_world():
    for x in range(WIDTH // TILE_SIZE):
        for y in range(HEIGHT // TILE_SIZE):
            
            rand = random.randint(0, 100)

            if rand < 2:
                world[x][y] = 2  # STONE
            elif rand < 5:
                world[x][y] = 1  # OAK
            else:
                world[x][y] = 0  # GRASS

def draw_world(screen):
    for x in range(WIDTH // TILE_SIZE):
        for y in range(HEIGHT // TILE_SIZE):
            pos = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

         
            if world[x][y] == 0:
                p.draw.rect(screen, GRASS, pos)
            elif world[x][y] == 1:
                p.draw.rect(screen, OAK, pos)
            elif world[x][y] == 2:
                p.draw.rect(screen, STONE, pos)



