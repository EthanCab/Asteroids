import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Negro
        pygame.display.flip()   # Actualiza la pantalla
        
        dt = clock.tick(60) / 1000  #limitacióm a 60 fps

if __name__ == "__main__":
    main()
