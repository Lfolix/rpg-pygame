import pygame
import classes
import level_1

pygame.init()

texts = [
    classes.GUI(280, 0, "The Country", 50, "Green"),
    classes.GUI(225, 200, "WASD to move, left click to attack", 30, "Green"),
    classes.GUI(287, 500, "Press enter to start", 30, "Green")
]

start = True
def main(screen, key):
    global start
    if start:
        for i in texts:
            i.draw(screen)
    if key[pygame.K_RETURN]:
        start = False
