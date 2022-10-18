import sys
import pygame, time
from sys import exit
import math
from random import randint, choice
from Player import Player
from Obstacle import Obstacle
from UI import UI


class Buffs(pygame.sprite.Sprite):
    def __init__(self):
        super(Buffs, self).__init__()


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle()
player1 = Player()
player.add(player1)

obstacle_group = pygame.sprite.Group()
game_active = False


def display_score():
    current_time = math.floor(pygame.time.get_ticks() / 100) - start_time
    score_surface = test_font.render(f'Score : {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


# sky and ground
sky_surface = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground.png').convert_alpha()
apple_surface = pygame.image.load('./graphics/Apple.png').convert_alpha()
apple_rect = apple_surface.get_rect(center=(400, 200))
# text surface and rectangle
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # scores and shessh
start_time = 0

# Intro text


player_surface_intro = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
player_surface_intro = pygame.transform.rotozoom(player_surface_intro, 0, 2)
player_rect_intro = player_surface_intro.get_rect(center=(400, 200))
# Info text
info_text = test_font.render('Press Space to play again!', False, (111, 196, 169))
info_rect = info_text.get_rect(center=(400, 325))
# Game name
game_name = test_font.render('First Game Ever', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 75))
# Timer
obstacle_timer = pygame.USEREVENT + 1  # look it up
pygame.time.set_timer(obstacle_timer, 1500)
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)
# misc
player_gravity = 0
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = math.floor(pygame.time.get_ticks() / 100)
                    time.sleep(0.1)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        player.draw(screen)
        obstacle_group.draw(screen)
        player.update()
        obstacle_group.update()
        screen.blit(apple_surface, apple_rect)
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_surface_intro, player_rect_intro)
        score_message = test_font.render(f'Your score : {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 325))
        screen.blit(game_name, game_name_rect)

        player1.set_gravity_zero()
        if score == 0:
            screen.blit(info_text, info_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
