import pygame

class Player:
    velocity = 10

    def __init__(self):
        self.player_img = pygame.image.load('Textures/Player.png')
        self.player_img_rect = self.player_img.get_rect()
        self.player_img_rect.left = 20
        self.player_img_rect.top = 600/2 - 100
        self.down = True
        self.up = False

    def update(self, canvas, up_rect, down_rect, SCORE):
        canvas.blit(self.player_img, self.player_img_rect)
        if self.player_img_rect.top <= up_rect.bottom:
            #if SCORE > self.player_score:
            #    self.player_score = SCORE
            return False
        if self.player_img_rect.bottom >= down_rect.top:
            #if SCORE > self.player_score:
            #    self.player_score = SCORE
            return False
        if self.up:
            self.player_img_rect.top -= 10
        if self.down:
            self.player_img_rect.bottom += 10
