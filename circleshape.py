import pygame

# clase base
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def colliding(self, other): #calcula la distancia entre el centro y un extremo de dos circulos, si es menor a la suma de los dos radios, devuelve true y el programa se cierra
        return self.position.distance_to(other.position) <= self.radius + other.radius


    def draw(self, screen):
        pass

    def update(self, dt):
        pass