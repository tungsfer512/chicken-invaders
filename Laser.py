import pygame

import Objects

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

# Trứng or laser
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    # Vẽ trứng/laser lên màn hình
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    # Di chuyển laser
    def move(self, vel):
        self.y += vel
    # Laser đã đi hết màn hình chưa???
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    # Kiểm tra va chạm của 2 đối tượng
    def collision(self, obj):
        return Objects.Objects.collide(self, obj)

