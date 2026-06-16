import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dancing Heart Game")

# Clock
clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Draw a heart shape
def draw_heart(surface, x, y, size, color):
    points = []
    for t in range(0, 360, 1):
        angle = math.radians(t)
        # Heart equation
        px = size * 16 * math.sin(angle) ** 3
        py = -size * (13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle))
        points.append((x + px, y + py))
    pygame.draw.polygon(surface, color, points)

# Game loop
t = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Make heart "dance" (scale up and down)
    scale = 10 + 2 * math.sin(t)
    draw_heart(screen, WIDTH//2, HEIGHT//2, scale, RED)

    # Update display
    pygame.display.flip()
    clock.tick(60)
    t+=0.1