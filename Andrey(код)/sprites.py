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
        self.width = TILESIZE  # Ширина плиты
        self.height = TILESIZE  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])  # Сторона направления взгляда врага (по умолчанию: 'вниз')
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_traveling = random.randint(7, 30)

        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, 42, 90)  # Изображение врага
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта врага = размеру прямоуг.)
        self.rect.x = self.x  # Положение хитбокса = положению  точки врага (по X и Y)
        self.rect.y = self.y

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
        self.width = 63  # Ширина плиты
        self.height = 112  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'  # Сторона направления взгляда игрока (по умолчанию: 'вниз')
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)  #Изображение игрока

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта игрока = размеру прямоуг.)
        self.rect.x = self.x  # Положение хитбокса = положению  точки игрока (по X и Y)
        self.rect.y = self.y


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
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    # Метод, содержащий логику столкноыений с блоками\стенами
    def collide_blocks(self, direction):

        if direction == "x":  # Проверка: находится ли прямая линия одного спррайта внутри прямой линии другого
            hits = pygame.sprite.spritecollide(self, self.game.walls,False)  # Передаём сюда объекты игрока и стены
            if hits:
                if self.x_change > 0:  # Проверка: движемся вправо
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                if self.x_change < 0:  # Проверка: движемся влево
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.walls,False)
            if hits:
                if self.y_change > 0:  # Проверка: движемся вверх
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change < 0:  # Проверка: движемся вниз
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED

    def animated(self):
        down_animations = [self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(63, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(126, 0, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(189, 0, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(0, 112, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(63, 112, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(126, 112, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(189, 112, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(0, 336, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(63, 336, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(126, 336, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(189, 336, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(0, 224, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(63, 224, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(126, 224, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(189, 224, self.width, self.height)]
        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 112, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 336, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1
        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(0, 224, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 4:
                    self.animation_loop = 1

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites, self.game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrarian_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Tree(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WALL_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 200
        self.height = 200

        self.image = self.game.tree_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

