import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot

def main():
    pygame.init()
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_fields = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.split()

        


        pygame.Surface.fill(screen,(0,0,0))

        for obj in drawable:
            obj.draw(screen)

        #refreshes screen
        pygame.display.flip()

        #limit framerate to 60 fps
        dt = clock.tick(60) / 1000

        

        
       

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()