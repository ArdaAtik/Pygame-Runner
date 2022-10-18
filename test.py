import pygame
from sys import exit
from UI import UI

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_name = UI('Press Space to play again!', (111, 196, 169), 400, 325)
info = UI('First Game Ever', (111, 196, 169), 400, 75)
score = UI(f'Score :{UI.current_time}', (111, 196, 169), 400, 50)

ui_group = pygame.sprite.Group()
ui_group.add(game_name)
ui_group.add(info)
player_surface_intro = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
player_surface_intro = pygame.transform.rotozoom(player_surface_intro, 0, 2)

player_rect_intro = player_surface_intro.get_rect(center=(400, 200))
game_active = False
print(ui_group)
start_time = 0
while True:
    for event in pygame.event.get():
        if game_active:
            pass
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if game_active:
        screen.fill((94, 129, 162))
        score.display_score(start_time)
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_surface_intro, player_rect_intro)
        ui_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
