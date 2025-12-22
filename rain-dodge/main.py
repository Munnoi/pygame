import pygame
import time
import random

WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Load the background image and scale it to fit the window dimensions
BG = pygame.transform.scale(pygame.image.load('bg.jpeg'), (WIDTH, HEIGHT)) # Loads the image to the variable 'BG'.

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

def draw(player):
    # Draw the background image at position (0, 0)
    WIN.blit(BG, (0, 0))
    # Draw the player rectangle on the window
    pygame.draw.rect(WIN, 'red', player)
    # Update the display to show the changes
    pygame.display.update()

def main():
    running = True

    # Initialize the player rectangle at the bottom of the screen
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    while running:
        # Limit the loop to run at 60 frames per second
        clock.tick(60)

        # Handle events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Get a dictionary of all keys currently pressed
        keys = pygame.key.get_pressed()
        # Move the player left if the left arrow key is pressed and within bounds
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        # Move the player right if the right arrow key is pressed and within bounds
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()