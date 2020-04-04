class Settings():
    def __init__(self):
        """属性初始化"""

        """屏幕"""
        self.screen_width = 700  # 添加屏幕宽属性
        self.screen_height = 600  # 高属性
        self.bg_color = (222, 222, 222)  # 背景颜色属性
        """飞船"""
        self.ship_speed_factor = 1.5  # 飞船速度
        """子弹"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        #子弹数量
        self.bullet_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1


