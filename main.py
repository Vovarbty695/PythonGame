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
            run = False  # Зупиняємо цикл

    # Перевіряємо, чи Pygame все ще активний, щоб уникнути помилок
    if not p.get_init():
        break

    screen.fill(BACKGROUND)  # Заповнюємо фон

    draw_world(screen)  # Малюємо світ
    player()            # Малюємо гравця


    fps = clock.get_fps()

    # Виводимо FPS в консоль
    print(f"FPS: {fps:.2f}")

    p.display.flip()    # Оновлюємо екран

    clock.tick(60)

# Закриваємо Pygame після завершення циклу
p.quit()