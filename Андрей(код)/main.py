import pygame
from config import *
from sprites import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Отрисовка экрана
        self.clock = pygame.time.Clock()  # Частота кадров за 1 сек
        #self.font = pygame.font.Font('Arial',32) # Шрифт в игре (Временно)
        self.running = True  # Поле для распознавание передвижения

    # Метод для создания стен/препятствий
    def createTilmap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "#":
                    Wall(self, j, i)
                if column == "P":
                    Player(self, j, i)


    # Метод для запуска игры
    def new(self):
        self.playing = True  # Поле, отвечающее за продолжение игры(игрок умер и захотел продолжить или захотел выйти во время игры)
        self.all_sprites = pygame.sprite.LayeredUpdates()  # Объект, содержащий все спрайты в игре(стены, враги, и т.п) Для быстрого их обновления
        self.walls = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()  # тут содержатся все атакующие спрайты

        self.createTilmap()

    # Метод для хранения событий(нажатие клавиш, клик мыши и т.п.)
    def events(self):
        for event in pygame.event.get():  # тут мы получаем каждое отдельное событие из pygame
            if event.type == pygame.QUIT:  # Перехват попытки пользователя закрыть окно
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()  # Ищем каждый спрайт в группе 'все спрайты' 17стр., и вызываем в нем свой метод update(), который содержит свою логику обновления кадров
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)  # draw() просматривает каждый отдельный спрайт во 'все спрайты', находит изображение, находит хитбокс и рисует это всё в игровом окне
        self.clock.tick(FPS)  # Устанавливаем частоту кадров
        pygame.display.update()  # Обновляем экран

    # Метод для фиксирования игрового цикла(игра продолжается или конец игры)
    def main(self):
        while self.playing:
            self.events()  # Перехватывем событие в игре
            self.update()  # Обновляем игру для того, чтобы сменить(анимировать) новый кадр
            self.draw()  # Отрисовываем спрайтов на экране
        self.running = False

    def game_over(self):
        pass
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()