import pygame
from pygame.locals import *
from pygame import mixer
import math
import sys

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

pygame.init()
pygame.font.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cool Platformer")


x = 800
y = 600
player_x = 0
player_y = 0
player_speed = 0
player_acceleration = 0.4
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
pink = (247, 49, 188)
Calibri60 = pygame.font.SysFont("Calibri", 60)
Calibri120 = pygame.font.SysFont("Calibri", 120)
Calibri40 = pygame.font.SysFont("Calibri", 40)
ArcadeFont50 = pygame.font.Font("PublicPixel-0W6DP.ttf", 50)
ArcadeFont30 = pygame.font.Font("PublicPixel-0W6DP.ttf", 30)
cross = Calibri120.render("x", 1, white)
circle = Calibri120.render("o", 1, white)
pop_sfx = mixer.Sound("spacebar_soundfx.mp3")
player = pygame.image.load("white_square.png").convert_alpha()
spikes = pygame.image.load("spikes.png").convert_alpha()
welcome = ArcadeFont50.render("Use WASD---->", 1, white)
dodge = ArcadeFont50.render("Jump Over The", 1, white)
dodge1 = ArcadeFont50.render("Spikes", 1, white)
goodluck = ArcadeFont50.render("Don't Look Down!", 1, white)
enter = ArcadeFont30.render("'Enter' To Retry", 1, white)
menu_label = ArcadeFont30.render("'M' For Menu", 1, white)

gameover_label = ArcadeFont50.render("Game Over", 1, white)
win_label = ArcadeFont50.render("You Win!", 1, white)

# transformations of sprites
player = pygame.transform.scale(player, (50, 50))
spikes = pygame.transform.scale(spikes, (60, 60))

# functions


def isCollision(killer_x, killer_y, player_x, player_y):
    distance = math.sqrt(
        (math.pow(player_x - killer_x, 2)) + (math.pow(player_y - killer_y, 2))
    )
    if distance < 114:
        game_over = True
    else:
        pass


# all platforms
platforms_level1 = [
    # floor
    pygame.Rect(0, 450, 800, 25),
    # middle platform
    pygame.Rect(350, 300, 300, 25)
]
platforms_level2 = [
    # floor
    pygame.Rect(0, 450, 800, 25),
]
platforms_level3 = [
    # platform1
    pygame.Rect(0, 270, 100, 25),
    # platform2
    pygame.Rect(300, 270, 70, 25),
    # platforms3
    pygame.Rect(600, 270, 70, 25),
]


running = True
start_screen = True
point = 0
pressed = False
jump = False
game_over = False

# all levels
level_1 = False
level_2 = False
level_3 = False
level_4 = False
level_5 = False
win = False


