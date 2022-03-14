import pygame
from pygame.locals import *
from pygame import mixer
import sys
import math
import random
import time


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

pygame.init()
pygame.font.init()
pygame.mixer.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("beepboopblap's platform game")


x = 800
y = 600
player_x = 0
player_y = 0
player_speed = 0
player_acceleration = 0.4
enemy_x = 300
enemy_y = 0
enemy_x1 = 500
enemy_y1 = 0
enemy_x2 = 700
enemy_y2 = 0
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
game_over_sfx = mixer.Sound("game_over.mp3")
background_music = mixer.music.load("background_music.mp3")
player_white = pygame.image.load("white_square.png").convert_alpha()
player_yellow = pygame.image.load("yellow_square.png").convert_alpha()
player_green = pygame.image.load("green_square.png").convert_alpha()
player_orange = pygame.image.load("orange_square.png").convert_alpha()
player_blue = pygame.image.load("blue_square.png").convert_alpha()
player_whiteprev = pygame.image.load("white_square.png").convert_alpha()
player_yellowprev = pygame.image.load("yellow_square.png").convert_alpha()
player_greenprev = pygame.image.load("green_square.png").convert_alpha()
player_orangeprev = pygame.image.load("orange_square.png").convert_alpha()
player_blueprev = pygame.image.load("blue_square.png").convert_alpha()
spikes = pygame.image.load("spikes.png").convert_alpha()
pipe = pygame.image.load("pipe.png").convert_alpha()
flipped_spike = pygame.image.load("flipped_spike.png").convert_alpha()
welcome = ArcadeFont50.render("Use WASD---->", 1, yellow)
dodge = ArcadeFont50.render("Jump Over The", 1, white)
dodge1 = ArcadeFont50.render("Spikes", 1, red)
goodluck = ArcadeFont50.render("Don't Look Down!", 1, red)
careful_label = ArcadeFont50.render("Be Careful", 1, white)
enter = ArcadeFont30.render("'Enter' To Retry", 1, white)
menu_label = ArcadeFont30.render("'M' For Menu", 1, white)
madeby = ArcadeFont30.render("Made by", 1, white)
me = ArcadeFont50.render("beepboopblap", 1, yellow)
esc_label = ArcadeFont30.render("Press 'esc' to Escape", 1, white)
choose_label = ArcadeFont50.render("Choose a Skin", 1, yellow)


gameover_label = ArcadeFont50.render("Game Over", 1, red)
win_label = ArcadeFont50.render("You Win!", 1, yellow)

# transformations of sprites
player_white = pygame.transform.scale(player_white, (50, 50))
player_yellow = pygame.transform.scale(player_yellow, (50, 50))
player_green = pygame.transform.scale(player_green, (50, 50))
player_blue = pygame.transform.scale(player_blue, (50, 50))
player_orange = pygame.transform.scale(player_orange, (50, 50))
player_whiteprev = pygame.transform.scale(player_white, (300, 300))
player_yellowprev = pygame.transform.scale(player_yellow, (300, 300))
player_greenprev = pygame.transform.scale(player_green, (300, 300))
player_blueprev = pygame.transform.scale(player_blue, (300, 300))
player_orangeprev = pygame.transform.scale(player_orange, (300, 300))
spikes = pygame.transform.scale(spikes, (60, 60))
pipe = pygame.transform.scale(pipe, (100, 100))
flipped_spike = pygame.transform.scale(flipped_spike, (60, 60))


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
    # platform1#
    pygame.Rect(25, 270, 70, 25),
    #  platform2
    pygame.Rect(300, 270, 70, 25),
    # platforms3
    pygame.Rect(600, 270, 70, 25),
]
platforms_level4 = [
    # floor
    pygame.Rect(0, 450, 800, 25),

]

# functions


