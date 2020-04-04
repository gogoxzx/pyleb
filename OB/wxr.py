import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    pygame.init()#执行初始化函数所有内容里的init
    ai_settings = Settings() #创建静态实例方法
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#创建屏幕，指向静态方法中的属性得出值
    alien = Alien(ai_settings,screen)

    pygame.display.set_caption("外星人大作战")#为窗口起名字
    #创建实例方法 一艘飞船
    ship = Ship(screen,ai_settings)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()#编组中的所有value调用Bullet类中的update方法
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.updeta_screen(ai_settings,screen,ship,aliens,bullets)
run_game()

