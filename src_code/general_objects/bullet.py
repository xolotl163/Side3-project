
import config
import pygame
import math
import utils

class Bullet:
    #cconstructor
    def __init__(self, mov_speed: float, x: float, y: float, width: float, height: float, direction: tuple, appeareance = None ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = utils.angle_to_forward_vector(direction - 90)
        self.appeareance = pygame.image.load(appeareance).convert_alpha()
        self.original_appeareance = self.appeareance
        self.rotation = direction
        self.mov_speed = mov_speed
        self.is_active = True #used to libberate memory during execution

        print("******************************************")
        print("Direction: ", self.direction )
        print("Rotation: ", self.rotation)
        print("******************************************")

        self.rotate(self.rotation)

    #setters and getters

    # general methods to the class
    def draw(self, screen):
        screen.blit(self.appeareance, self.rect)

    def rotate(self, rotation):
        """
        Due to the fact that we are taking the current roration of the player to rotate the bullet,
        we just pass it (the player rotation) as an argument of this function
        """
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
        if self.rect.left < 0:
            self.is_active = False
        if self.rect.right > config.window_width:
            self.is_active = False
        if self.rect.top < 0:
            self.is_active = False
        if self.rect.bottom > config.window_height:
            self.is_active = False
    
    def reposition(self, direction, delta_time):
        self.x = self.x + config.bullet_movement_speed*direction[0]*delta_time
        self.y = self.y + config.bullet_movement_speed*direction[1]*delta_time
        self.rect.x = self.x
        self.rect.y = self.y
        self.check_is_active()