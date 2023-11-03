import pygame

class Boss:
    boss_velocity = 10

    def __init__(self):
        self.boss_img = pygame.image.load('Textures/Boss.png')
        self.boss_img_rect = self.boss_img.get_rect()
        self.boss_img_rect.width -= 10
        self.boss_img_rect.height -= 10
        self.boss_img_rect.top = 600/2
        self.boss_img_rect.right = 1200
        self.up = True
        self.down = False

    def update(self, canvas, up_rect, down_rect):
        canvas.blit(self.boss_img, self.boss_img_rect)
        if self.boss_img_rect.top <= up_rect.bottom:
            self.up = False
            self.down = True
        elif self.boss_img_rect.bottom >= down_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.boss_img_rect.top -= self.boss_velocity
        elif self.down:
            self.boss_img_rect.top += self.boss_velocity
