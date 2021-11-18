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

class Player(Objects.Objects):
    score: int

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.Chicken_img = YELLOW_SPACE_Chicken
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.Chicken_img)
        self.max_health = health
        self.score = 0
    # Đạn bay lên hết màn hình thì biến mất hoặc chạm vào gà thì gà và đạn đều biến mất
    def move_lasers(self, vel, objs):
        self.cooldown()
        self.score = 0
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.score = 5
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    # Đạn bay lên hết màn hình hoặc chạm vào boss thì biến mất. Đạn chạm vào boss 5 lần thì boss và đạn đều biến mất
    def move_lasers_boss(self, vel, objs):
        self.cooldown()
        self.score = 0
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= 10
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        if obj.health <= 0:
                            objs.remove(obj)
                            self.score = 10

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    # Thanh máu
    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.Chicken_img.get_height() + 10, self.Chicken_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.Chicken_img.get_height() + 10, self.Chicken_img.get_width() * (self.health/self.max_health), 10))
    # Bắn
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser.Laser(self.x + 40, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

