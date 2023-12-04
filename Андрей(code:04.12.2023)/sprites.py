import pygame
from config import *
import math
import random

class Spritesheet:  # класс для отрисовки таблицы спрайтов
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])

        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        # sprite.set_colorkey(BLACK)
        return sprite

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER  # Это слой игрока, нужен для отрисовки игрока поверх других слоёв, т.к слой уровня(трава, дорога)
        self.groups = self.game.all_sprites, self.game.enemies  # Добавляем врага в группу 'Все спрайты'
        pygame.sprite.Sprite.__init__(self, self.groups)  # Вызывается конструктор класса Sprite. Это инициализирует объект игрока, и он будет готов к отображению на экране и управлению.

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE  # Ширина плиты
        self.height = TILESIZE  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])  # Сторона направления взгляда врага (по умолчанию: 'вниз')
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_traveling = random.randint(7, 30)

        #self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 42, 90)  # Изображение врага
        self.image = self.game.enemy_spritesheet.get_sprite(2, 5, 41, 91)

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта врага = размеру прямоуг.)
        self.rect.x = self.x  # Положение хитбокса = положению  точки врага (по X и Y)
        self.rect.y = self.y

        # self.down_animations = [self.game.character_spritesheet.get_sprite(2, 5, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(50, 5, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(96, 5, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(145, 5, self.width, self.height)]
        #
        # self.up_animations = [self.game.character_spritesheet.get_sprite(2, 99, self.width, self.height),
        #                       self.game.character_spritesheet.get_sprite(50, 99, self.width, self.height),
        #                       self.game.character_spritesheet.get_sprite(96, 99, self.width, self.height),
        #                       self.game.character_spritesheet.get_sprite(145, 99, self.width, self.height)]
        #
        # self.left_animations = [self.game.character_spritesheet.get_sprite(2, 291, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(50, 291, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(96, 291, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(145, 291, self.width, self.height)]
        #
        # self.right_animations = [self.game.character_spritesheet.get_sprite(2, 195, self.width, self.height),
        #                          self.game.character_spritesheet.get_sprite(50, 195, self.width, self.height),
        #                          self.game.character_spritesheet.get_sprite(96, 195, self.width, self.height),
        #                          self.game.character_spritesheet.get_sprite(145, 195, self.width, self.height)]

    def update(self):
        self.movement()
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

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):  # Конструктор для создания игрока (Через game получаем доступ ко всем переменным класа Game())

        self.game = game
        self._layer = PLAYER_LAYER  # Это слой игрока, нужен для отрисовки игрока поверх других слоёв, т.к слой уровня(трава, дорога)
        self.groups = self.game.all_sprites  # Добавляем игрока в группу 'Все спрайты'
        pygame.sprite.Sprite.__init__(self, self.groups)  # Вызывается конструктор класса Sprite. Это инициализирует объект игрока, и он будет готов к отображению на экране и управлению.

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 41  # Ширина плиты
        self.height = 91  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'  # Сторона направления взгляда игрока (по умолчанию: 'вниз')
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(19, 21, self.width, self.height)  #Изображение игрока

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта игрока = размеру прямоуг.)
        self.rect.x = self.x  # Положение хитбокса = положению  точки игрока (по X и Y)
        self.rect.y = self.y


        # self.down_animations = [self.game.character_spritesheet.get_sprite(19, 21, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(69, 21, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(115, 21, self.width, self.height),
        #                         self.game.character_spritesheet.get_sprite(165, 21, self.width, self.height)]
        #
        # self.up_animations = [self.game.character_spritesheet.get_sprite(18, 127, 43, self.height),
        #                       self.game.character_spritesheet.get_sprite(67, 127, 39, self.height),
        #                       self.game.character_spritesheet.get_sprite(114, 127, 43, self.height),
        #                       self.game.character_spritesheet.get_sprite(165, 127, 39, self.height)]
        #
        # self.left_animations = [self.game.character_spritesheet.get_sprite(20, 352, 40, self.height),
        #                         self.game.character_spritesheet.get_sprite(68, 352, 40, self.height),
        #                         self.game.character_spritesheet.get_sprite(116, 352, 40, self.height),
        #                         self.game.character_spritesheet.get_sprite(164, 352, 40, self.height)]
        #
        # self.right_animations = [self.game.character_spritesheet.get_sprite(20, 239, self.width, self.height),
        #                          self.game.character_spritesheet.get_sprite(71, 239, 37, self.height),
        #                          self.game.character_spritesheet.get_sprite(116, 239, self.width, self.height),
        #                          self.game.character_spritesheet.get_sprite(163, 239, 40, self.height)]

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
                      self.game.character_spritesheet.get_sprite(163, 239, 40, self.height)]
        }

    def update(self):  # Предназначен для обновления состояния игрока на каждом шаге игрового цикла
        self.movement()  # тут будет прописана логика обновления
        self.animated()
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
    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)

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
                # if keys[pygame.K_SPACE]:
                #     self.image = self.animations[direction][0]
            else:
                index = math.floor(self.animation_loop)
                self.image = self.animations[direction][index]
                self.animation_loop += 0.3
                if self.animation_loop >= len(self.animations[direction]):
                    self.animation_loop = 1
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
        self.image = self.game.character_attack_spritesheet.get_sprite(16, 454, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.game.character_attack_spritesheet.get_sprite(16, 454, 49, 91),
                                self.game.character_attack_spritesheet.get_sprite(69, 454, 43, 91),
                                self.game.character_attack_spritesheet.get_sprite(113, 454, 49, 91)]

        self.up_animations = [self.game.character_attack_spritesheet.get_sprite(17, 550, 47, 91),
                              self.game.character_attack_spritesheet.get_sprite(67, 550, 44, 91),
                              self.game.character_attack_spritesheet.get_sprite(113, 550, 47, 91)]

        self.left_animations = [self.game.character_attack_spritesheet.get_sprite(21, 742, 40, 91),
                                self.game.character_attack_spritesheet.get_sprite(61, 742, 50, 91),
                                self.game.character_attack_spritesheet.get_sprite(116, 742, 41, 91)]

        self.right_animations = [self.game.character_attack_spritesheet.get_sprite(20, 646, 41, 91),
                                 self.game.character_attack_spritesheet.get_sprite(66, 646, 51, 91),
                                 self.game.character_attack_spritesheet.get_sprite(117, 646, 41, 91)]

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
        direction = self.game.player.facing
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            # self.rect.y -= PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED

        if direction == 'up':
            self.image = self.up_animations[math.floor(self.animation_loop)]
        elif direction == 'down':
            self.image = self.down_animations[math.floor(self.animation_loop)]
        elif direction == 'left':
            self.image = self.left_animations[math.floor(self.animation_loop)]
        elif direction == 'right':
            self.image = self.right_animations[math.floor(self.animation_loop)]

        self.animation_loop += 0.3
        if self.animation_loop >= 3:
            self.kill()  # уничтожаем анимацию атаки


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

        # if imagee == ""
        self.image = imagee.get_sprite(img_x, img_y, img_width, img_height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect = self.rect.inflate(0, -self.rect.height // 2.5)

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