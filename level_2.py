import pygame
import classes
import interface

pygame.init()

player = classes.Player(100)
bg = classes.Background(player, "images/background.jpg")
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
death = 0

def load(screen):
    global death
    print(death)
    if is_load:

        for i in npc:
            if not i.alive:
                death += 1
            if death > len(npc):
                texts[0].text = "Спасибо! Ты спас мне жизнь!"

        bg.draw(screen)

        classes.draw(npc, screen)
        classes.draw(buildings, screen)
        classes.draw(persons, screen)
        classes.draw(texts, screen)

        player.draw(screen)

        interface.main(screen, player)


