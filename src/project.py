import pygame

class Draw():

    def __init__(self, screen):
        self.screen = screen

    def background(self):
        self.screen.fill('cyan')

    def floor(self, floor):
        pygame.draw.rect(self.screen, (0, 255, 0), floor)

    def platform2(self, platform2):
        pygame.draw.rect(self.screen, (255, 200, 0), platform2)

    def moving1(self, moving1):
        pygame.draw.rect(self.screen, (255, 75, 255), moving1)

    def player(self, player):
        pygame.draw.rect(self.screen, (0, 0, 255), player)

    def spikes(self, spikes):
        for x in range (spikes.x, spikes.x + spikes.width, 25):
            pygame.draw.polygon(self.screen, (255, 0, 0), [
            (x, 575),
            (x + 12, 550),
            (x + 25, 575)
            ])

    def goal(self, goal):
        pygame.draw.rect(self.screen, (0, 0, 0), goal)

    def win(self):

        font = pygame.font.SysFont("Comic Sans MS", 80, bold=True)

        text = font.render("You Win!", True, (0, 255, 0))

        text_rect = text.get_rect(center=(400, 300))

        self.screen.blit(text, text_rect)

class Control():

    def movement(self, player, keys):
        if keys[pygame.K_a]:
            player.x -= 5
        
        if keys[pygame.K_d]:
            player.x += 5

    def jump(self, grounded, velocity_y, keys):
        if keys[pygame.K_SPACE] and grounded:
            velocity_y = -10
        return velocity_y
    
    def reset(self, player, keys):
        if keys[pygame.K_r]:
            player.x = 50
            player.y = 500
            print("You are Dead!")

class Level():

    def __init__(self):
        self.level = 1

    def next_level(self, player, goal):

        if player.colliderect(goal):

            self.level += 1

            player.x = 50
            player.y = 500

            print("Level:", self.level)
    
    def moving_platform(self, moving1, platform_speed):
        if self.level == 1:

            moving1.y += platform_speed

            if moving1.top <= 300:
               platform_speed = 2

            if moving1.bottom >= 575:
                platform_speed = -2

        if self.level == 2:

            moving1.x += platform_speed

            if moving1.left <= 100:
                platform_speed = 2

            if moving1.right >= 700:
                platform_speed = -2

        return platform_speed

        


def main():
    pygame.init()
    pygame.display.set_caption("Platform Game")
    clock = pygame.time.Clock()

    player = pygame.Rect(50, 500, 25, 25)
    ground = pygame.Rect(0, 575, 800, 100)
    spikes = pygame.Rect(200, 550, 400, 25)
    moving1 = pygame.Rect(200, 400, 100, 20)
    platform2 = pygame.Rect(450, 350, 100, 20)
    goal = pygame.Rect(750, 500, 40, 40)

    platform_speed = 3
    velocity_y = 0
    gravity = 0.5

    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    draw = Draw(screen)
    control = Control()
    level = Level()
    running = True
    grounded = False

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        control.movement(player, keys)
        velocity_y = control.jump(grounded, velocity_y, keys)
        control.reset(player, keys)
        level.next_level(player,goal)

        if level.level == 2:

            platform2.width = 0
            platform2.height = 0

            spikes.x = 100
            spikes.width = 600

            moving1.y = 500

        if level.level == 3:

            platform2.width = 400
            platform2.height = 20
            platform2.x = 200
            platform2.y = 500

            moving1.width = 0
            moving1.height = 0

            goal.width = 0
            goal.height = 0

        grounded = False

        velocity_y += gravity
        player.y += velocity_y

        platform_speed = level.moving_platform(moving1, platform_speed)

        if player.bottom >= ground.top: #Gravity
            player.bottom = ground.top
            velocity_y = 0
            grounded = True

        if player.colliderect(moving1) and velocity_y >= 0:

            player.bottom = moving1.top

            velocity_y = 0

            grounded = True

            player.y += platform_speed

        if player.colliderect(platform2) and velocity_y >= 0:

            player.bottom = platform2.top

            velocity_y = 0

            grounded = True

        if player.colliderect(spikes):
            player.x = 50
            player.y = 500
            print("spikes are sharp!")

        draw.background()
        draw.floor(ground)
        draw.moving1(moving1)
        draw.platform2(platform2)
        draw.player(player)
        draw.spikes(spikes)
        draw.goal(goal)

        if level.level == 3:
            draw.win()

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
