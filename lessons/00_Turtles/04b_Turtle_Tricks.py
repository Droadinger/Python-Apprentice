import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Flight Simulator")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load plane image
plane_img = pygame.image.load('plane.png')  # Replace with your own image file
plane_rect = plane_img.get_rect()
plane_speed = 5

# Game loop
clock = pygame.time.Clock()

def handle_input(plane_rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plane_rect.x -= plane_speed
    if keys[pygame.K_RIGHT]:
        plane_rect.x += plane_speed
    if keys[pygame.K_UP]:
        plane_rect.y -= plane_speed
    if keys[pygame.K_DOWN]:
        plane_rect.y += plane_speed

def draw_window(plane_rect):
    screen.fill(BLUE)  # Set background color to blue
    screen.blit(plane_img, plane_rect)  # Draw plane on screen
    pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    handle_input(plane_rect)
    draw_window(plane_rect)

    clock.tick(60)  # FPS (frames per second)


