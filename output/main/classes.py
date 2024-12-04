import pygame
import random
import time

pygame.init()

def draw(images, screen):
    for image in images:
        image.draw(screen)

def walking(objects):
    for object in objects:
        object.walking()

kill_sound = pygame.mixer.Sound('sounds/kill.mp3')
miss_sound = pygame.mixer.Sound('sounds/not kill.mp3')

class Player:
    def __init__(self, health, *npc):

        self.health = health
        self.attack = random.randint(10, 20)
        self.alive = True
        self.speed = 2

        self.hunger = True
        self.hunger_nums = 100

        self.x = 370
        self.y = 280

        self.rect = pygame.Rect(self.x, self.y, 64, 64)

        self.image = pygame.image.load('ico.png')

        self.show_table = False

        self.tables = []

        self.npc = npc

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

            #self.control()

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

        elif key[pygame.K_s]:
            self.direction = self.anim_down
            self.update_animation()

        elif key[pygame.K_a]:
            self.direction = self.anim_left
            self.update_animation()

        elif key[pygame.K_d]:
            self.direction = self.anim_right
            self.update_animation()
    
        elif not any(key):
            self.anim_count = 0

    def control(self, key, screen):

        if key[pygame.K_1]:
            self.show_table = True

        if key[pygame.K_LSHIFT]:
            self.speed = 10
        else:
            self.speed = 7
            
        if self.show_table:
            self.tables.append(Workbench(self.x, self.y))
            draw(self.tables, screen)
            
class Background:
    def __init__(self, player):
        self.x = 0
        self.y = 0
        self.speed = 7
        self.player = player

        self.image = pygame.image.load('images/background.jpg')

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
        self.detection_rect = pygame.Rect(self.x, self.y, 128, 128)

        self.rect = pygame.Rect(self.x, self.y, 64, 64)

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
        self.text = pygame.font.Font(None, size).render(text, True, (color))

    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))  

class Text(GUI):
    def draw(self, screen):
        screen.blit(self.text, (self.x, self.y))  
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
        

def main(objects, screen):
    for object in objects:
        object.draw(screen)

def next_level(level):
    levels = [
        level_1,
    ]

        