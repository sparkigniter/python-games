import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SHIP_SPEED = 10
BULLET_SPEED = 10
METEOR_SPEED = 5
BULLET_COOLDOWN = 20  # Cooldown frames between bullet firings

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SPACESHIP GAME")

# Load assets
ship_img = pygame.image.load("./assets/ship.png").convert()
ship_rect = ship_img.get_rect()

meteor_imgs = [pygame.transform.scale(pygame.image.load(f"./assets/meteor/Meteor_0{i}.png").convert(), (50, 50))
               for i in range(1, 10)]  # Adjusted to 10 for 9 meteoroids
meteors = []

bullets = []
bullet_img = pygame.Surface((10, 5))  # Create a smaller surface for the bullet
bullet_img.fill((255, 255, 255))  # Fill the bullet surface with white color

# Cooldown variables
bullet_cooldown = 0

# Main game loop
is_quit = False
while not is_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_quit = True

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_rect.y -= SHIP_SPEED
    if keys[pygame.K_DOWN]:
        ship_rect.y += SHIP_SPEED
    if keys[pygame.K_SPACE] and bullet_cooldown == 0:
        # Fire a bullet when spacebar is pressed and cooldown is over
        bullet = bullet_img.get_rect()
        bullet.y = ship_rect.y + ship_rect.height // 2 - bullet.height // 2  # Center bullet vertically
        bullet.x = ship_rect.right  # Position the bullet to the right of the ship
        bullets.append(bullet)
        bullet_cooldown = BULLET_COOLDOWN  # Start cooldown

    # Move bullets
    for bullet in bullets:
        bullet.x += BULLET_SPEED
        # Remove bullets when they go off-screen
        if bullet.right >= SCREEN_WIDTH:
            bullets.remove(bullet)

    # Update bullet cooldown
    if bullet_cooldown > 0:
        bullet_cooldown -= 1

    # Randomly spawn new meteors
    if len(meteors) < 10 and random.random() < 0.01:
        meteor_img = random.choice(meteor_imgs)
        meteor_rect = meteor_img.get_rect()
        meteor_rect.x = SCREEN_WIDTH
        meteor_rect.y = random.randint(0, SCREEN_HEIGHT - meteor_rect.height)
        meteors.append((meteor_rect, meteor_img))


    # Move meteors horizontally towards the left
    for i, (meteor_rect, _) in enumerate(meteors):
        meteor_rect.x -= METEOR_SPEED
        if meteor_rect.right <= 0:
            # Remove meteors that go off-screen
            meteors.pop(i)

    # Check for collision between ship and meteoroids
    for meteor_rect, _ in meteors:
        #ship_rect_collision =  pygame.Rect(ship_rect.left - 50, ship_rect.top , ship_rect.width, ship_rect.right)
        if ship_rect.colliderect(meteor_rect):
            # Game over if ship collides with any meteoroid
            is_quit = True
            break

    # Check for collisions between bullets and meteoroids
    for bullet in bullets[:]:  # Iterate over a copy of the list to avoid issues while removing items
        for meteor_rect, _ in meteors[:]:  # Iterate over a copy of the list to avoid issues while removing items
            if bullet.colliderect(meteor_rect):
                bullets.remove(bullet)
                meteors.remove((meteor_rect, _))
                break

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(ship_img, ship_rect)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    for meteor_rect, meteor_img in meteors:
        screen.blit(meteor_img, meteor_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
