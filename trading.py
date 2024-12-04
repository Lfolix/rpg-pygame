import pygame
import classes
import interface

pygame.init()

#dsadas

player = classes.Player(100)
bg = classes.Background(player, "images/background.jpg")

buttons = [
    classes.Button(0, 0, "Text", 50, 50),
    classes.Button(100, 100, "Text", 50, 50),
]

buildings = [
    classes.Building(200, 100, 'images/house_1.png', player),
    classes.Building(350, 100, 'images/house_1.png', player),
]

is_load = True


def load(screen):
    if is_load:

        bg.draw(screen)

        classes.draw(buttons, screen)
        classes.draw(buildings, screen)

        player.draw(screen)

        interface.main(screen, player)