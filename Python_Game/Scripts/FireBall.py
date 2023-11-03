import pygame

class FireBall:
    fireball_velocity = 20

    def __init__(self, boss):
        self.fireball = pygame.image.load('Textures/Fireball.png')
        self.fireball_img = pygame.transform.scale(self.fireball, (20, 20))
        self.fireball_img_rect = self.fireball_img.get_rect()
        self.fireball_img_rect.right = boss.boss_img_rect.left
        self.fireball_img_rect.top = boss.boss_img_rect.top + 30

    def update(self, canvas):
        canvas.blit(self.fireball_img, self.fireball_img_rect)

        if self.fireball_img_rect.left > 0:
            self.fireball_img_rect.left -= self.fireball_velocity
