from settings import *

pygame.init()
# Añadir sonidos--------------------------------------------------------------------------------
menu_music = "sound_effects\\special_sounds\\menu_music.mp3"

game_music = "sound_effects\\special_sounds\\underwater_music.mp3"

press_button_sound = pygame.mixer.Sound("sound_effects\\special_sounds\\button_pressed.mp3")

fio_start_game_sound = pygame.mixer.Sound('fio_sounds\\B4VFIO.mp3')

mission_start_sound = pygame.mixer.Sound("sound_effects\\special_sounds\\MISSION_START.mp3")

coin_sound = pygame.mixer.Sound('sound_effects\\special_sounds\\coin.mp3')

basic_shoot_gun_sound = pygame.mixer.Sound('sound_effects\\shooting.mp3')

heavy_machine_gun_sound = pygame.mixer.Sound('sound_effects\\special_sounds\\HM_GUN.mp3')

medusa_explosion_sound = pygame.mixer.Sound('sound_effects\\enemies_sound\\explosion_enemies.mp3')

rayo_sound = pygame.mixer.Sound('sound_effects\\enemies_sound\\electric_medusa.mp3')

rayo_colsion_sound = pygame.mixer.Sound('sound_effects\\enemies_sound\\electric_medusa_killing.mp3')