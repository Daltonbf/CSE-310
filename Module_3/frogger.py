import pygame
import sys
import random

# Pygame Initialization
pygame.init()

# Screen size
screen = pygame.display.set_mode((800, 600))

# Title of the window
pygame.display.set_caption("Frogger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Frogger properties
frogger = pygame.Rect(375, 550, 50, 50)
frogger_speed = 50

# Car properties
cars = [pygame.Rect(0, 450, 50, 50), pygame.Rect(150, 400, 50, 50), pygame.Rect(300, 350, 50, 50), pygame.Rect(450, 300, 50, 50), pygame.Rect(600, 250, 50, 50)]
car_speed = 5

# Score
score = 0

# Game over
game_over = False

# Function to draw game
def draw_game():
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (0, 550, 800, 50))  # Grass
    pygame.draw.rect(screen, WHITE, frogger)  # Frogger
    for car in cars:
        pygame.draw.rect(screen, WHITE, car)  # Cars
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

# Function to draw game over
def draw_game_over():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over! Score: " + str(score), True, WHITE)
    screen.blit(text, (200, 250))
    pygame.display.flip()

def frogger_game():
    global score
    global game_over
    game_over = False
    while True:
        if not game_over:
            draw_game()
        else:
            draw_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP:
                        frogger.y -= frogger_speed
                    if event.key == pygame.K_DOWN:
                        frogger.y += frogger_speed
                    if event.key == pygame.K_LEFT:
                        frogger.x -= frogger_speed
                    if event.key == pygame.K_RIGHT:
                        frogger.x += frogger_speed
                if event.key == pygame.K_e:
                    pygame.quit()
                    import menu  # Return to menu
                    sys.exit()

        # Move cars
        for car in cars:
            car.x += car_speed
            if car.x > 800:
                car.x = -50
                car.y = random.randint(250, 450)

        # Check collision with cars
        for car in cars:
            if frogger.colliderect(car):
                game_over = True

        # Check if frogger reached the top
        if frogger.y < 250:
            score += 1
            frogger.y = 550

        pygame.time.delay(100)

frogger_game()