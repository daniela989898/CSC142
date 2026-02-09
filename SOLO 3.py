import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Click the Ball Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

ball_image = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(ball_image, (255, 0, 0), (25, 25), 25)
ball_rect = ball_image.get_rect()
ball_rect.x = random.randint(0, window_width - ball_rect.width)
ball_rect.y = random.randint(0, window_height - ball_rect.height)

success_sound = pygame.mixer.Sound("assets/sound.wav")

xSpeed = 3
ySpeed = 3
score = 0
game_over = False
game_start = pygame.time.get_ticks()

def draw_text(surface, text, x, y, color, font_size=24):
    font = pygame.font.SysFont(None, font_size)
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surf, text_rect)

running = True
while running:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if ball_rect.collidepoint(event.pos):
                score += 1
                success_sound.play()
                ball_rect.x = random.randint(0, window_width - ball_rect.width)
                ball_rect.y = random.randint(0, window_height - ball_rect.height)
                xSpeed = (abs(xSpeed) + random.randint(1,5)) * (1 if xSpeed > 0 else -1)
                ySpeed = (abs(ySpeed) + random.randint(1,5)) * (1 if ySpeed > 0 else -1)

    if not game_over:
        ball_rect.x += xSpeed
        ball_rect.y += ySpeed
        if ball_rect.left < 0 or ball_rect.right > window_width:
            xSpeed = -xSpeed
        if ball_rect.top < 0 or ball_rect.bottom > window_height:
            ySpeed = -ySpeed

    draw_text(window, f"Score: {score}", 10, 10, WHITE, 30)

    if score >= 5 and not game_over:
        game_over = True
        time_taken = (pygame.time.get_ticks() - game_start) / 1000

    if game_over:
        draw_text(window, f"Game Over! Time: {time_taken:.2f}s", window_width//4, window_height//2, YELLOW, 40)
    else:
        window.blit(ball_image, ball_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()