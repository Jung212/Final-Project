import random
import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Platform Game")
    clock = pygame.time.Clock()

    player = pygame.Rect(100, 100, 25, 25)
    ground = pygame.Rect(0, 575, 800, 100)

    velocity_y = 0
    gravity = 0.5

    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.x -= 5

        if keys[pygame.K_d]:
            player.x += 5

        if keys[pygame.K_SPACE] and player.bottom == ground.top:
            velocity_y = -12

        velocity_y += gravity
        player.y += velocity_y

        if player.bottom >= ground.top:
            player.bottom = ground.top
            velocity_y = 0


        screen.fill('cyan')
        pygame.draw.rect(screen, (0, 255, 0), ground) 
        pygame.draw.rect(screen, (255, 0, 0), player)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
