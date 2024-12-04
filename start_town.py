import pygame
import classes

pygame.init()

player = classes.Player(100)
bg = classes.Background(player, "images/background.jpg")

persons = [
    classes.Person(150, 350, player),
]

buildings = [
    classes.Building(100, 200, "images/house_1.png", player)
]

npc = []

is_load = True
def load(screen):
    if is_load:
        bg.draw(screen)

        classes.draw(persons, screen)
        classes.draw(buildings, screen)

        player.draw(screen)