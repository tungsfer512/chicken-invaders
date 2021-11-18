import pygame
import random

import Objects
import Player
import Enemy
import Boss

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

def main():
    run = True

    FPS = 60
    level = 0
    lives = 5

    # Font chữ
    main_font = pygame.font.SysFont("Calibri", 50)
    lost_font = pygame.font.SysFont("Calibri", 60)
    # Mảng gà + số lượng gà mỗi level + tốc độ đẻ trứng
    enemies = []
    wave_length = 5
    enemy_vel = 1
    # Tốc độ di chuyển + bắn của người chơi
    player_vel = 5
    laser_vel = 5

    player = Player.Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0
    score = 0
    # reset màn hình FPS lần / giây
    def redraw_window():
        WINDOWS.blit(BACKGROUND, (0,0))
        # Hiển thị sô mạng còn lại + level
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        score_lable = main_font.render(f"Score: {score}", 1, (255,255,255))
        WINDOWS.blit(lives_label, (10, 10))
        WINDOWS.blit(score_lable, (WIDTH // 2 - score_lable.get_width() // 2, 10))
        WINDOWS.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        # Hiển thị gà và người chơi
        for enemy in enemies:
            enemy.draw(WINDOWS)

        player.draw(WINDOWS)
        # Nếu thua in ra "You lost..."
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WINDOWS.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        # Nếu hết máu và còn mạng --> hồi sinh
        if lives > 0 and player.health <= 0:
            player.health = 100
            lives -= 1
        # Nếu hết mạng --> thua
        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        # Nếu mảng enermies rỗng --> hết level --> sang level mới
        # Nếu là level 5, 10, 15, 20, ... thì có boss (số lượng boss = level//5)
        # Mỗi ván mới cộng thêm 5 gà
        if len(enemies) == 0:
            level += 1
            if level % 5 != 0:
                wave_length += 5
                for i in range(wave_length):
                    enemy = Enemy.Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                    enemies.append(enemy)
            elif level:
                for i in range(level // 5):
                    boss = Boss.Boss(random.randrange(130, WIDTH - 130), 0, random.choice(["red_boss", "blue_boss"]))
                    enemies.append(boss)
        # Thoát game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Di chuyển bằng các phím mũi tên
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        # Bắn liên tục
        player.shoot()
        score += player.score
        # Xét xem đang ở level boss hay level thường
        if level % 5 != 0:
            for enemy in enemies:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2*60) == 1:
                    enemy.shoot()
                if Objects.Objects.collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy)
                    score += 5
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)
            player.move_lasers(-laser_vel, enemies)
        else:
            for enemy in enemies:
                if enemy.x + enemy.get_width() >= WIDTH -10:
                    enemy.y += 10
                    enemy.x += 5
                    enemy.y += 10
                    enemy.x += 5
                    enemy.y += 10
                    enemy.x -= 5
                    enemy.y += 10
                    enemy.x -= 5
                    enemy_vel *= -1
                elif enemy.x <= 10:
                    enemy_vel *= -1
                    enemy.y += 10
                    enemy.x -= 5
                    enemy.y += 10
                    enemy.x -= 5
                    enemy.y += 10
                    enemy.x += 5
                    enemy.y += 10
                    enemy.x += 5
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                if random.randrange(0, 2 * 75) == 1:
                    enemy.shoot()
                if Objects.Objects.collide(enemy, player):
                    player.health -= 50
                    enemies.remove(enemy)
                    score += 10
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 2
                    enemies.remove(enemy)
            player.move_lasers_boss(-laser_vel, enemies)
            score += player.score
            pygame.display.update();
