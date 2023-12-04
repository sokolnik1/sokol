WIN_WIDTH = 1920  #(временно)
WIN_HEIGHT = 1080  #(временно)
TILESIZE = 42  # Размер 1 плиты карты в pxl (времененно)
FPS = 60

PLAYER_LAYER = 3  # Приоритет отображения слоя игрока
ENEMY_LAYER = 3  # Приоритет отображения слоя врага
WALL_LAYER = 2  # Приоритет отображения слоя стены
GROUND_LAYER = 1  # Приоритет отображения слоя пола

PLAYER_SPEED = 15
ENEMY_SPEED = 4

BLUE = (0, 154, 255)
BLACK = (0, 0, 0)
YELLOW = (249, 234, 25)

# высота дисплея(1080px) / высота плиты(32px) =~ 25(34)49 строк
# ширина дисплея(1920px) / ширина плиты(32px) =~ 40(60)156 столбцов
tilemap = [
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%2====================',
    '======================#--------------------------------------E-----------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------P-----------------------------------------------------+++++++++++++++++++++++++-------------------------------------T-----------------------------:====================',
    '======================#---------------------------------------------T----------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++--------------------T-----------------------t----------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#---------------------------------------T-------------------++++++++++++++++++++++++++++++-----------------------------------------------------------------:====================',
    '======================#-----------------E---------------------------------------++++++++++++++++++++++++++++++++++---------------------------------------------------------------:====================',
    '======================#------------------------------------------------------++++++++++++++++++++++++++++++++++++++++-----------------------T------------------------------------:====================',
    '======================#----------------------------------------------------++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------------------:====================',
    '======================#----------------------------t----------------------++++++++++++++++++++++++++++++++++++++++++++++---------------------------------------------------------:====================',
    '======================#--------------------------------------------------++++++++++++++++++++++++++++++++++++++++++++++++--------E-----------------------------------------------:====================',
    '======================#-------------------------------------------------++++++++++++++++++++++++++++++++++++++++++++++++++-------------------------------------------------------:====================',
    '======================#------------------t-----------------------------++++++++++++++++++++++++++++++++++++++++++++++++++++------------------------------------------------------:====================',
    '======================#---------------------------------------E-------++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------------------------------------------:====================',
    '======================#----------------------------------------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------------:====================',
    '======================#---------------------------------------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------------------------------:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++E+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:====================',
    '======================#-----------------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++----------------------------------------------------:====================',
    '======================#---------------------------T--------------------+++++++++++++++++++++++++++++++++++++++++++++++++++++-------------t---------------------------------------:====================',
    '======================#-------------------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++++++------------------------------------------------------:====================',
    '======================#--------------------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++++-------------------------------------------------------:====================',
    '======================#--------------------------------------E------------+++++++++++++++++++++++++++++++++++++++++++++++--------------------------------------------------------:====================',
    '======================#--------------------T------------------------t------+++++++++++++++++++++++++++++++++++++++++++++---------------------------------------------------------:====================',
    '======================#------------------------------------------------------+++++++++++++++++++++++++++++++++++++++++-------------t---------------------------------------------:====================',
    '======================#--------------------------------------------------------+++++++++++++++++++++++++++++++++++++-------------------------------------------------------------:====================',
    '======================#----------------------------------------------------------+++++++++++++++++++++++++++++++++---------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================#--------------------------------------------------------------+++++++++++++++++++++++++-------------------------------------------------------------------:====================',
    '======================3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4====================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
    '======================================================================================================================================================================================================',
]