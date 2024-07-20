import pygame
import sys

def tic_tac_toe_game():
    pygame.init()

    # Screen size
    screen = pygame.display.set_mode((800, 600))

    # Title of the window
    pygame.display.set_caption("Tic Tac Toe")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (200, 200, 200)

    # Load sound effects
    pygame.mixer.init()
    x_sound = pygame.mixer.Sound('x_sound.wav')
    o_sound = pygame.mixer.Sound('o_sound.wav')
    winner_sound = pygame.mixer.Sound('winner.wav')

    # Game board
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    # Font
    font = pygame.font.Font(None, 72)
    small_font = pygame.font.Font(None, 36)

    def draw_board():
        screen.fill(WHITE)
        # Draw grid lines
        pygame.draw.line(screen, BLACK, (266, 50), (266, 550), 5)
        pygame.draw.line(screen, BLACK, (533, 50), (533, 550), 5)
        pygame.draw.line(screen, BLACK, (50, 200), (750, 200), 5)
        pygame.draw.line(screen, BLACK, (50, 400), (750, 400), 5)
        # Draw pieces
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    pygame.draw.line(screen, RED, (col * 266 + 70, row * 200 + 70), (col * 266 + 230, row * 200 + 180), 5)
                    pygame.draw.line(screen, RED, (col * 266 + 230, row * 200 + 70), (col * 266 + 70, row * 200 + 180), 5)
                elif board[row][col] == 'O':
                    pygame.draw.circle(screen, BLUE, (col * 266 + 150, row * 200 + 135), 60, 5)

    def check_winner():
        for row in board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != '':
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]
        return None

    def check_draw():
        for row in board:
            for cell in row:
                if cell == '':
                    return False
        return True

    game_over = False
    winner = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col = (x - 50) // 266
                row = (y - 50) // 200
                if 0 <= col < 3 and 0 <= row < 3 and board[row][col] == '':
                    board[row][col] = current_player
                    if current_player == 'X':
                        x_sound.play()
                        current_player = 'O'
                    else:
                        o_sound.play()
                        current_player = 'X'
                    winner = check_winner()
                    if winner or check_draw():
                        game_over = True

        draw_board()

        if game_over:
            if winner:
                text = font.render(f'{winner} wins!', True, BLACK)
                winner_sound.play()
            else:
                text = font.render('Draw!', True, BLACK)
            screen.blit(text, (300, 500))
            pygame.display.flip()
            pygame.time.wait(3000)
            return

        pygame.display.flip()

if __name__ == "__main__":
    tic_tac_toe_game()
