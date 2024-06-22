from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)
        
        #Movement
        self.direction = vector(0,0)
        self.speed = 0.1
        
    def input(self):
    
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
            print('right')
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
            print('left')
        self.direction = input_vector
      
        
    
    def move(self):
        self.rect.topleft += self.direction * self.speed
    
    def update(self):
        self.input()
        self.move()