import pygame
import math
import random

pygame.init()

# Окно
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart + Fireworks")

clock = pygame.time.Clock()

# Цвета
RED = (255, 60, 100)
PINK = (255, 120, 180)
WHITE = (255, 255, 255)
BG = (15, 15, 25)

# Шрифт
font = pygame.font.SysFont("Arial", 50, bold=True)

# -------- Сердце --------
def draw_heart(surface, x, y, scale):
    points = []
    for t in range(0, 360):
        t = math.radians(t)
        hx = 16 * math.sin(t) ** 3
        hy = -(13 * math.cos(t) - 5 * math.cos(2*t)
               - 2 * math.cos(3*t) - math.cos(4*t))
        points.append((x + hx * scale, y + hy * scale))
    
    pygame.draw.polygon(surface, PINK, points)
    pygame.draw.polygon(surface, RED, points, 4)

# -------- Салют --------
particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 3)
        self.life = random.randint(30, 60)
        self.color = random.choice([
            (255, 100, 150),
            (255, 150, 200),
            (255, 200, 220)
        ])

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.life -= 1

    def draw(self, surface):
        if self.life > 0:
            alpha = int(255 * (self.life / 60))
            surf = pygame.Surface((4, 4), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), (2, 2), 2)
            surface.blit(surf, (self.x, self.y))

# -------- Главный цикл --------
running = True
time = 0

while running:
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Случайный запуск салюта (редко, чтобы не мешал)
    if random.random() < 0.05:
        x = random.randint(100, WIDTH - 100)
        y = random.randint(50, HEIGHT - 200)
        for _ in range(20):
            particles.append(Particle(x, y))

    # Обновление салюта
    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.life <= 0:
            particles.remove(p)

    # Пульсация сердца
    scale = 10 + math.sin(time) * 1.5

    draw_heart(screen, WIDTH // 2, HEIGHT // 2, scale)

    # Текст
    text = font.render("AMINA", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)
    time += 0.05

pygame.quit()