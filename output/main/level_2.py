import pygame
import classes
import interface

pygame.init()

player = classes.Player(100)
bg = classes.Background(player)
font = pygame.font.Font(None, 20)

npc = [
    classes.NPC(0, 0, 100, 2, 0.1, player),
    classes.NPC(100, 100, 100, 2, 0.1, player),
    classes.NPC(400, 000, 100, 2, 0.1, player),
    classes.NPC(100, 000, 100, 2, 0.1, player),
]

persons = [
    classes.Person(480, 180, player)
]

texts = [
    classes.Text(480, 250, "Помогите! Меня окружили эти бандиты!", 20, "Black")
]

buildings = [
    classes.Building(200, 100, 'images/house_1.png', player),
    classes.Building(350, 100, 'images/house_1.png', player),
    classes.Building(550, 100, 'images/house_1.png', player),
]

is_load = True

def load(screen):
    if is_load:

        bg.draw(screen)

        classes.draw(npc, screen)
        classes.draw(buildings, screen)
        classes.draw(persons, screen)
        classes.draw(texts, screen)

        player.draw(screen)

        interface.main(screen, player)

        for i in npc:
            death = 0
            if i.health < 1:
                death += 1
            if death == len(npc):
                texts[0].text = "Спасибо! Ты спас мне жизнь!"


