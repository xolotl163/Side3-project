
import config
import pygame
import math
import utils
from utils.observer import Observer


class Obstacle(Observer):
    #cconstructor
    def __init__(self, x: float, y: float, width: float, height: float, appeareance = None, name = "observer"):
        super().__init__(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.HP = 10
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
        if self.HP <= 0:
            self.is_active = False

    def take_damage(self, damage):
        self.HP = self.HP - damage
        self.check_is_active()

    def on_notify(self, event_type: str, data: dict):
        print(f"[Obstacle] Notificación recibida: {event_type}")
        match event_type:
            case "bullet_impact":
                target = data["target"]
                damage = data["damage_inflicted"]
                bullet = data["bullet"]
                position = data["position"]

                if target is self:
                    self.take_damage(damage)
                    if config.dev_mode == True:
                        print(f"[Obstacle] ¡Impacto directo!")
                        print(f"  → Posición: {position}")
                        print(f"  → Daño: {damage}")
                        print(f"  -> HP: {self.HP}")
            case _ :
                print(f"[Obstacle] Evento desconocido: {event_type}")