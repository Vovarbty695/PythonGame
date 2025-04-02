import pygame as p
from config import BACKGROUND, screen, icon
from player import player
from world import generate_world, draw_world

p.init()
p.display.set_caption("Minecraft2D")
p.display.set_icon(icon)

clock = p.time.Clock()
run = True
generate_world()

while run:
    for events in p.event.get():
        if events.type == p.QUIT:
            run = False  

    screen.fill(BACKGROUND)  

    draw_world(screen) 
    player()           


    fps = clock.get_fps()

    
    print(f"FPS: {fps:.2f}")

    p.display.flip()    

    clock.tick(60)

p.quit()