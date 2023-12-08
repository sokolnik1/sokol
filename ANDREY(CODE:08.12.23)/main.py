import pygame
from config import *
from sprites import *
import sys
class Game:
    X = None
    Y = None
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.FULLSCREEN)  # Отрисовка экрана
        self.clock = pygame.time.Clock()  # Частота кадров за 1 сек
        self.font = pygame.font.Font('arial.ttf',54) # Шрифт в игре (Временно)
        self.game_isPaused = False
        self.running = True  # Поле для распознавание передвижения

        self.character_spritesheet = Spritesheet('img/Player/Movement/character.png') # ЛИСТ СО СПРАЙТАМИ ПЕРСОНАЖА
        self.character_attack_spritesheet = Spritesheet('img/Player/Movement/character.png')
        self.enemy_spritesheet = Spritesheet('img/Enemy/Movement/character1.png')  # ЛИСТ СО СПРАЙТАМИ ПЕРСОНАЖА
        self.block_spritesheet = Spritesheet('img/Level_textures/all_sprites.png')
        self.terrarian_spritesheet = Spritesheet('img/Level_textures/all_sprites.png')  # ЛИСТ СО СПРАЙТАМИ земли
        self.tree_spritesheet = Spritesheet('img/Level_textures/all_sprites.png')
        self.chest_spritesheet = Spritesheet('img/Level_textures/all_sprites.png')
        self.main_spritesheet = pygame.image.load('img/Level_textures/MainScr.jpg').convert()

        self.text = self.font.render(f'Health: {HEALTH}', True, WHITE)
    # Метод для создания стен/препятствий
    def createTilmap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i, self.terrarian_spritesheet, 7, 221, 43, 43)
                if column == "+":
                    Ground(self, j, i, self.block_spritesheet, 59, 221, 43, 43)
                if column == "=":
                    Block(self, j, i, self.block_spritesheet, 5, 5, 43, 43)  #  Блок моря

                if column == "#":
                    Block(self, j, i, self.block_spritesheet, 115, 168, 42, 43)
                if column == "%":
                    Block(self, j, i, self.block_spritesheet, 7, 168, 43, 42)
                if column == "$":
                    Block(self, j, i, self.block_spritesheet, 59, 168, 43, 43)
                if column == ":":
                    Block(self, j, i, self.block_spritesheet, 169, 168, 43, 43)
                if column == "1":
                    Block(self, j, i, self.block_spritesheet, 15, 367, 43, 43)
                if column == "2":
                    Block(self, j, i, self.block_spritesheet, 207, 367, 43, 43)
                if column == "3":
                    Block(self, j, i, self.block_spritesheet, 143, 367, 43, 43)
                if column == "4":
                    Block(self, j, i, self.block_spritesheet, 79, 367, 43, 43)
                if column == "C":
                    Chest(self, j, i)
                if column == "T":
                    Tree(self, j, i, self.tree_spritesheet, 433, 1, 185, 193)
                if column == "t":
                    Tree(self, j, i, self.tree_spritesheet, 250, 1, 167, 197)

                if column == "P":
                    self.player = Player(self, j, i)
                    self.X = j
                    self.Y = i
                if column == "E":
                    Enemy(self, j, i)
    # Метод для запуска игры
    def new(self):
        self.playing = True  # Поле, отвечающее за продолжение игры(игрок умер и захотел продолжить или захотел выйти во время игры)
        self.all_sprites = pygame.sprite.LayeredUpdates()  # Объект, содержащий все спрайты в игре(стены, враги, и т.п) Для быстрого их обновления
        self.walls = pygame.sprite.LayeredUpdates()
        self.decoration = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()  # тут содержатся все атакующие спрайты

        self.createTilmap()
        for sprite in self.all_sprites:
            sprite.rect.y += WIN_HEIGHT / 2 - self.Y * TILESIZE
            sprite.rect.x += WIN_WIDTH / 2 - self.X * TILESIZE

    # Метод для хранения событий(нажатие клавиш, клик мыши и т.п.)
    def events(self):
        for event in pygame.event.get():  # тут мы получаем каждое отдельное событие из pygame
            if event.type == pygame.QUIT:  # Перехват попытки пользователя закрыть окно
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        self.player.image = self.character_spritesheet.get_sprite(170, 463, 41, 91)
                        Attack(self, self.player.rect.x, self.player.rect.y)
                    if self.player.facing == 'down':
                        self.player.image = self.character_spritesheet.get_sprite(170, 463, 41, 91)
                        Attack(self, self.player.rect.x, self.player.rect.y)
                    if self.player.facing == 'right':
                        self.player.image = self.character_spritesheet.get_sprite(170, 463, 41, 91)
                        Attack(self, self.player.rect.x, self.player.rect.y)
                    if self.player.facing == 'left':
                        self.player.image = self.character_attack_spritesheet.get_sprite(170, 463, 41, 91)
                        Attack(self, self.player.rect.x, self.player.rect.y)
                if event.key == pygame.K_ESCAPE:
                    self.game_over()
    def update(self):
        self.all_sprites.update()  # Ищем каждый спрайт в группе 'все спрайты' 17стр., и вызываем в нем свой метод update(), который содержит свою логику обновления кадров
    def draw(self):
        self.all_sprites.draw(self.screen)  # draw() просматривает каждый отдельный спрайт во 'все спрайты', находит изображение, находит хитбокс и рисует это всё в игровом окне
        self.screen.blit(self.text, (10, 10))
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
        intro = True
        self.screen.blit(self.main_spritesheet, (0, 0))
        play_button = Button(765, 517, 360, 112)
        exit_button = Button(883, 709, 225, 63)

        while intro:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            for event in pygame.event.get():
                if exit_button.is_pressed(mouse_pos, mouse_pressed):
                    self.playing = False
                    self.running = False
                    intro = False

                if play_button.is_pressed(mouse_pos, mouse_pressed):
                    for sprite in self.all_sprites:
                        sprite.kill()
                    self.new()
                    self.main()
                    intro = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.main()
                self.clock.tick(FPS)
                pygame.display.update()

    def intro_screen(self):
        intro = True
        self.screen.blit(self.main_spritesheet, (0, 0))
        play_button = Button(765, 517, 360, 112)
        exit_button = Button(883, 709, 225, 63)

        while intro:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            for event in pygame.event.get():  # тут мы получаем каждое отдельное событие из pygame
                if exit_button.is_pressed(mouse_pos, mouse_pressed):
                    intro = False
                    self.running = False

                if play_button.is_pressed(mouse_pos, mouse_pressed):
                    intro = False
            pygame.display.update()
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()