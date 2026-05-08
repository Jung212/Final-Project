import random
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Platform Game")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('blue')
    pygame.quit()

if __name__ == "__main__":
    main()
