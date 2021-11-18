import pygame

import Objects
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


class Boss(Objects.Objects):

    COLOR_MAP = {
        "red_boss": (RED_SPACE_BOSS, RED_EGG),
        "blue_boss": (BLUE_SPACE_BOSS, BLUE_EGG)
    }

    def __init__(self, x, y, color, health=50):
        super().__init__(x, y, health)
        self.Chicken_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.Chicken_img)

    def move(self, vel):
        self.x += vel
    # Boss đẻ trứng
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser.Laser(self.x + 50, self.y + 80, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


