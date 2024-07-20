import pygame
import sys
import subprocess

# Import game modules
import pong
import tictactoe
import frogger

# Pygame Initialization
pygame.init()

# Screen size
screen = pygame.display.set_mode((800, 600))

# Title of the window
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font for menu
font = pygame.font.Font(None, 72)

# Menu options
options = ["Pong", "Tic Tac Toe", "Frogger"]
selected_option = 0

# Function to draw menu
def draw_menu():
    screen.fill(BLACK)
    for i, option in enumerate(options):
        color = WHITE if i == selected_option else (100, 100, 100)
        text = font.render(option, True, color)
        screen.blit(text, (350, 200 + i * 100))
    pygame.display.flip()

# Game loop for menu
while True:
    draw_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(options)
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(options)
            if event.key == pygame.K_RETURN:
                if selected_option == 0:
                    pong.pong_game()
                elif selected_option == 1:
                    tictactoe.tic_tac_toe_game()
                elif selected_option == 2:
                    frogger.frogger_game()
            if event.key == pygame.K_e:
                pygame.init()  # Re-initialize Pygame
                break  # Return to menu