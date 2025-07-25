import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
   
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    field = AsteroidField()


    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill((0, 0, 0))  # Negro

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()   # Actualiza la pantalla
        
        dt = clock.tick(60) / 1000  #limitacióm a 60 fps

if __name__ == "__main__":
    main()
