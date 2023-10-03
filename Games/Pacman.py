import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pac-Man")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Define constants for fullscreen resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Define constants and variables
pacman_x = 100
pacman_y = 100
pacman_speed = 5
pacman_radius = 20
pacman_mouth = 0




# Define maze walls
maze_walls = [
    (0, 0), (SCREEN_WIDTH, 0), (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT),
    (80, 80), (120, 80), (160, 80), (200, 80), (240, 80), (280, 80), (320, 80),
    (360, 80), (400, 80), (440, 80), (480, 80), (520, 80), (560, 80), (600, 80),
    (640, 80), (680, 80), (720, 80), (760, 80), (800, 80), (840, 80), (880, 80),
    (920, 80), (960, 80), (1000, 80), (1040, 80), (1080, 80), (1120, 80), (1160, 80),
    (1200, 80), (1240, 80), (1280, 80), (1320, 80), (1360, 80), (1400, 80), (1440, 80),
    (1480, 80), (1520, 80), (1560, 80), (1600, 80), (1640, 80), (1680, 80), (1720, 80),
    (1760, 80), (1800, 80), (1840, 80),
    # ... Continue adding more walls
]

# Define boundary walls around orbs
for x in range(40, SCREEN_WIDTH, 40):
    maze_walls.append((x, 0))
    maze_walls.append((x, SCREEN_HEIGHT))
for y in range(40, SCREEN_HEIGHT, 40):
    maze_walls.append((0, y))
    maze_walls.append((SCREEN_WIDTH, y))

# Create additional maze walls for a more complex layout
# Feel free to adjust these coordinates to design your maze
additional_maze_walls = [
    (360, 200), (360, 240), (360, 280), (360, 320), (360, 360), (360, 400),
    (360, 440), (400, 440), (440, 440), (480, 440), (520, 440), (560, 440),
    (600, 440), (600, 400), (600, 360), (600, 320), (600, 280), (600, 240),
    (600, 200), (160, 360), (200, 360), (240, 360), (280, 360), (280, 320),
    (280, 280), (280, 240), (280, 200)
]

maze_walls.extend(additional_maze_walls)

# Define enemies
enemies = []
for _ in range(4):
    enemy_x = random.randint(40, SCREEN_WIDTH - 40)
    enemy_y = random.randint(40, SCREEN_HEIGHT - 40)
    enemies.append((enemy_x, enemy_y))

enemy_speed = 1

# Define collectible orbs
orbs = []
for x in range(40, SCREEN_WIDTH, 40):
    for y in range(40, SCREEN_HEIGHT, 40):
        orbs.append((x, y))

# Define fruits
fruits = []
fruit_spawn_timer = 0
fruit_spawn_interval = 20 * 60  # 20 seconds in frames

# Ensure Pac-Man doesn't spawn inside a wall
while any(wall[0] < pacman_x < wall[0] + 40 and wall[1] < pacman_y < wall[1] + 40 for wall in maze_walls):
    pacman_x = random.randint(40, SCREEN_WIDTH - 40)
    pacman_y = random.randint(40, SCREEN_HEIGHT - 40)

# Game over flag
game_over = False

# Player score
score = 0

# Font for game over text and points display
font = pygame.font.Font(None, 36)

# Clock object to control frame rate
clock = pygame.time.Clock()

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    new_pacman_x = pacman_x
    new_pacman_y = pacman_y

    if keys[pygame.K_UP]:
        new_pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        new_pacman_y += pacman_speed
    if keys[pygame.K_LEFT]:
        new_pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        new_pacman_x += pacman_speed

    # Check collision with maze walls
    hit_wall = False
    for wall in maze_walls:
        if (new_pacman_x + pacman_radius > wall[0] and
            new_pacman_x - pacman_radius < wall[0] + 40 and
            new_pacman_y + pacman_radius > wall[1] and
            new_pacman_y - pacman_radius < wall[1] + 40):
            hit_wall = True
            break

    if not hit_wall:
        pacman_x = new_pacman_x
        pacman_y = new_pacman_y

    # Move enemies
    for enemy_idx, enemy in enumerate(enemies):
        enemy_x, enemy_y = enemy
        move_direction = random.choice(['x', 'y'])

        if move_direction == 'x':
            if enemy_x < pacman_x:
                enemy_x += enemy_speed
            elif enemy_x > pacman_x:
                enemy_x -= enemy_speed
        else:  # move_direction == 'y'
            if enemy_y < pacman_y:
                enemy_y += enemy_speed
            elif enemy_y > pacman_y:
                enemy_y -= enemy_speed

        enemies[enemy_idx] = (enemy_x, enemy_y)

        # Check collision with enemy
        if (abs(pacman_x - enemy_x) < pacman_radius + 15 and
                abs(pacman_y - enemy_y) < pacman_radius + 15):
            game_over = True

    # Check collision with orbs
    for orb in orbs:
        orb_x, orb_y = orb
        if (abs(pacman_x - orb_x) < pacman_radius and
                abs(pacman_y - orb_y) < pacman_radius):
            score += 50
            orbs.remove(orb)

    # Check collision with fruits
    for fruit in fruits:
        fruit_x, fruit_y = fruit
        if (abs(pacman_x - fruit_x) < pacman_radius and
                abs(pacman_y - fruit_y) < pacman_radius):
            score += 200
            fruits.remove(fruit)

    # Spawn random fruit
    fruit_spawn_timer += 1
    if fruit_spawn_timer >= fruit_spawn_interval:
        fruit_x = random.randint(40, SCREEN_WIDTH - 40)
        fruit_y = random.randint(40, SCREEN_HEIGHT - 40)
        fruits.append((fruit_x, fruit_y))
        fruit_spawn_timer = 0

    # Clear the screen
    screen.fill(BLACK)

    # Draw maze walls
    for wall in maze_walls:
        pygame.draw.rect(screen, BLUE, (wall[0], wall[1], 40, 40))

    # Draw collectible orbs
    for orb in orbs:
        pygame.draw.circle(screen, WHITE, orb, 5)

    # Draw fruits
    for fruit in fruits:
        pygame.draw.circle(screen, RED, fruit, 10)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.circle(screen, RED, enemy, 15)

    # Draw Pac-Man
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)
    pygame.draw.polygon(screen, BLACK, [(pacman_x, pacman_y),
                                        (pacman_x + pacman_radius, pacman_y - pacman_mouth),
                                        (pacman_x + pacman_radius, pacman_y + pacman_mouth)])

    # Draw points display
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # Update the screen
    pygame.display.update()

    # Animate Pac-Man's mouth
    pacman_mouth = (pacman_mouth + 1) % pacman_radius

    # Control frame rate
    clock.tick(60)  # Limit the frame rate to 60 FPS

    # Check for game over
    if len(orbs) == 0 and len(fruits) == 0:
        game_over = True

# Clear the screen
screen.fill(BLACK)

# Display final score
final_score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(final_score_text, (300, 250))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.delay(2000)
pygame.quit()
sys.exit()
