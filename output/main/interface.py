import pygame
import classes

pygame.init()

def main(screen, player):
    interface = [
        classes.GUI(0, 0, f"Health: {int(player.health)}", 20, "Red")
    ]

    for i in interface:
        i.draw(screen)