import pygame
class ScymanWalk(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        super().__init__()
        self.animating=False
        self.sprites =[]
        self.sprites.append(pygame.image.load('media\scyman_walk\scymanwalk0.png'))
        self.sprites.append(pygame.image.load('media\scyman_walk\scymanwalk1.png'))
        self.sprites.append(pygame.image.load('media\scyman_walk\scymanwalk2.png'))
        self.sprites.append(pygame.image.load('media\scyman_walk\scymanwalk3.png'))
        self.current_sprite=0
        self.image=self.sprites[self.current_sprite]
        self.rect=self.image.get_rect()
        self.rect.topleft=[pos_x,pos_y]
    def animate(self):
        self.animating=True
    def update(self,speed):
        if self.animating==True:
            self.current_sprite+=speed
            if int(self.current_sprite)>=len(self.sprites):
                self.current_sprite=0
                self.animating=False
        self.image=self.sprites[int(self.current_sprite)]