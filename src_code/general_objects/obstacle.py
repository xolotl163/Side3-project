
import config
import pygame
import math
import utils

class Obstacle:
    #cconstructor
    def __init__(self, x: float, y: float, width: float, height: float, appeareance = None ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.appeareance = pygame.image.load(appeareance).convert_alpha()
        self.original_appeareance = self.appeareance
        self.is_active = True #used to libberate memory during execution
        
    #setters and getters

    # general methods to the class
    def draw(self, screen):
        screen.blit(self.appeareance, self.rect)

    def rotate(self, rotation):
        #rotation is given in degrees

        old_center = self.rect.center
        # rotate the image
        self.appeareance = pygame.transform.rotate(self.original_appeareance, rotation)
        #update the rect
        self.rect = self.appeareance.get_rect(center=(old_center))

        #sinc the rotation with our x,y psotion to create
        #the new top left position
        self.x = self.rect.x
        self.y = self.rect.y

    def check_is_active(self):
        pass