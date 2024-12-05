import pygame
import random
import time
import inventory

pygame.init()

def draw(images, screen):
    for image in images:
        image.draw(screen)

def walking(objects):
    for object in objects:
        object.walking()

kill_sound = pygame.mixer.Sound('sounds/kill.mp3')
miss_sound = pygame.mixer.Sound('sounds/not kill.mp3')

battle_sounds = pygame.mixer.Sound("sounds/battle music.mp3")

class Item:
    def __init__(self, image, slot, title):
        self.image = pygame.image.load(image)
        self.slot = slot
        self.mouse = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        self.title = title
        self.health_coins = 10

    def draw(self, screen, slot):
        self.rect = pygame.Rect(self.slot[0], self.slot[1], 32, 32)
        self.mouse = pygame.mouse.get_pressed()
        screen.blit(self.image, (self.slot))
        #self.is_click(pygame.mouse)

        #if not inventory.alive:
            #self.rect.center = 24534562, 4567354

    def is_click(self, mouse):
        self.mouse = pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()

        if self.mouse[0]:
            print(self.player.inventory)
            if self.rect.collidepoint(self.mouse_pos):
                self.player.inventory.remove(self)

class Food(Item):
    def __init__(self, image, slot, title, health_coins):
        super().__init__(image, slot, title)
        self.health_coins = health_coins

class DropedItem:
    def __init__(self, x, y, image, player):
        self.x = x
        self.y = y
        self.image_path = image
        self.image = pygame.image.load(self.image_path)
        self.player = player
        self.rect = self.image.get_rect()

    def draw(self, screen):
        self.rect.center = self.x, self.y

        screen.blit(self.image, (self.x, self.y))
        self.camera(pygame.key.get_pressed())
        self.is_take()

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += self.player.speed

        if key[pygame.K_s]:
            self.y -= self.player.speed

        if key[pygame.K_a]:
            self.x += self.player.speed

        if key[pygame.K_d]:
            self.x -= self.player.speed

    def is_take(self):
        if self.player.rect.colliderect(self.rect):
            self.x = 1343245
            self.y = 3465345
            self.rect.center = self.y, self.x
            
            self.player.inventory.append(Food(self.image_path, None, "Meat", 20))

class Weapon():
    def __init__(self, damage, title, image, slot):
        self.damage = damage
        self.title = title
        self.image = pygame.image.load(image)
        self.slot = slot
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.slot))

