import pygame
import sys

def pong_game():
    # Pygame Initialization
    pygame.init()

    # Screen size
    screen = pygame.display.set_mode((800, 600))

    # Title of the window
    pygame.display.set_caption("Pong Game")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Load sound effects
    pygame.mixer.init()
    hit_sound = pygame.mixer.Sound('hit.wav')
    point_sound = pygame.mixer.Sound('point.wav')
    winner_sound = pygame.mixer.Sound('winner.wav')

    # Paddle A
    paddleA = pygame.Rect(30, 30, 20, 100)
    paddleA_speed = 0

    # Paddle B
    paddleB = pygame.Rect(750, 30, 20, 100)
    paddleB_speed = 0

    # Ball
    ball = pygame.Rect(375, 275, 20, 20)
    ball_speed_x = 5
    ball_speed_y = 5

    # Score
    scoreA = 0
    scoreB = 0
    max_score = 10

    # Font for score
    font = pygame.font.Font(None, 72)
    winner_font = pygame.font.Font(None, 100)

    # Game Loop
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return
                if event.key == pygame.K_w:
                    paddleA_speed = -5
                if event.key == pygame.K_s:
                    paddleA_speed = 5
                if event.key == pygame.K_UP:
                    paddleB_speed = -5
                if event.key == pygame.K_DOWN:
                    paddleB_speed = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddleA_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddleB_speed = 0

        if not game_over:
            # Move paddles
            paddleA.y += paddleA_speed
            paddleB.y += paddleB_speed

            # Move ball
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            # Ball collision with walls
            if ball.y < 0 or ball.y > 580:
                ball_speed_y *= -1
                hit_sound.play()

            # Ball collision with paddles
            if ball.colliderect(paddleA) or ball.colliderect(paddleB):
                ball_speed_x *= -1
                hit_sound.play()

            # Ball out of bounds
            if ball.x < 0:
                scoreB += 1
                point_sound.play()
                ball.x = 375
                ball.y = 275
                ball_speed_x *= -1
            if ball.x > 780:
                scoreA += 1
                point_sound.play()
                ball.x = 375
                ball.y = 275
                ball_speed_x *= -1

            # Check for winner
            if scoreA == max_score or scoreB == max_score:
                game_over = True
                winner_text = f"{'Player A' if scoreA == max_score else 'Player B'} Wins!"
                winner_sound.play()

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddleA)
        pygame.draw.rect(screen, WHITE, paddleB)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (400, 0), (400, 600))

        # Draw score
        score_text = font.render(f"{scoreA} - {scoreB}", True, WHITE)
        screen.blit(score_text, (350, 10))

        if game_over:
            winner_surface = winner_font.render(winner_text, True, WHITE)
            screen.blit(winner_surface, (200, 250))

        # Update display
        pygame.display.flip()
        pygame.time.Clock().tick(60)

        # Check if game is over to return to menu
        if game_over:
            pygame.time.wait(3000)
            return

if __name__ == "__main__":
    pong_game()
