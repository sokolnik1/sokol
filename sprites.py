import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):  # Конструктор для создания игрока (Через game получаем доступ ко всем переменным класа Game())

        self.game = game
        self._layer = PLAYER_LAYER  # Это слой игрока, нужен для отрисовки игрока поверх других слоёв, т.к слой уровня(трава, дорога)
        self.groups = self.game.all_sprites  # Добавляем игрока в группу 'Все спрайты'
        pygame.sprite.Sprite.__init__(self, self.groups)  # Вызывается конструктор класса Sprite. Это инициализирует объект игрока, и он будет готов к отображению на экране и управлению.

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE  # Ширина плиты
        self.height = TILESIZE  # Длинна плиты

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'  # Сторона направления взгляда игрока (по умолчанию: 'вниз')

        self.image = pygame.Surface([self.width, self.height])  #Изображение игрока (пока что квадрат)
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()  # Хитбокс(габариты точки(x,y)) - (Размер спрайта игрока = размеру прямоуг.)
        self.rect.x = self.x  # Положение хитбокса = положению  точки игрока (по X и Y)
        self.rect.y = self.y

    def update(self):  # Предназначен для обновления состояния игрока на каждом шаге игрового цикла
        self.movement()  # тут будет прописана логика обновления

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    # Метод движения игрока
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

    # Метод, содержащий логику столкноыений с блоками\стенами
    def collide_blocks(self, direction):
        if direction == "x":  # Проверка: находится ли прямая линия одного спррайта внутри прямой линии другого
            hits = pygame.sprite.spritecollide(self, self.game.walls,False)  # Передаём сюда объекты игрока и стены
            if hits:
                if self.x_change > 0:  # Проверка: движемся вправо
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:  # Проверка: движемся влево
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.walls,False)
            if hits:
                if self.y_change > 0:  # Проверка: движемся вверх
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:  # Проверка: движемся вниз
                    self.rect.y = hits[0].rect.bottom


class Wall(pygame.sprite.Sprite):
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