class Player:
    def __init__(self, health, *npc):

        self.health = health
        self.attack = random.randint(10, 20)
        self.alive = True
        self.speed = 2

        self.hunger = True
        self.hunger_nums = 100

        self.inventory = [

        ]


        self.weapon = Weapon(15, "Weapon", 'images/meat.png', None)

        self.x = 370
        self.y = 280

        self.rect = pygame.Rect(self.x, self.y, 64, 64)

        self.image = pygame.image.load('ico.png')

        self.show_table = False

        self.tables = []
        self.level_up = False

        self.npc = npc

        self.level_up_sound = pygame.mixer.Sound('sounds/level_up.mp3')


        self.attack_level = 0
        self.run = 0

        self.anim_down = [
            pygame.image.load('player/player_1.png'),
            pygame.image.load('player/player_2.png'),
            pygame.image.load('player/player_3.png'),
            pygame.image.load('player/player_4.png'),
        ]

        self.anim_left = [
            pygame.image.load('player/player_5.png'),
            pygame.image.load('player/player_6.png'),
            pygame.image.load('player/player_7.png'),
            pygame.image.load('player/player_8.png'),
        ]

        self.anim_right = [
            pygame.image.load('player/player_9.png'),
            pygame.image.load('player/player_10.png'),
            pygame.image.load('player/player_11.png'),
            pygame.image.load('player/player_12.png'),
        ]

        self.anim_up = [
            pygame.image.load('player/player_13.png'),
            pygame.image.load('player/player_14.png'),
            pygame.image.load('player/player_15.png'),
            pygame.image.load('player/player_16.png'),
        ]

        self.direction = self.anim_down
        self.anim_count = 0

    def draw(self, screen):
        if self.alive:
            self.rect.center = self.x, self.y
            screen.blit(self.direction[self.anim_count // 6], (self.x, self.y))
            self.anim_walk(pygame.key.get_pressed())

            mouse = pygame.mouse.get_pressed()

            print(self.run)

            self.control(pygame.key.get_pressed(), screen)

            if self.run >= 100:
                self.speed += 0.5
                self.run = 0

            if mouse[1]:
                self.attack_level += 2

            if self.attack_level == 100:
                self.attack += 1
                self.attack_level = 0

        if self.health < 1:
            self.alive = False
            time.sleep(9999999999)

    def update_animation(self):
        self.anim_count += 1
        if self.anim_count == 24:
            self.anim_count = 0

    def anim_walk(self, key):
        if key[pygame.K_w]:
            self.direction = self.anim_up
            self.update_animation()
            self.run += 0.1

        elif key[pygame.K_s]:
            self.direction = self.anim_down
            self.update_animation()
            self.run += 0.1

        elif key[pygame.K_a]:
            self.direction = self.anim_left
            self.update_animation()
            self.run += 0.1

        elif key[pygame.K_d]:
            self.direction = self.anim_right
            self.update_animation()
            self.run += 0.1
    
        elif not any(key):
            self.anim_count = 0

    def control(self, key, screen):

        if key[pygame.K_1]:
            self.show_table = True

        if key[pygame.K_y]:
            print(self.inventory)

        #if key[pygame.K_5]:
            #self.inventory.append(Item('images/meat.png', None))
            
        if self.show_table:
            self.tables.append(Workbench(self.x, self.y))
            draw(self.tables, screen)
            
class Background:
    def __init__(self, player, image):
        self.x = 0
        self.y = 0
        self.speed = 7
        self.player = player

        self.image = pygame.image.load(image)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.player.alive:
            self.walk(pygame.key.get_pressed())

    def walk(self, key):
        if key[pygame.K_w]:
            self.y += self.player.speed

        if key[pygame.K_s]:
            self.y -= self.player.speed

        if key[pygame.K_a]:
            self.x += self.player.speed

        if key[pygame.K_d]:
            self.x -= self.player.speed

        if self.speed > 7:
            self.speed = 7

class NPC:
    def __init__(self, x, y, health, speed, attack, player):
        self.x = x
        self.y = y
        self.health = health
        self.alive = True 
        self.speed = 1
        self.attack = attack
        self.player = player
        self.detection_rect = pygame.Rect(self.x, self.y, 300, 300)

        self.rect = pygame.Rect(self.x, self.y, 100, 100)

        self.anim_down = [
            pygame.image.load('npc/npc_1.jpg'),
            pygame.image.load('npc/npc_2.jpg'),
            pygame.image.load('npc/npc_3.jpg'),
            pygame.image.load('npc/npc_4.jpg'),
        ]

        self.anim_left = [
            pygame.image.load('npc/npc_5.jpg'),
            pygame.image.load('npc/npc_6.jpg'),
            pygame.image.load('npc/npc_7.jpg'),
            pygame.image.load('npc/npc_8.jpg'),
        ]

        self.anim_right = [
            pygame.image.load('npc/npc_9.jpg'),
            pygame.image.load('npc/npc_10.jpg'),
            pygame.image.load('npc/npc_11.jpg'),
            pygame.image.load('npc/npc_12.jpg'),
        ]

        self.anim_up = [
            pygame.image.load('npc/npc_13.jpg'),
            pygame.image.load('npc/npc_14.jpg'),
            pygame.image.load('npc/npc_15.jpg'),
            pygame.image.load('npc/npc_16.jpg'),
        ]

        self.anim_count = 0
        self.direction = self.anim_down

    def draw(self, screen):
        if self.alive:
            screen.blit(self.direction[self.anim_count // 6], (self.x, self.y))
            self.rect.center = self.x, self.y
            self.detection_rect.center = self.x, self.y

        if self.health < 1:
            self.alive = False
            self.rect.center = 123435, 5364361

        if self.rect.colliderect(self.player.rect) and self.alive:
            self.player.health -= self.attack
            print(self.player.health)
        
        if self.player.alive:
            self.camera(pygame.key.get_pressed())
            self.walking()

        else:
            self.rect.center = 65746, 567345
            self.detection_rect = 2308742, 5489763            

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += self.player.speed

        if key[pygame.K_s]:
            self.y -= self.player.speed

        if key[pygame.K_a]:
            self.x += self.player.speed

        if key[pygame.K_d]:
            self.x -= self.player.speed

    def update_animation(self):
        self.anim_count += 1
        if self.anim_count == 24:
            self.anim_count = 0

    def walking(self):
        if self.alive:
            if self.player.rect.colliderect(self.detection_rect):
                if abs(self.player.x - self.x) > abs(self.player.y - self.y):
                    if self.player.x > self.x:
                        self.direction = self.anim_right
                        self.x += self.speed
                    elif self.player.x < self.x:
                        self.direction = self.anim_left
                        self.x -= self.speed
                else:
                    if self.player.y > self.y:
                        self.direction = self.anim_down
                        self.y += self.speed
                    elif self.player.y < self.y:
                        self.direction = self.anim_up
                        self.y -= self.speed

                self.update_animation()

class Workbench:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y

        self.image = pygame.image.load('images/workbench.jpg')
        self.player = player

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.player.alive:
            self.camera(pygame.key.get_pressed())

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += self.player.speed

        if key[pygame.K_s]:
            self.y -= self.player.speed

        if key[pygame.K_a]:
            self.x += self.player.speed

        if key[pygame.K_d]:
            self.x -= self.player.speed

class Person:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.image = pygame.image.load('player/player_1.png')
        self.player = player

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.player.alive:
            self.camera(pygame.key.get_pressed())

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += self.player.speed

        if key[pygame.K_s]:
            self.y -= self.player.speed

        if key[pygame.K_a]:
            self.x += self.player.speed

        if key[pygame.K_d]:
            self.x -= self.player.speed

class Building:
    def __init__(self, x, y, image, player):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.player = player
        self.is_draw = False

        self.list = []

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.is_draw = True
        if self.player.alive:
            self.camera(pygame.key.get_pressed())

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += self.player.speed

        if key[pygame.K_s]:
            self.y -= self.player.speed

        if key[pygame.K_a]:
            self.x += self.player.speed

        if key[pygame.K_d]:
            self.x -= self.player.speed

class GUI:
    def __init__(self, x, y, text, size, color):
        self.x, self.y = x, y
        self.text = text
        self.render = pygame.font.Font(None, size).render(text, True, (color))

    def draw(self, screen):
        screen.blit(self.render, (self.x, self.y))  

class Text(GUI):
    def draw(self, screen):
        screen.blit(self.render, (self.x, self.y))  
        self.camera(pygame.key.get_pressed())

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += 2

        if key[pygame.K_s]:
            self.y -= 2

        if key[pygame.K_a]:
            self.x += 2

        if key[pygame.K_d]:
            self.x -= 2

class Button:
    def __init__(self, x, y, text, width, height):
        self.x = x
        self.y = y
        self.text = pygame.font.Font(None, 20).render(text, True, ("Black"))
        self.width = width
        self.height = height
        self.surface = pygame.surface.Surface((self.width, self.height))
        self.surface.fill("white")
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.text, (self.rect.center))
        self.camera(pygame.key.get_pressed())

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += 2

        if key[pygame.K_s]:
            self.y -= 2

        if key[pygame.K_a]:
            self.x += 2

        if key[pygame.K_d]:
            self.x -= 2

class Health:
    def __init__(self, x, y, health_count, image, player):
        self.x = x
        self.y = y
        self.health_count = health_count
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.player = player

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.rect.center = self.x, self.y
        self.health_player()
        self.camera(pygame.key.get_pressed())

    def camera(self, key):
        if key[pygame.K_w]:
            self.y += 2

        if key[pygame.K_s]:
            self.y -= 2

        if key[pygame.K_a]:
            self.x += 2

        if key[pygame.K_d]:
            self.x -= 2

    def health_player(self):
        if self.player.rect.colliderect(self.rect):
            self.player.health += self.health_count
            self.x += 5463456
            self.rect.center = self.x, self.y

def main(objects, screen):
    for object in objects:
        object.draw(screen)





        
