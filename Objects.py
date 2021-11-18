import pygame

import Laser

pygame.font.init()

# WINDOW
HEIGHT, WIDTH = 750, 750
WINDOWS = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Sfer's Shooter")
icon = pygame.image.load("data\pixel_ship_green_small.png")
pygame.display.set_icon(icon)

# Ảnh gà
RED_CHICKEN = pygame.image.load("data\starwar_red (1).png")
BLUE_CHICKEN = pygame.image.load("data\super_blue (1).png")
GREEN_CHICKEN = pygame.image.load("data\solider_green (1).png")

# BOSS
RED_SPACE_BOSS = pygame.image.load("data\starwar_red_boss.png")
BLUE_SPACE_BOSS = pygame.image.load("data\super_blue_boss.png")

# Ảnh tàu người chơi
YELLOW_SPACE_Chicken = pygame.image.load("data\\a (1).png")

# Laser của gà
RED_EGG = pygame.image.load( "data\\red_egg (1).png")
BLUE_EGG = pygame.image.load("data\\blue_egg (1).png")
GREEN_EGG = pygame.image.load("data\green_egg (1).png")

# Laser của người chơi
YELLOW_LASER = pygame.image.load("data\yellow_bullet (1).png")

# BACKGROUND
BACKGROUND = pygame.transform.scale(pygame.image.load("data\\background-black.png"), (WIDTH, HEIGHT))



class Objects:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.Chicken_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    # Vẽ đối tượng
    def draw(self, window):
        window.blit(self.Chicken_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
    # Trứng rơi/ đạn bắn với tốc độ vel
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    # Thời gian chờ sau khi bắn
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    # Bắn đạn/ đẻ trứng
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser.Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
    # Lấy chiều dài và cao của đối tượng
    def get_width(self):
        return self.Chicken_img.get_width()

    def get_height(self):
        return self.Chicken_img.get_height()

    # xét xem có va chạm nhau hay không
    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
