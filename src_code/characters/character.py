
import config
import pygame
import math

class Character:
    #appeareance is the path to the image of the character, it should be a string
    def __init__(self, x = 0.0, y = 0.0, width = 1.0, height = 1.0, appeareance = None):
        
        self.x = x #current rect position of the surface
        self.y = y #current rect position of the surface
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.forward_vector = (0, -1)  # this is the initial forward vector of the character, it points upwards
        
        #appeareance - load the image and convert it for better performance, convert_alpha() is used to preserve the transparency of the image
        self.appeareance = pygame.image.load(appeareance).convert_alpha()
        
        #original_appeareance is used to store the original image of the character, 
        #so we can rotate it without losing quality, if we rotate the already rotated image, it will lose quality and become blurry over time
        self.original_appeareance = self.appeareance

        #trotation - this is the current rotation of the character, it starts at 0 degrees
        self.rotation = 0     
    
        print("****************************************************")
        print("Character created with the following parameters: ")
        print("Character created at position: ", self.rect.x, self.rect.y)
        print("Character created with width: ", self.width)
        print("Character created with height: ", self.height)
        print("Character created with rect: ", self.rect)
        print("Character dimensiones: ", self.x+self.width, self.y+self.height)
        print("Character created with center: ", self.rect.center[0], self.rect.center[1])
        print("Character created with rotation: ", self.rotation)
        print("Character created with appeareance: ", appeareance)
        print("Character created with forward vector: ", self.forward_vector)
        print("****************************************************")

    def draw(self, screen):
        screen.blit(self.appeareance, self.rect)

class Player(Character):
    def __init__(self, x, y, width, height, appeareance):
        super().__init__(x, y, width, height, appeareance)

    def move(self, keys, delta_time = 1.0):
        #if no delta is given, we just use the default value of 1.0
        #it does not affect the movement of the player, but it allows us to use the same function for both fixed and variable time steps, if we want to use a fixed time step, we can just call this function with a fixed delta time, for example: player.move(keys, 0.016) for 60 FPS
        speed = config.player_movement_speed * delta_time

        if keys[pygame.K_w]:
            if self.rect.top > 0:  # move up
                self.y -= speed
        if keys[pygame.K_s]:
            if self.rect.bottom < config.window_height:  # move down
                self.y += speed
        
        if keys[pygame.K_a]: 
            if self.rect.left > 0:  # move left
                self.x -= speed
        if keys[pygame.K_d]:
            if self.rect.right < config.window_width:  # move right
                self.x += speed

        self.rect.x = self.x
        self.rect.y = self.y
    
    #auxiliar method
    def reposition(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def rotate(self, mouse_pos, delta_time = 1.0):

        """
        This method rotates the characaters image by a given angle.
        The angles is "attached" to the mouse position, so the character will always look at the mouse cursor.
        The players forward vector is also updated to reflect the new direction the character is facing.

        We use the delta time to make the rotation smooth and frame rate independent, 
        if we want to use a fixed time step, we can just call this function with a fixed delta time, 
        for example: player.rotate(mouse_pos, 0.016) for 60 FPS    
        """
        #save the original center before rotating
        old_center = self.rect.center

        #calculate the angle between the character and the mouse position using atan2, 
        # this will give us the angle in radians, we can then convert it to degrees
        dx = mouse_pos[0] - self.rect.center[0]
        dy = mouse_pos[1] - self.rect.center[1]
        angle_rad = math.atan2(dy, dx)

        self.forward_vector = (math.cos(angle_rad), math.sin(angle_rad))
        angle_degrees = math.degrees(angle_rad) + 90  # add 90 degrees to make the character face the mouse cursor

        # rotate the image
        self.appeareance = pygame.transform.rotate(self.original_appeareance, -angle_degrees)

        #update the rect
        self.rect = self.appeareance.get_rect(center=(old_center))

        #sinc the rotation with our x,y psotion to create
        #the new top left position
        self.x = self.rect.x
        self.y = self.rect.y