import pygame as p
from config import speed, player_pos, screen, TILE_SIZE

def player():
    keys = p.key.get_pressed()

    if keys[p.K_w]:
        player_pos.y -= speed
    if keys[p.K_s]:
        player_pos.y += speed
    if keys[p.K_a]:
        player_pos.x -= speed
    if keys[p.K_d]:
        player_pos.x += speed        

    p.draw.rect(screen, "red", (*player_pos, TILE_SIZE, TILE_SIZE))