while running == True:

    # main game loop

    if start_screen == True:
        # graphics
        window.fill(black)
        tic_tac_toe_label = ArcadeFont50.render("Main Menu", 1, white)
        window.blit(tic_tac_toe_label, (175, 80))

        if point == 0:

            start_label = ArcadeFont50.render("Start", 1, white)
            exit_label = ArcadeFont50.render("Exit", 1, white)
            choose_sign = ArcadeFont50.render("*", 1, white)
            window.blit(start_label, (300, 240))
            window.blit(exit_label, (300, 320))
            window.blit(choose_sign, (240, 250))

        elif point == 1:

            start_label = ArcadeFont50.render("Start", 1, white)
            exit_label = ArcadeFont50.render("Exit", 1, white)
            choose_sign = ArcadeFont50.render("*", 1, white)
            window.blit(start_label, (300, 240))
            window.blit(exit_label, (300, 320))
            window.blit(choose_sign, (240, 330))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    pop_sfx.play()
                    point += 1

                elif event.key == K_UP:
                    pop_sfx.play()
                    point -= 1
                elif event.key == K_RETURN:
                    if point == 0:
                        pop_sfx.play()
                        level_1 = True
                        start_screen = False
                    elif point == 1:
                        pygame.quit()
                        sys.exit()

        point = point % 2
        pygame.display.update()

    elif game_over == True:

        window.fill(black)
        window.blit(gameover_label, (180, 170))
        window.blit(enter, (150, 320))
        window.blit(menu_label, (180, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_RETURN:
                    game_over = False
                    level_1 = True
                    player_x = 0
                    player_y = 0
                elif event.key == K_m:
                    game_over = False
                    start_screen = True
                    player_x = 0
                    player_y = 0
                    player_y = 0

        pygame.display.update()
        fps.tick(60)

    elif win == True:

        window.fill(black)
        window.blit(win_label, (180, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps.tick(60)

    elif level_1 == True:

        # graphics
        window.fill(black)
        window.blit(player, (player_x, player_y))
        window.blit(welcome, (50, 100))

        # blit all platforms
        for p in platforms_level1:
            pygame.draw.rect(window, white, p)

        # event checker thing
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # borders for the sides
        if player_x >= 755:
            level_2 = True
            level_1 = False
            player_y = 350
            player_x = 20
        if player_x <= -10:
            player_x = -10

        # borders for platforms

        # the floor
        if player_y >= 405:
            player_y = 405
            player_speed = 0
            platform_collision = True
            jump = True

        # the middle platform
        elif player_y >= 254 and player_x >= 300 and player_x <= 640:
            player_y = 254
            player_speed = 0
            platform_collision = True
            jump = True

        # player input
        keys = pygame.key.get_pressed()
        if keys[ord("a")]:
            player_x -= 4

            if keys[ord("w")]:
                if jump == True:
                    player_speed = - 12
                    jump = False

        elif keys[ord("d")]:
            player_x += 4

            if keys[ord("w")]:
                if jump == True:
                    player_speed = - 12
                    jump = False

        player_speed += player_acceleration
        player_y += player_speed

        pygame.display.update()
        fps.tick(60)

    elif level_2 == True:

        # graphics
        window.fill(black)
        window.blit(player, (player_x, player_y))
        window.blit(dodge, (50, 100))
        window.blit(dodge1, (70, 200))
        window.blit(spikes, (400, 410))
        window.blit(spikes, (430, 410))
        window.blit(spikes, (460, 410))
        window.blit(spikes, (490, 410))

        # blit platforms
        for p in platforms_level2:
            pygame.draw.rect(window, white, p)

         # event checker thing
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # borders
        if player_y >= 405:
            player_y = 405
            player_speed = 0
            platform_collision = True
            jump = True
        if player_x <= -10:
            player_x = -10
        if player_x >= 755:
            level_2 = False
            level_3 = True
            player_y = 200
            player_x = 20

        # user input
        keys = pygame.key.get_pressed()
        if keys[ord("a")]:
            player_x -= 4
        elif keys[ord("d")]:
            player_x += 4

        elif jump == True:
            if keys[ord("w")]:
                player_speed = - 12
                jump = False

        player_speed += player_acceleration
        player_y += player_speed

        # collisions
        if player_y >= 380 and player_x >= 375 and player_x <= 527:
            player_speed = 0
            level_2 = False
            game_over = True

        pygame.display.update()
        fps.tick(60)

    elif level_3 == True:

        window.fill(black)
        window.blit(player, (player_x, player_y))
        window.blit(goodluck, (10, 80))
        window.blit(spikes, (400, 550))
        window.blit(spikes, (430, 550))
        window.blit(spikes, (460, 550))
        window.blit(spikes, (490, 550))
        window.blit(spikes, (280, 550))
        window.blit(spikes, (310, 550))
        window.blit(spikes, (340, 550))
        window.blit(spikes, (370, 550))
        window.blit(spikes, (250, 550))
        window.blit(spikes, (220, 550))
        window.blit(spikes, (190, 550))
        window.blit(spikes, (160, 550))
        window.blit(spikes, (130, 550))
        window.blit(spikes, (100, 550))
        window.blit(spikes, (70, 550))
        window.blit(spikes, (40, 550))
        window.blit(spikes, (10, 550))
        window.blit(spikes, (-20, 550))
        window.blit(spikes, (520, 550))
        window.blit(spikes, (550, 550))
        window.blit(spikes, (580, 550))
        window.blit(spikes, (610, 550))
        window.blit(spikes, (640, 550))
        window.blit(spikes, (670, 550))
        window.blit(spikes, (700, 550))
        window.blit(spikes, (730, 550))
        window.blit(spikes, (760, 550))
        window.blit(spikes, (790, 550))
        window.blit(spikes, (820, 550))

        # blit platforms
        for p in platforms_level3:
            pygame.draw.rect(window, white, p)

        # event checker thing
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[ord("a")]:
            player_x -= 4
        elif keys[ord("d")]:
            player_x += 4

        elif jump == True:
            if keys[ord("w")]:
                player_speed = - 12
                jump = False

        player_speed += player_acceleration
        player_y += player_speed

        # borders

        # first platform
        if player_y >= 226 and player_x >= -20 and player_x <= 81:
            player_y = 226
            player_speed = 0
            platform_collision = True
            jump = True

        # second platform
        if player_y >= 226 and player_x >= 263 and player_x <= 370:
            player_y = 226
            player_speed = 0
            platform_collision = True
            jump = True

        # third platform
        if player_y >= 226 and player_x >= 563 and player_x <= 670:
            player_y = 226
            player_speed = 0
            platform_collision = True
            jump = True

        if player_x <= -10:
            player_x = -10
        if player_x >= 755:
            level_3 = False
            win = True
        if player_y >= 538:
            level_3 = False
            game_over = True

        pygame.display.update()
        fps.tick(60)


# loop over, game over
pygame.quit()
