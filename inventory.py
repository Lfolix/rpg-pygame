import pygame
import classes
import time

pygame.init()

inventory = pygame.image.load('images/inventory.png')
player_image = pygame.image.load('images/player_inventory_image.png')

items = []

alive = False

slots = [
    (258, 145),
    (323, 145),
    (388, 145),
    (453, 145),

    (258, 242),
    (323, 242),
    (388, 242),
    (453, 242),

    (258, 339),
    (323, 339),
    (388, 339),
    (453, 339),
]

surrent_slots = [
    (10, 145)
]

sur_slot = -1

def draw(screen, player):

    global alive
    global sur_slot
    global key

    sur_slot = -1



    def finding_item(mouse):
        for i in player.inventory:
            if i.rect.collidepoint(mouse.get_pos()):
                print(i)
                return i
            

    for i in player.inventory:
        sur_slot += 1
        if sur_slot > len(player.inventory):
            sur_slot = len(player.inventory)
        i.slot = slots[sur_slot]

    player.weapon.slot = surrent_slots[0]

    player.weapon.draw(inventory)

    for i in player.inventory:
        i.draw(inventory, i.slot)

    health = pygame.font.Font(None, 40).render(f'Health: {int(player.health)}', True, ('Red'))

    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()


    if mouse[2]:
        time.sleep(0.2)

        if alive:
            alive = False

        else:
            alive = True


    if alive:
        screen.blit(inventory, (0, 0))
        inventory.blit(player_image, (8, 248))
        inventory.blit(health, (9, 9))

    mouse = pygame.Rect(int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1]), 10, 10)

    for i in player.inventory:
        if alive:
            if i.rect.collidepoint(mouse_pos):
                win = pygame.image.load('images/inventory_properties.png')
                win.blit(pygame.font.Font(None, 20).render(f'{i.title}', True, ('Red')), (48, 10))
                win.blit(pygame.font.Font(None, 20).render(f'Health coins: {i.health_coins}', True, ('Red')), (15, 25))
                screen.blit(win, (mouse_pos[0], mouse_pos[1]))  # Отображаем окно, исходя из позиции мыши
                break  # Если нашли элемент, выходим из цикла (достаточно показывать одно окно)

        #print("ok")

    #finding_item(pygame.mouse)

    if not alive:
        for i in player.inventory:
            i.rect.center = (436543763, 346243563)





        