
import config
import pygame
import math
import utils
from utils.observer import Subject

class Bullet(Subject):
    #cconstructor
    def __init__(self, mov_speed: float, x: float, y: float, width: float, height: float, direction: float, appeareance = None ):
        super().__init__()
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
        self.damage_inflicted = 1
        self.has_impacted = False
        self.is_active = True #used to libberate memory during execution

        """ just for debug
        print("******************************************")
        print("Direction: ", self.direction )
        print("Rotation: ", self.rotation)
        print("******************************************")
        """
        
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

    def check_collisions(self, objects_to_check: list):
        if not self.is_active:
            return False
        
        for object in objects_to_check:
            if not hasattr(object, 'rect'):
                """
                remeber: object bullets has only its rect, that actsas the hitbox at the same time, in the case of the player or enemy object
                the if sentence has to check for the object directly called as hitboxm due tot he fact that these kinfd of objects have the surface
                to its corresponding "texture" or image and the hitbox itself.
                These rules apply int the same way to the obstacle object
                """
                continue
            
            if self.has_impacted == False:
                if self.rect.colliderect(object.rect):
                    self.has_impacted = True
                    self.on_notify(
                        "bullet_impact",
                        {
                            "bullet": self,
                            "target": object,
                            "position": self.rect.center,
                            "damage_inflicted": self.damage_inflicted
                        }
                    )
                    self.is_active = False
                    #print(f"[Bullet] ¡Impacto notificado a {self.observers} observadores!")
            return True
        
        return False