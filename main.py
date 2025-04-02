import pygame as p

p.init()
screen = p.display.set_mode((800, 600))
p.display.set_caption("Minecraft2D")
run = True

while run:

    screen.fill(((231, 221, 255)))

    p.display.flip()

    for events in p.event.get():
        if events.type == p.QUIT:
            run = False
p.quit()

        