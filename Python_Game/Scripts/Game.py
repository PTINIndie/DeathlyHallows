import pygame
import sys

import Player 
import FireBall
import Boss
import TopScore

############################################################################
# Start Details #
pygame.init()

Window_width = 1200
Window_height = 600
FPS = 20
Black = (0,0,0)
Green = (0,255,0)
ADD_NEW_FIREBALL_RATE = 25
bricks_img = pygame.image.load('Textures\BrickWall.png')
up_img_rect = bricks_img.get_rect()
up_img_rect.left = 0
down_img_rect = bricks_img.get_rect()
down_img_rect.left = 0
CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)

canvas = pygame.display.set_mode((Window_width, Window_height))
pygame.display.set_caption('Arcade Deathly Hallows - By Yashar Mirzaei')

topScore = TopScore.TopScore()

############################################################################
# Game Over # !When player lose the game
def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('Musics/GameOver.mp3')
    music.play()
    topScore.top_score(SCORE)
    game_over_img = pygame.image.load('Textures/End.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (Window_width/2, Window_height/2)
    canvas.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()
############################################################################
# Start Game # !Start the game 
def start_game():
    canvas.fill(Black)
    start_img = pygame.image.load('Textures/Start.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (Window_width/2, Window_height/2)
    canvas.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()
############################################################################
# Check Level # !Check for difficulty for make game harder  
def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        up_img_rect.bottom = 50
        down_img_rect.top = Window_height - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        up_img_rect.bottom = 100
        down_img_rect.top = Window_height - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        up_img_rect.bottom = 150
        down_img_rect.top = Window_height - 150
        LEVEL = 3
    elif SCORE > 30:
        up_img_rect.bottom = 200
        down_img_rect.top = Window_height - 200
        LEVEL = 4
############################################################################
# Update # !Update each frame of the game ("Void Update" in C#)
def game_loop():
    while True:
        global boss
        boss = Boss.Boss()
        fireBalls = FireBall.FireBall(boss)
        player = Player.Player()
        add_new_fireball_counter = 0
        global SCORE
        SCORE = 0
        global  HIGH_SCORE
        fireball_list = []
        pygame.mixer.music.load('Musics/Game.mp3')
        pygame.mixer.music.play(-1, 0.0)
        while True:
            canvas.fill(Black)
            check_level(SCORE)
            boss.update(canvas ,up_img_rect,down_img_rect)
            add_new_fireball_counter += 1

            if add_new_fireball_counter == ADD_NEW_FIREBALL_RATE:
                add_new_fireball_counter = 0
                new_fireball = FireBall.FireBall(boss)
                fireball_list.append(new_fireball)
            for f in fireball_list:
                if f.fireball_img_rect.left <= 0:
                    fireball_list.remove(f)
                    SCORE += 1
                f.update(canvas)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.up = True
                        player.down = False
                    elif event.key == pygame.K_DOWN:
                        player.down = True
                        player.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player.up = False
                        player.down = True
                    elif event.key == pygame.K_DOWN:
                        player.down = True
                        player.up = False

            score_font = font.render('Score:'+str(SCORE), True, Green)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, up_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:'+str(LEVEL), True, Green)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, up_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:'+str(topScore.high_score),True,Green)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, up_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(bricks_img, up_img_rect)
            canvas.blit(bricks_img, down_img_rect)
            playerState = player.update(canvas, up_img_rect, down_img_rect, SCORE)
            if(playerState == False):
                game_over()
            for f in fireball_list:
                if f.fireball_img_rect.colliderect(player.player_img_rect):
                    #if SCORE > player.player_score:
                    #    player.player_score = SCORE
                    game_over()
            pygame.display.update()
            CLOCK.tick(FPS)
############################################################################
# Start Game # 
start_game()
############################################################################