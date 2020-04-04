import pygame

class Ship():
    def __init__(self, screen,ai_settings):
        """初始化飞船并设置其初始位置"""
        self.screen = screen #screen 屏幕
        self.ai_settings = ai_settings

        """加载飞船图像并获取其外接矩形"""
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央  rect 矩形  center 中心 conterx x轴的中心 contery y轴的中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.center = float(self.rect.centerx) #将ship图片的x坐标存在了center中
        self.ycenter = float(self.rect.bottom)#将ship图片距离屏幕上方的距离存在ycenter中

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx +=1
            self.center += self.ai_settings.ship_speed_factor #上方初始化时创建的实例方法,ai_settings即为settings.py，找到自己的速度
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.ycenter += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.ycenter -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.ycenter
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)