import sys
import pygame
from sys import exit
import math
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate()

    def animate(self):
        if self.rect.bottom < 300:
            # jump animation
            self.image = self.player_jump
        else:  # walk animation
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


#
# snail_index = 0
# snail_surface = snail_frames[snail_index]
# fly_frame_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_index = 0
# fly_surface = fly_frames[snail_index]
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super(Obstacle, self).__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()
# test_surface = pygame.Surface((200, 200))
# test_surface.fill('Red')
game_active = False


# walk


def display_score():
    current_time = math.floor(pygame.time.get_ticks() / 100) - start_time
    score_surface = test_font.render(f'Score : {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > 0]
        return obstacle_list
    else:
        return []


def collision_check(player, obstacles):
    if obstacles:
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                return False
    return True


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


def player_animation():
    global player_surface, player_index
    if player_rect.bottom < 300:
        # jump animation
        player_surface = player_jump
    else:  # walk animation
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]


# sky and ground
sky_surface = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground.png').convert_alpha()

# text surface and rectangle
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # scores and shessh
start_time = 0
# text_surface = test_font.render('My game', False, (64, 64, 64))  # string , antialias , rgb
# text_rect = text_surface.get_rect(center=(400, 50))

# snail surface and rect
snail_frame_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surface = snail_frames[snail_index]
fly_frame_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surface = fly_frames[snail_index]

obstacle_rect_list = []

# Collisions and Rectangles

# player surface
player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))

# Intro screen
player_surface_intro = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
# player_surface_intro = pygame.transform.scale2x(player_surface_intro)
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
                # if randint(0, 2):
                #     obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 210)))
            if event.type == snail_animation_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surface = snail_frames[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surface = fly_frames[fly_index]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
                x, y = event.pos
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = math.floor(pygame.time.get_ticks() / 100)

    if game_active:
        # draw all our elements and update everything
        # Screen surfaces
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', text_rect)
        # pygame.draw.rect(screen, '#c0e8ec', text_rect, 10)
        score = display_score()
        # pygame.draw.line(screen, 'Silver', (0, 0), (800, 400), 5)
        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))
        # screen.blit(text_surface, text_rect)

        # Snail
        # snail_rect.right -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface, player_rect)
        player.draw(screen)
        obstacle_group.draw(screen)
        player.update()
        obstacle_group.update()

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision

        game_active = collision_check(player_rect, obstacle_rect_list)
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_surface_intro, player_rect_intro)
        score_message = test_font.render(f'Your score : {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 325))
        screen.blit(game_name, game_name_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        if score == 0:
            screen.blit(info_text, info_rect)
        else:
            screen.blit(score_message, score_message_rect)
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # if player_rect.colliderect(snail_rect):
    #     print('collision')
    # block image transfer put the surface inside another surface
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     # print(pygame.mouse.get_pressed())
    pygame.display.update()
    clock.tick(60)
