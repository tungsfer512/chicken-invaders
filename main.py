import sys
import pygame

import mainRun

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

title_font = pygame.font.SysFont("Calibri", 70)
run = True
while run:
    WINDOWS.blit(BACKGROUND, (0,0))
    title_label = title_font.render("Press space to begin...", 1, (255,255,255))
    WINDOWS.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
    pygame.display.update()
    # Nhấn phím cách để bắt đầu
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if key[pygame.K_SPACE]:
            mainRun.main()
sys.exit()
