WIN_WIDTH = 800  #(временно)
WIN_HEIGHT = 600  #(временно)
TILESIZE = 32  # Размер 1 плиты карты в pxl (времененно)
FPS = 60

PLAYER_LAYER = 2  # Приоритет отображения слоя игрока
WALL_LAYER = 1  # Приоритет отображения слоя стены

PLAYER_SPEED = 4

BLUE = (0, 154, 255)
BLACK = (0, 0, 0)
YELLOW = (249, 234, 25)

# высота дисплея(600px) / высота плиты(32px) =~ 19 строк
# ширина дисплея(800px) / ширина плиты(32px) =~ 25 столбцов
tilemap = [
    '#########################',
    '#-----------------------#',
    '#---###-----------------#',
    '#-----------------------#',
    '#-----------------------#',
    '#-------------####------#',
    '#--------P-------##-----#',
    '#-----------------------#',
    '#------#----------------#',
    '#------###--------------#',
    '#------######-----------#',
    '#---------####----------#',
    '#-----------##----------#',
    '#-----------------------#',
    '#-----------------------#',
    '#-----------------------#',
    '#-----------------------#',
    '#-----------------------#',
    '#########################',
]