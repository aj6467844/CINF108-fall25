import pygame
import sys

pygame.init()

# -------------------- WINDOW --------------------
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK = (50, 50, 50)

font = pygame.font.SysFont("Arial", 32)
bigfont = pygame.font.SysFont("Arial", 60)

# -------------------- GAME CONSTANTS --------------------
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 6
AI_SPEED = 5
ai_difficulty = "Normal"  # "Easy", "Normal", "Hard"

BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
BALL_SPEED_INCREMENT = 1.05
MAX_BALL_SPEED = 12

WIN_SCORE = 7

# -------------------- GAME OBJECTS --------------------
left_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2,
                          PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20 - PADDLE_WIDTH,
                           HEIGHT // 2 - PADDLE_HEIGHT // 2,
                           PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2,
                   HEIGHT // 2 - BALL_SIZE // 2,
                   BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

# -------------------- GLOBAL GAME STATE --------------------
player1_name = ""
player2_name = ""
ai_mode = False
score1 = 0
score2 = 0
game_running = False
game_paused = False
winner = None
total_points_for_speed = 0
input_active = True  # input mode for GUI

# Menu button — moved to bottom-center
menu_btn = pygame.Rect(WIDTH // 2 - 70, HEIGHT - 48, 140, 36)

# Difficulty buttons — moved to top-center
_btn_w, _btn_h, _spacing = 84, 34, 8
diff_labels = ["Easy", "Normal", "Hard"]
btn_y = 15  # top area (below any title / safe from score text)
_total_w = len(diff_labels) * _btn_w + (len(diff_labels) - 1) * _spacing
_start_x = WIDTH // 2 - _total_w // 2
diff_buttons = [
    pygame.Rect(_start_x + i * (_btn_w + _spacing), btn_y, _btn_w, _btn_h)
    for i in range(len(diff_labels))
]

# -------------------- HELPERS --------------------
def set_ai_speed_from_difficulty():
    global AI_SPEED
    mapping = {"Easy": 3, "Normal": 5, "Hard": 8}
    AI_SPEED = mapping.get(ai_difficulty, 5)

def draw_text_centered(surface, text, font_, color, y):
    """Draw text centered horizontally at y"""
    render = font_.render(text, True, color)
    surface.blit(render, (WIDTH // 2 - render.get_width() // 2, y))

def draw_menu_button():
    pygame.draw.rect(WIN, DARK, menu_btn)
    pygame.draw.rect(WIN, WHITE, menu_btn, 2)
    t = font.render("Main Menu", True, WHITE)
    WIN.blit(t, (menu_btn.x + (menu_btn.width - t.get_width()) // 2,
                 menu_btn.y + (menu_btn.height - t.get_height()) // 2))

def draw_difficulty_buttons():
    """Draw clickable difficulty buttons (visible when AI is active)."""
    for rect, label in zip(diff_buttons, diff_labels):
        selected = (label == ai_difficulty)
        bg = (80, 80, 80) if not selected else (200, 200, 200)
        fg = WHITE if not selected else BLACK
        pygame.draw.rect(WIN, bg, rect)
        pygame.draw.rect(WIN, WHITE, rect, 2)
        t = font.render(label, True, fg)
        WIN.blit(t, (rect.x + (rect.width - t.get_width()) // 2,
                     rect.y + (rect.height - t.get_height()) // 2))

# -------------------- START SCREEN --------------------
def start_screen_gui():
    """GUI input for player names and optional AI mode + difficulty selection."""
    global player1_name, player2_name, ai_mode, ai_difficulty
    set_ai_speed_from_difficulty()

    input_box1 = pygame.Rect(WIDTH//2 - 150, 220, 300, 40)
    input_box2 = pygame.Rect(WIDTH//2 - 150, 300, 300, 40)

    color_inactive = GRAY
    color_active = WHITE
    color1 = color_inactive
    color2 = color_inactive

    active1 = False
    active2 = False

    text1 = ""
    text2 = ""

    running = True
    while running:
        WIN.fill(BLACK)

        # ----- INSTRUCTIONS -----
        draw_text_centered(WIN, "Enter Player 1 Name:", font, WHITE, 160)
        draw_text_centered(WIN, "Enter Player 2 Name (leave blank for AI):", font, WHITE, 260)
        draw_text_centered(WIN, f"AI Difficulty: {ai_difficulty}  (press 1-Easy 2-Normal 3-Hard)", font, WHITE, 340)
        draw_text_centered(WIN, "Click a box to type. Press ENTER to start!", font, WHITE, 380)

        # ----- DRAW INPUT BOXES -----
        pygame.draw.rect(WIN, color1, input_box1, 2)
        pygame.draw.rect(WIN, color2, input_box2, 2)

        # ----- DRAW TEXT INSIDE BOXES -----
        txt_surface1 = font.render(text1, True, WHITE)
        txt_surface2 = font.render(text2 if text2.strip() != "" else "", True, WHITE)

        WIN.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        WIN.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))

        pygame.display.update()

        # ----- EVENT HANDLING -----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Select active input field
                active1 = input_box1.collidepoint(event.pos)
                active2 = input_box2.collidepoint(event.pos)
                color1 = color_active if active1 else color_inactive
                color2 = color_active if active2 else color_inactive

            if event.type == pygame.KEYDOWN:
                # difficulty keys
                if event.key == pygame.K_1:
                    ai_difficulty = "Easy"
                    set_ai_speed_from_difficulty()
                elif event.key == pygame.K_2:
                    ai_difficulty = "Normal"
                    set_ai_speed_from_difficulty()
                elif event.key == pygame.K_3:
                    ai_difficulty = "Hard"
                    set_ai_speed_from_difficulty()

                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode

                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode

                # ENTER → START GAME
                if event.key == pygame.K_RETURN:
                    player1_name = text1 if text1.strip() else "Player 1"

                    if text2.strip() == "":
                        player2_name = "AI"
                        ai_mode = True
                    else:
                        player2_name = text2
                        ai_mode = False

                    running = False

# -------------------- RESET / DRAW / GAME LOGIC --------------------
def reset_ball():
    """Centers the ball and reverses direction"""
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    BALL_SPEED_X = -abs(BALL_SPEED_X) if BALL_SPEED_X < 0 else abs(BALL_SPEED_X)

def reset_game():
    """Resets everything including scores and paddles"""
    global score1, score2, winner, game_running, BALL_SPEED_X, BALL_SPEED_Y, total_points_for_speed
    score1 = 0
    score2 = 0
    winner = None
    total_points_for_speed = 0

    left_paddle.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    right_paddle.y = HEIGHT // 2 - PADDLE_HEIGHT // 2

    BALL_SPEED_X = 4 if BALL_SPEED_X > 0 else -4
    BALL_SPEED_Y = 4 if BALL_SPEED_Y > 0 else -4
    reset_ball()
    game_running = True

def draw_center_message(text):
    msg = bigfont.render(text, True, WHITE)
    WIN.blit(msg, (WIDTH // 2 - msg.get_width() // 2,
                   HEIGHT // 2 - msg.get_height() // 2))

def pause_screen():
    draw_center_message("PAUSED")
    pygame.display.update()

def handle_paddle_movement():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    if not ai_mode:
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED
    else:
        # AI movement using AI_SPEED
        if ball.centery > right_paddle.centery and right_paddle.bottom < HEIGHT:
            right_paddle.y += min(AI_SPEED, ball.centery - right_paddle.centery)
        elif ball.centery < right_paddle.centery and right_paddle.top > 0:
            right_paddle.y -= min(AI_SPEED, right_paddle.centery - ball.centery)

def move_ball():
    global BALL_SPEED_X, BALL_SPEED_Y, score1, score2, winner, game_running, total_points_for_speed

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Bounce top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Paddle collisions
    if ball.colliderect(left_paddle) and BALL_SPEED_X < 0:
        BALL_SPEED_X *= -1
    if ball.colliderect(right_paddle) and BALL_SPEED_X > 0:
        BALL_SPEED_X *= -1

    # Scoring
    scored = False
    if ball.left <= 0:
        score2 += 1
        scored = True
        reset_ball()
    if ball.right >= WIDTH:
        score1 += 1
        scored = True
        reset_ball()

    # Increase speed every 3 total points
    if scored:
        total_points_for_speed += 1
        if total_points_for_speed % 3 == 0:
            BALL_SPEED_X *= BALL_SPEED_INCREMENT
            BALL_SPEED_Y *= BALL_SPEED_INCREMENT

        # Limit speed
        BALL_SPEED_X = max(-MAX_BALL_SPEED, min(BALL_SPEED_X, MAX_BALL_SPEED))
        BALL_SPEED_Y = max(-MAX_BALL_SPEED, min(BALL_SPEED_Y, MAX_BALL_SPEED))

    # Win detection
    if score1 >= WIN_SCORE:
        winner = player1_name
        game_running = False
    elif score2 >= WIN_SCORE:
        winner = player2_name
        game_running = False

def draw():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    p1 = font.render(f"{player1_name}: {score1}", True, WHITE)
    p2 = font.render(f"{player2_name}: {score2}", True, WHITE)
    WIN.blit(p1, (50, 20))
    WIN.blit(p2, (WIDTH - p2.get_width() - 50, 20))

    # show clickable difficulty buttons at top-center when AI is active
    if ai_mode:
        draw_difficulty_buttons()

    # draw menu button (bottom-center)
    draw_menu_button()
    pygame.display.flip()

# -------------------- MAIN LOOP --------------------
start_screen_gui()
set_ai_speed_from_difficulty()
reset_game()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                game_paused = not game_paused
            if event.key == pygame.K_r and winner:
                reset_game()
            # runtime difficulty change via keys 1/2/3
            if event.key == pygame.K_1:
                ai_difficulty = "Easy"; set_ai_speed_from_difficulty()
            elif event.key == pygame.K_2:
                ai_difficulty = "Normal"; set_ai_speed_from_difficulty()
            elif event.key == pygame.K_3:
                ai_difficulty = "Hard"; set_ai_speed_from_difficulty()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # clickable main menu button (lower-right)
            if menu_btn.collidepoint(event.pos):
                start_screen_gui()
                set_ai_speed_from_difficulty()
                reset_game()

            # clickable difficulty buttons (runtime change)
            for rect, label in zip(diff_buttons, diff_labels):
                if rect.collidepoint(event.pos):
                    ai_difficulty = label
                    set_ai_speed_from_difficulty()
                    break

    if game_paused:
        pause_screen()
        continue

    if winner:
        WIN.fill(BLACK)
        draw_center_message(f"{winner} Wins! Press R to Restart")
        pygame.display.update()
        continue

    handle_paddle_movement()
    move_ball()
    draw()