def isCollision(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt(
        (math.pow(player_x - enemy_x, 2)) + (math.pow(player_y - enemy_y, 2))
    )
    if distance < 50:
        return True
    else:
        return False


running = True
start_screen = True
credits_screen = False
point = 0
point1 = 0
pressed = False
jump = False
game_over = False
skin_chooser = False

# all levels
level_1 = False
level_2 = False
level_3 = False
level_4 = False
level_5 = False
win = False

# background_music

while running == True:

    # main game loop

    if start_screen == True:
        # graphics
        window.fill(black)
        main_menu = ArcadeFont50.render("Main Menu", 1, yellow)
        window.blit(main_menu, (175, 80))

        if point == 0:

            start_label = ArcadeFont50.render("Start", 1, white)
            exit_label = ArcadeFont50.render("Exit", 1, white)
            credits = ArcadeFont50.render("Credits", 1, white)
            choose_sign = ArcadeFont50.render("*", 1, white)
            window.blit(start_label, (290, 240))
            window.blit(exit_label, (290, 320))
            window.blit(credits, (290, 400))
            window.blit(choose_sign, (230, 250))

        elif point == 1:

            start_label = ArcadeFont50.render("Start", 1, white)
            exit_label = ArcadeFont50.render("Exit", 1, white)
            credits = ArcadeFont50.render("Credits", 1, white)
            choose_sign = ArcadeFont50.render("*", 1, white)
            window.blit(start_label, (290, 240))
            window.blit(exit_label, (290, 320))
            window.blit(credits, (290, 400))
            window.blit(choose_sign, (230, 330))

        elif point == 2:

            start_label = ArcadeFont50.render("Start", 1, white)
            exit_label = ArcadeFont50.render("Exit", 1, white)
            credits = ArcadeFont50.render("Credits", 1, white)
            choose_sign = ArcadeFont50.render("*", 1, white)
            window.blit(start_label, (290, 240))
            window.blit(exit_label, (290, 320))
            window.blit(credits, (290, 400))
            window.blit(choose_sign, (230, 410))

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
                        skin_chooser = True
                        start_screen = False
                    elif point == 1:
                        pygame.quit()

                        start_screen = False

        point = point % 3
        pygame.display.update()

    elif skin_chooser == True:

        white_square = ArcadeFont30.render("White", 1, white)
        yellow_square = ArcadeFont30.render("Yellow", 1, white)
        green_square = ArcadeFont30.render("Green", 1, white)
        blue_square = ArcadeFont30.render("Blue", 1, white)
        orange_square = ArcadeFont30.render("Orange", 1, white)
        choose_sign = ArcadeFont50.render("*", 1, white)

        window.fill(black)
        window.blit(choose_label, (97, 80))
        window.blit(white_square, (97, 200))
        window.blit(yellow_square, (97, 270))
        window.blit(green_square, (97, 340))
        window.blit(blue_square, (97, 410))
        window.blit(orange_square, (97, 480))

        if point == 0:
            window.blit(choose_sign, (40, 200))
            window.blit(player_whiteprev, (420, 200))

        elif point == 1:
            window.blit(choose_sign, (40, 270))
            window.blit(player_yellowprev, (420, 200))

        elif point == 2:
            window.blit(choose_sign, (40, 340))
            window.blit(player_greenprev, (420, 200))

        elif point == 3:
            window.blit(choose_sign, (40, 410))
            window.blit(player_blueprev, (420, 200))

        elif point == 4:
            window.blit(choose_sign, (40, 480))
            window.blit(player_orangeprev, (420, 200))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_UP:
                    point -= 1
                elif event.key == K_DOWN:
                    point += 1
                    pop_sfx.play()
                elif event.key == K_RETURN:
                    skin_chooser = False
                    level_1 = True
                    if point == 0:
                        player_sprite = player_white
                    elif point == 1:
                        player_sprite = player_yellow
                    elif point == 2:
                        player_sprite = player_green
                    elif point == 3:
                        player_sprite = player_blue
                    elif point == 4:
                        player_sprite = player_orange

        point = point % 5
        pygame.display.update()
        fps.tick(60)

    elif credits_screen == True:

        window.fill(black)
        window.blit(madeby, (175, 80))
        window.blit(me, (100, 280))
        window.blit(esc_label, (80, 500))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    credits_screen = False
                    start_screen = True

        pygame.display.update()
        fps.tick(60)

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

        pygame.display.update()
        fps.tick(60)

    elif win == True:

        window.fill(black)
        window.blit(win_label, (200, 180))
        window.blit(menu_label, (200, 400))
        window.blit(elapsed_label, (150, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key == K_m:
                    win = False
                    start_screen = True

        pygame.display.update()
        fps.tick(60)

    elif level_1 == True:

        start_time = time.time()

        # graphics
        window.fill(black)
        window.blit(player_sprite, (player_x, player_y))
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

        elif keys[ord("w")]:
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
        window.blit(player_sprite, (player_x, player_y))
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

        elif keys[ord("w")]:
            if jump == True:
                player_speed = - 12
                jump = False

        player_speed += player_acceleration
        player_y += player_speed

        # collisions
        if player_y >= 380 and player_x >= 375 and player_x <= 527:
            game_over_sfx.play()
            player_speed = 0
            level_2 = False
            game_over = True

        pygame.display.update()
        fps.tick(60)

    elif level_3 == True:

        window.fill(black)
        window.blit(player_sprite, (player_x, player_y))
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

        elif keys[ord("w")]:
            if jump == True:
                player_speed = - 12
                jump = False

        player_speed += player_acceleration
        player_y += player_speed

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

        # borders

        if player_x <= -10:
            player_x = -10
        if player_x >= 755:
            level_3 = False
            level_4 = True
            player_x = 0
            player_y = 250
        if player_y >= 550:
            game_over_sfx.play()
            game_over = True
            level_3 = False

        pygame.display.update()
        fps.tick(60)

    elif level_4 == True:

        window.fill(black)
        window.blit(careful_label, (50, 100))
        window.blit(player_sprite, (player_x, player_y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # input
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

        elif keys[ord("w")]:
            if jump == True:
                player_speed = - 12
                jump = False

        player_speed += player_acceleration
        player_y += player_speed

        # blit all platforms
        for p in platforms_level4:
            pygame.draw.rect(window, white, p)

        # borders
        if player_y >= 405:
            player_y = 405
            player_speed = 0
            platform_collision = True
            jump = True

        # enemy and enemy collision

        if enemy_y < y:

            window.blit(flipped_spike, (enemy_x, enemy_y))
            enemy_y = enemy_y + 7
            if enemy_y > 400:
                enemy_x = random.randrange(200, 700)
                enemy_y = 0

            # Collision
            collision = isCollision(enemy_x, enemy_y, player_x, player_y)

            if collision:
                enemy_y = 0
                enemy_x = random.randrange(0, x)
                game_over = True
                level_4 = False
                game_over_sfx.play()

        if enemy_y1 < y:

            window.blit(flipped_spike, (enemy_x1, enemy_y1))
            enemy_y1 = enemy_y1 + 5
            if enemy_y1 > 400:
                enemy_x1 = random.randrange(200, 700)
                enemy_y1 = 0

            # Collision
            collision = isCollision(enemy_x1, enemy_y1, player_x, player_y)

            if collision:
                enemy_y1 = 0
                enemy_x1 = random.randrange(0, x)
                game_over = True
                level_4 = False
                game_over_sfx.play()

        if enemy_y2 < y:

            window.blit(flipped_spike, (enemy_x2, enemy_y2))
            enemy_y2 = enemy_y2 + 3
            if enemy_y2 > 400:
                enemy_x2 = random.randrange(200, 700)
                enemy_y2 = 0

            # Collision
            collision = isCollision(enemy_x2, enemy_y2, player_x, player_y)

            if collision:
                enemy_y2 = 0
                enemy_x2 = random.randrange(0, x)
                game_over = True
                level_4 = False
                game_over_sfx.play()

        # borders
        if player_x <= -10:
            player_x = -10
        if player_x >= 755:
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_lapsed = float(time_lapsed + 3)
            time_lapsed = round(time_lapsed)
            elapsed_label = ArcadeFont30.render(
                "Elapsed: " + str(time_lapsed) + " seconds", 1, white)
            win = True
            level_4 = False
            player_x = 0
            player_y = 250

        pygame.display.update()
        fps.tick(60)

# loop over, game over
pygame.quit()
