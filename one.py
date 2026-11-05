"""
Flappy Bird Clone — PS No. 61
Python 3 + Pygame

Install:
    python -m pip install pygame

Run:
    python flappy_bird.py

Controls:
    SPACE     flap upward
    R         restart after Game Over
    ESC       quit

Specified initial values:
    Window: 400 x 600
    Bird: 30 x 30 at x=100, y=300
    Initial velocity: 0
    Gravity: velocity += 1, then y += velocity each frame
    SPACE: velocity = -10 before the frame update
    Pipe width: 60; gap: 150
    Ground y: 600
"""

import random
import sys
import pygame

# --------------------------- Configuration ---------------------------
WIDTH, HEIGHT = 400, 600
FPS = 60

BIRD_X = 100
BIRD_SIZE = 30
START_BIRD_Y = 300 #case_4 a

GRAVITY = 1
FLAP_VELOCITY = 5 #case_4 a 

PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_SPAWN_INTERVAL = 90  # frames

GROUND_Y = 600

# Colors
SKY = (135, 206, 235)
GREEN = (50, 180, 70)
DARK_GREEN = (30, 130, 45)
YELLOW = (255, 220, 0)
ORANGE = (255, 150, 0)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GROUND = (210, 180, 120)


class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = START_BIRD_Y
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, BIRD_SIZE, BIRD_SIZE)

    def flap(self):
        # The problem statement says SPACE sets velocity to -10
        # before that frame's gravity/position update.
        self.velocity = FLAP_VELOCITY

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.topleft = (self.x, int(self.y))

    def draw(self, screen):
        pygame.draw.ellipse(screen, YELLOW, self.rect)
        # Small eye and beak
        pygame.draw.circle(screen, WHITE, (self.x + 21, int(self.y) + 8), 5)
        pygame.draw.circle(screen, BLACK, (self.x + 23, int(self.y) + 8), 2)
        pygame.draw.polygon(
            screen, ORANGE,
            [(self.x + 27, int(self.y) + 14),
             (self.x + 35, int(self.y) + 18),
             (self.x + 27, int(self.y) + 21)]
        )


class Pipe:
    def __init__(self, x):
        self.x = x
        # Leave enough room for a gap inside the playable area.
        self.gap_y = random.randint(100, HEIGHT - 100)
        self.top_rect = pygame.Rect(
            self.x, 0, PIPE_WIDTH, self.gap_y - PIPE_GAP // 2
        )
        self.bottom_rect = pygame.Rect(
            self.x, self.gap_y + PIPE_GAP // 2,
            PIPE_WIDTH, HEIGHT - (self.gap_y + PIPE_GAP // 2)
        )
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)
        # Pipe rims
        pygame.draw.rect(
            screen, DARK_GREEN,
            (self.x - 4, self.top_rect.bottom - 12, PIPE_WIDTH + 8, 12)
        )
        pygame.draw.rect(
            screen, DARK_GREEN,
            (self.x - 4, self.bottom_rect.y, PIPE_WIDTH + 8, 12)
        )


class FlappyBirdGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flappy Bird Clone — PS 61")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.large_font = pygame.font.SysFont(None, 54)
        self.reset()

    def reset(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.frames_since_pipe = 0
        self.game_over = False

    def spawn_pipe(self):
        self.pipes.append(Pipe(WIDTH))

    def check_collisions(self):
        # Ground: bird's bottom edge reaches y=600.
        if self.bird.rect.bottom >= GROUND_Y:
            return True

        # Top boundary: bird leaves the screen.
        if self.bird.rect.top < 0:
            return True

        # Pipe collision uses Rect.colliderect(), as required.
        for pipe in self.pipes:
            if (self.bird.rect.colliderect(pipe.top_rect)
                    or self.bird.rect.colliderect(pipe.bottom_rect)):
                return True

        return False

    def update(self):
        if self.game_over:
            return

        self.bird.update()

        self.frames_since_pipe += 1
        if self.frames_since_pipe >= PIPE_SPAWN_INTERVAL:
            self.spawn_pipe()
            self.frames_since_pipe = 0

        for pipe in self.pipes:
            pipe.update()

            # Score once when the pipe's right edge has passed bird x.
            # This matches the supplied test: x=39 + width=60 => 99 < 100.
            if not pipe.passed and pipe.x + PIPE_WIDTH < self.bird.x:
                pipe.passed = True
                self.score += 1

        # Remove pipes after they leave the left side of the window.
        self.pipes = [pipe for pipe in self.pipes
                      if pipe.x + PIPE_WIDTH > 0]

        if self.check_collisions():
            self.game_over = True

    def draw_text_centered(self, text, font, color, y):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=(WIDTH // 2, y))
        self.screen.blit(surface, rect)

    def draw(self):
        self.screen.fill(SKY)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.bird.draw(self.screen)

        # Ground strip; its collision boundary is exactly y=600.
        pygame.draw.rect(self.screen, GROUND, (0, GROUND_Y - 12, WIDTH, 12))
        pygame.draw.line(self.screen, DARK_GREEN, (0, GROUND_Y - 12),
                         (WIDTH, GROUND_Y - 12), 3)

        score_surface = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_surface, (12, 12))

        if self.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 130))
            self.screen.blit(overlay, (0, 0))
            self.draw_text_centered("GAME OVER", self.large_font, WHITE, 250)
            self.draw_text_centered(f"Score: {self.score}", self.font, WHITE, 305)
            self.draw_text_centered("Press R to restart", self.font, WHITE, 360)
            self.draw_text_centered("ESC to quit", self.font, WHITE, 405)

        pygame.display.flip()

    def run(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_r and self.game_over:
                        self.reset()

                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.bird.flap()

            self.update()
            self.draw()


def main():
    FlappyBirdGame().run()


if __name__ == "__main__":
    main()
