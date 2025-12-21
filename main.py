import pygame
import sys

pygame.init() # Initializes all the pygame modules (sound, video, ect.)

screen = pygame.display.set_mode((1280, 720)) # Creates the game window with a width of 1280 pixels and a height of 720 pixels. The returned screen object is a "Surface" where you will draw everything. 
clock = pygame.time.Clock() # Creates a Clock object to help track time and control the frame rate.
running = True # A boolean variable to control the main game loop.
while running: # Main game loop that continues until 'running' is set to False.
    for event in pygame.event.get(): # Processes all the events in the event queue, such as keyboard and mouse input.
        if event.type == pygame.QUIT: # Checks if the event type is QUIT (e.g., clicking the window's close button).
            running = False # Sets 'running' to False to exit the main game loop.

    screen.fill("black") # Fills the entire screen with black color to clear the previous frame.

    pygame.display.flip() # Updates the full display surface to the screen, making everything drawn visible.
    clock.tick(60) # Pauses the loop to maintain a frame rate of 60 frames per second.

pygame.quit() # Uninitializes all pygame modules and cleans up resources.
sys.exit() # Exits the program cleanly.