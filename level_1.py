import pygame
import classes
import interface
import inventory
import random

pygame.init()

player = classes.Player(100)
bg = classes.Background(player, "images/background.jpg")

npc = [
    classes.NPC(0, 0, 100, 2, 0.1, player),
    classes.NPC(100, 100, 100, 2, 0.1, player),
]

buildings = [
    classes.Building(200, 100, 'images/house_1.png', player),
    classes.Building(350, 100, 'images/house_1.png', player),
]

trees = [
    classes.Building(0, 0, 'images/tree.png', player),
]

bushes = [
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
    classes.Building(random.randint(0, 1000), random.randint(0, 1000), "images/bush.png", player),
]

items = [
    classes.DropedItem(0, 0, 'images/meat.png', player),
    classes.DropedItem(100, 0, 'images/meat.png', player),
    classes.DropedItem(200, 0, 'images/meat.png', player),
    classes.DropedItem(300, 0, 'images/meat.png', player),
    classes.DropedItem(400, 0, 'images/meat.png', player),
    classes.DropedItem(500, 0, 'images/meat.png', player),
    classes.DropedItem(500, 0, 'images/meat.png', player),
    classes.DropedItem(500, 0, 'images/meat.png', player),
    classes.DropedItem(500, 0, 'images/meat.png', player),
    classes.DropedItem(500, 0, 'images/meat.png', player),
    classes.DropedItem(500, 0, 'images/meat.png', player),
]

healths = [
    classes.Health(0, 0, 25, 'images/health.png', player)
]

is_load = True


def load(screen):
    if is_load:

        bg.draw(screen)

        classes.draw(items, screen)

        classes.draw(npc, screen)
        classes.draw(healths, screen)
        classes.draw(buildings, screen)

        classes.draw(bushes, screen)

        player.draw(screen)

        interface.main(screen, player)

        inventory.draw(screen, player)

        