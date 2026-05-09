import random
import pygame

# make a draw class for all drawing needs
# Make moving platforms class
# make a win condition that brings you to a different section for another level to be drawn

class Draw():

    def __init__(self, screen):
        self.screen = screen

    def background(self):
        self.screen.fill('cyan')

    def floor(self, floor):
        pygame.draw.rect(self.screen, (0, 255, 0), floor)

    def player(self, player):
        pygame.draw.rect(self.screen, (0, 0, 255), player)

    def spikes(self):
        for x in range (200,600,25):
            pygame.draw.polygon(self.screen, (255, 0, 0), [
            (x, 575),
            (x + 12, 550),
            (x + 25, 575)
            ])

class Control():

    def movement(self, player, keys):
        if keys[pygame.K_a]:
            player.x -= 5
        
        if keys[pygame.K_d]:
            player.x += 5

    def jump(self, player, ground, velocity_y, keys):
        if keys[pygame.K_SPACE] and player.bottom == ground.top:
            velocity_y = -10
        return velocity_y
    
    def reset(self, player, keys):
        if keys[pygame.K_r]:
            player.x = 50
            player.y = 500
            print("You are Dead!")


def main():
    pygame.init()
    pygame.display.set_caption("Platform Game")
    clock = pygame.time.Clock()

    player = pygame.Rect(50, 500, 25, 25)
    ground = pygame.Rect(0, 575, 800, 100)

    velocity_y = 0
    gravity = 0.5

    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    draw = Draw(screen)
    control = Control()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        control.movement(player, keys)
        velocity_y = control.jump(player, ground, velocity_y, keys)
        control.reset(player, keys)

        velocity_y += gravity
        player.y += velocity_y

        if player.bottom >= ground.top: #Gravity
            player.bottom = ground.top
            velocity_y = 0

        draw.background()
        draw.floor(ground)
        draw.player(player)
        draw.spikes()

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
