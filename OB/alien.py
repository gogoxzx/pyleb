import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setings = ai_settings
        # 加载外星人图像，并设置起rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每一个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.switch = True
        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.x < self.screen_rect.right and self.switch:
            self.x += self.ai_setings.alien_speed_factor
            self.rect.x = self.x
            if self.x == 699:
                self.switch = False
        elif self.x > self.screen_rect.left and self.switch == False:
            self.x -= self.ai_setings.alien_speed_factor
            self.rect.x = self.x
            if self.x == 0:
                self.switch = True
