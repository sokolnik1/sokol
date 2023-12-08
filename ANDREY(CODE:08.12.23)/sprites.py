import time

import pygame
from config import *
import math
import random

class Spritesheet:  # класс для отрисовки таблицы спрайтов
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])

        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER  # Это слой игрока, нужен для отрисовки игрока поверх других слоёв, т.к слой уровня(трава, дорога)
        self.groups = self.game.all_sprites, self.game.enemies  # Добавляем врага в группу 'Все спрайты'
        pygame.sprite.Sprite.__init__(self, self.groups)  # Вызывается конструктор класса Sprite. Это инициализирует объект игрока, и он будет готов к отображению на экране и управлению.

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 42  # Ширина плиты
        self.height = 91  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.health = 100
        self.facing = random.choice(['left', 'right'])  # Сторона направления взгляда врага (по умолчанию: 'вниз')
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_traveling = random.randint(7, 30)

        #self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 42, 90)  # Изображение врага
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 41, 91)

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта врага = размеру прямоуг.)
        self.rect.x = self.x  # Положение хитбокса = положению  точки врага (по X и Y)
        self.rect.y = self.y

        # self.down_animations = [self.game.enemy_spritesheet.get_sprite(2, 5, self.width, self.height),
        #                         self.game.enemy_spritesheet.get_sprite(50, 5, self.width, self.height),
        #                         self.game.enemy_spritesheet.get_sprite(96, 5, self.width, self.height),
        #                         self.game.enemy_spritesheet.get_sprite(145, 5, self.width, self.height)]
        #
        # self.up_animations = [self.game.enemy_spritesheet.get_sprite(2, 99, self.width, self.height),
        #                       self.game.enemy_spritesheet.get_sprite(50, 99, self.width, self.height),
        #                       self.game.enemy_spritesheet.get_sprite(96, 99, self.width, self.height),
        #                       self.game.enemy_spritesheet.get_sprite(145, 99, self.width, self.height)]
        #
        self.left_animations = [self.game.enemy_spritesheet .get_sprite(0, 293, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(48, 293, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(96, 293, self.width, self.height),
                                self.game.enemy_spritesheet.get_sprite(148, 293, self.width, self.height)
                                ]

        self.right_animations = [self.game.enemy_spritesheet.get_sprite(1, 200, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(49, 200, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(97, 200, self.width, self.height),
                                 self.game.enemy_spritesheet.get_sprite(145, 200, self.width, self.height)
                                 ]

    def update(self):
        self.movement()
        self.animated()
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    # Метод движения врага
    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_traveling:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_traveling:
                self.facing = 'left'

    def animated(self):
        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(0, 293, self.width, self.height)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(1, 200, self.width, self.height)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1

# class CameraGroup(pygame.sprite.Sprite):
#     def __init__(self, game):
#         self.game = game
#         super().__init__()
#         self.display_surface = pygame.display.get_surface()
#
#     def custom_draw(self):
#         for sprite in self.game.decoration:
#             self.display_surface.blit(sprite.image, sprite.rect)
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):  # Конструктор для создания игрока (Через game получаем доступ ко всем переменным класа Game())

        self.game = game
        self._layer = PLAYER_LAYER  # Это слой игрока, нужен для отрисовки игрока поверх других слоёв, т.к слой уровня(трава, дорога)
        self.groups = self.game.all_sprites   # Добавляем игрока в группу 'Все спрайты'
        pygame.sprite.Sprite.__init__(self, self.groups)  # Вызывается конструктор класса Sprite. Это инициализирует объект игрока, и он будет готов к отображению на экране и управлению.

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 41  # Ширина плиты
        self.height = 91  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'  # Сторона направления взгляда игрока (по умолчанию: 'вниз')
        #attack = Attack(game, x, y)
        self.health = 100
        self.elapsed_time = 0
       # self.start_enemy_colission_time = 0
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)  #Изображение игрока

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта игрока = размеру прямоуг.)
        self.rect.x = self.x
        self.rect.y = self.y

        self.animations = {
            'down': [self.game.character_spritesheet.get_sprite(19, 21, self.width, self.height),
                     self.game.character_spritesheet.get_sprite(69, 21, self.width, self.height),
                     self.game.character_spritesheet.get_sprite(115, 21, self.width, self.height),
                     self.game.character_spritesheet.get_sprite(165, 21, self.width, self.height)],

            'up': [self.game.character_spritesheet.get_sprite(18, 127, 43, self.height),
                   self.game.character_spritesheet.get_sprite(67, 127, 39, self.height),
                   self.game.character_spritesheet.get_sprite(114, 127, 43, self.height),
                   self.game.character_spritesheet.get_sprite(165, 127, 39, self.height)],

            'left': [self.game.character_spritesheet.get_sprite(20, 352, 40, self.height),
                     self.game.character_spritesheet.get_sprite(68, 352, 40, self.height),
                     self.game.character_spritesheet.get_sprite(116, 352, 40, self.height),
                     self.game.character_spritesheet.get_sprite(164, 352, 40, self.height)],

            'right': [self.game.character_spritesheet.get_sprite(20, 239, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(71, 239, 37, self.height),
                      self.game.character_spritesheet.get_sprite(116, 239, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(163, 239, 40, self.height)],

        }

    def update(self):  # Предназначен для обновления состояния игрока на каждом шаге игрового цикла
        self.movement()  # тут будет прописана логика обновления
        self.animated()
        self.collide_enemy()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0
    def movement(self):
        keys = pygame.key.get_pressed()  # сюда получаем список всех клавиш клавиатуры

        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

        # Обновляем координаты всех спрайтов относительно новой позиции игрока
        for sprite in self.game.all_sprites:
            if keys[pygame.K_w]:
                sprite.rect.y -= self.y_change
            elif keys[pygame.K_s]:
                sprite.rect.y -= self.y_change
            if keys[pygame.K_a]:
                sprite.rect.x -= self.x_change
            elif keys[pygame.K_d]:
                sprite.rect.x -= self.x_change
    # Метод, содержащий логику столкноыений с блоками\стенами
    def collide_enemy(self):
        #global HEALTH
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)

        if hits:
            # while self.health > 0:
            #     pygame.time.wait(100)
            #     self.health -= 25
            self.kill()
            self.game.playing = False
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        # hits_chest = pygame.sprite.spritecollide(self, self.game.decoration, False)
        # if hits_chest:
        #     chest = Chest(self, hits_chest[0].x, hits_chest[0].y)
        #     chest.a

        if direction == "x":
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                elif self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                for sprite in self.game.all_sprites:
                    sprite.rect.x += PLAYER_SPEED if self.x_change > 0 else -PLAYER_SPEED

        elif direction == "y":
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                elif self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                for sprite in self.game.all_sprites:
                    sprite.rect.y += PLAYER_SPEED if self.y_change > 0 else -PLAYER_SPEED
    def animated(self):
        keys = pygame.key.get_pressed()
        direction = self.facing
        is_moving = self.x_change != 0 or self.y_change != 0

        if direction in self.animations:
            if not is_moving:
                self.image = self.animations[direction][0]
                    #self.image = self.game.character_attack_spritesheet.get_sprite(170, 463, self.width, self.height)
            else:
                # if keys[pygame.K_SPACE]:
                #     self.kill()
                index = math.floor(self.animation_loop)
                self.image = self.animations[direction][index]
                self.animation_loop += 0.3
                if self.animation_loop >= len(self.animations[direction]):
                    self.animation_loop = 1
                # else:
                #     self.image = self.game.character_attack_spritesheet.get_sprite(170, 463, self.width, self.height)

# class CameraGroup(pygame.sprite.Sprite):
#     def __init__(self, game):
#         self.game = game
#         self.groups = self.game.all_sprites  # Добавляем игрока в группу 'Все спрайты'
#         pygame.sprite.Sprite.__init__(self, self.groups)
#         self.display_surface = pygame.display.get_surface()
#     def custom_draw(self):
#         for sprite in sorted(self.game.all_sprites, key = lambda sprite.rect.centrey):
#             self.game.screen.blit(sprite.image, sprite.rect)
class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER  # Это слой игрока, нужен для отрисовки игрока поверх других слоёв, т.к слой уровня(трава, дорога)
        self.groups = self.game.all_sprites, self.game.attacks  # Добавляем игрока в группу 'Все спрайты'
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = 52
        self.height = 91
        self.x_change = 0
        self.y_change = 0

        self.animation_loop = 0
        self.image = self.game.character_attack_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.attack_animations = {
            'down': [self.game.character_attack_spritesheet.get_sprite(16, 454, 49, 91),
                     self.game.character_attack_spritesheet.get_sprite(69, 454, 39, 91),
                     self.game.character_attack_spritesheet.get_sprite(113, 454, 49, 91)],

            'up': [self.game.character_attack_spritesheet.get_sprite(17, 550, 47, 91),
                   self.game.character_attack_spritesheet.get_sprite(67, 550, 44, 91),
                   self.game.character_attack_spritesheet.get_sprite(113, 550, 47, 91)],

            'left': [self.game.character_attack_spritesheet.get_sprite(21, 742, 40, 91), #20, 352
                     self.game.character_attack_spritesheet.get_sprite(71, 742, 30, 91),
                     self.game.character_attack_spritesheet.get_sprite(116, 742, 41, 91)],

            'right': [self.game.character_attack_spritesheet.get_sprite(20, 646, 41, 91),
                      self.game.character_attack_spritesheet.get_sprite(66, 646, 51, 91),
                      self.game.character_attack_spritesheet.get_sprite(117, 646, 41, 91)]
        }

    def update(self):
        self.animated()
        self.rect.x += self.x_change
        self.collide('x')
        self.rect.y += self.y_change
        self.collide('y')

        self.x_change = 0
        self.y_change = 0

    def collide(self, direction):
        hits_enemy = pygame.sprite.spritecollide(self, self.game.enemies, True)
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)

        if direction == "x":
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                elif self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        elif direction == "y":
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                elif self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
    def animated(self):
        keys = pygame.key.get_pressed()
        direction = self.game.player.facing
        index = math.floor(self.animation_loop)

        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED

        elif keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED

        # for sprite in self.game.all_sprites:
        #     if keys[pygame.K_w]:
        #         sprite.rect.y -= self.y_change
        #     elif keys[pygame.K_s]:
        #         sprite.rect.y -= self.y_change
        #     if keys[pygame.K_a]:
        #         sprite.rect.x -= self.x_change
        #     elif keys[pygame.K_d]:
        #         sprite.rect.x -= self.x_change

        if direction in self.attack_animations:
            self.image = self.attack_animations[direction][index]
            #self.rect = self.image.get_rect()
            # self.rect.x = self.x
            # self.rect.y = self.y
            self.animation_loop += 0.3
            if direction == 'down' and self.attack_animations['left'][1]:
              # self.rect = self.rect.inflate((self.rect.x - 10), 0)
                pass
            if self.animation_loop >= len(self.attack_animations[direction]):
                self.kill()
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, imagee, img_x, img_y, img_width, img_height):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites, self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = imagee.get_sprite(img_x, img_y, img_width, img_height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Tree(pygame.sprite.Sprite):
    def __init__(self, game, x, y, imagee, img_x, img_y, img_width, img_height):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites,  self.game.walls  # , self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = imagee.get_sprite(img_x, img_y, img_width, img_height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y, imagee, img_x, img_y, img_width, img_height):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = imagee.get_sprite(img_x, img_y, img_width, img_height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
class Chest(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites, self.game.walls, self.game.decoration
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 78
        self.height = 50

        self.animation_loop = 0
        self.image = self.game.chest_spritesheet.get_sprite(30, 286, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.animations = [self.game.chest_spritesheet.get_sprite(30, 286, self.width, self.height),
                           self.game.chest_spritesheet.get_sprite(118, 264, self.width, self.height),
                           self.game.chest_spritesheet.get_sprite(215, 264, self.width, self.height)]
    # def animated(self):
    #     index = math.floor(self.animation_loop)
    #     for i  in len(self.animations):
    #
    #         self.animation_loop += 0.3
    #         if self.animation_loop >= len(self.animations):
    #             self.image = self.animations[2]
    #     # def collide_chest(self, direction):
    #     #     hits =
    # def update(self):
    #     animated()
class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


