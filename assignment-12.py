import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Create paddles using Rects
left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

# Game loop
while True:
    clock.tick(60)  # 60 FPS

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Paddle Movement ---
    keys = pygame.key.get_pressed()

    # Player 1 (Left Paddle) - W/S
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Player 2 (Right Paddle) - Up/Down
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

    # Bounce off left/right walls
    if ball.left <= 0 or ball.right >= WIDTH:
        BALL_SPEED_X *= -1

    # Bounce off paddles
    if ball.colliderect(left_paddle) and BALL_SPEED_X < 0:
        BALL_SPEED_X *= -1
    if ball.colliderect(right_paddle) and BALL_SPEED_X > 0:
        BALL_SPEED_X *= -1

    # --- Drawing ---
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()

