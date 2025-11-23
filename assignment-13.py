import pygame
import sys

# Initialize Pygame
pygame.init()

# ----------- PLAYER NAME INPUT -----------
player1_name = input("Enter Player 1 Name (Left Paddle): ")
player2_name = input("Enter Player 2 Name (Right Paddle): ")

# Window settings
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font for UI
font = pygame.font.SysFont("Arial", 32)

# Paddle settings
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 6
BALL_SPEED_Y = 6

# Scores
score1 = 0
score2 = 0

# Create paddles
left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

# Reset ball after score
def reset_ball():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    BALL_SPEED_X *= -1

# Game loop
while True:
    clock.tick(60)

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Paddle Movement ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # --- Ball Movement ---
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Bounce off top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Paddle collision
    if ball.colliderect(left_paddle) and BALL_SPEED_X < 0:
        BALL_SPEED_X *= -1
    if ball.colliderect(right_paddle) and BALL_SPEED_X > 0:
        BALL_SPEED_X *= -1

    # ---------- SCORING ----------
    if ball.left <= 0:
        score2 += 1
        reset_ball()

    if ball.right >= WIDTH:
        score1 += 1
        reset_ball()

    # --- Drawing ---
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores and names
    p1_text = font.render(f"{player1_name}: {score1}", True, WHITE)
    p2_text = font.render(f"{player2_name}: {score2}", True, WHITE)

    WIN.blit(p1_text, (50, 20))
    WIN.blit(p2_text, (WIDTH - p2_text.get_width() - 50, 20))

    pygame.display.flip()
