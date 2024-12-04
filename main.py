import pygame
import classes
import level_1
import level_2
import level_3
import main_menu
import start_town
import interface
import trading
import time

screen = pygame.display.set_mode((800, 600))
title = pygame.display.set_caption("RPG GAME")
icon = pygame.display.set_icon(pygame.image.load('ico.png'))
fps = pygame.time.Clock()
level = level_1
level_num = 0

def next_level():
    global level
    global level_num
    levels = [
        level_1,
        level_2,
        level_3,
    ]

    level_num += 1
    if level_num > 2:
        level_num = 2

    level = levels[level_num]
    print(level)

running = True
while running:

    key = pygame.key.get_pressed()
    screen.fill('black')

    level.load(screen)

    if key[pygame.K_e]:
        time.sleep(1)
        next_level()


    fps.tick(60)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

        if event.type == pygame.MOUSEBUTTONDOWN:
            for person in level.npc:
                if level_1.player.rect.colliderect(person.rect) and person.rect.collidepoint(pygame.mouse.get_pos()):
                    person.health -= level_1.player.attack
                    classes.kill_sound.play()
            
            #for button in trading.buttons:
                #if button.rect.collidepoint(pygame.mouse.get_pos()):


pygame.quit()