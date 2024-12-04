import pygame
import classes
import interface

pygame.init()

player = classes.Player(100)
bg = classes.Background(player)

npc = [
    classes.NPC(0, 0, 100, 2, 0.1, player),
    classes.NPC(100, 100, 100, 2, 0.1, player),
]

buildings = [
    classes.Building(200, 100, 'images/house_1.png', player),
    classes.Building(350, 100, 'images/house_1.png', player),
]

is_load = True


def load(screen):
    if is_load:

        bg.draw(screen)

        classes.draw(npc, screen)
        classes.draw(buildings, screen)

        player.draw(screen)

        interface.main(screen, player)
        