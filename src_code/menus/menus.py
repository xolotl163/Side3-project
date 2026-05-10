
import config
import pygame

class Button:
    def __init__(self, x, y, width, height, text, color = "white"):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 30)
        self.text = text
        self.color = color

    def draw(self, screen):
        #draw button rectangle
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 2)

        #draw button text
        text_surface = self.font.render(self.text, True, "black")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Menu:
    #construtor
    def __init__(self, name = None, id = None):
        self.name = name
        self.id = id
        self.buttons = []

    #setter and getter methods
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    #general methods to the class
    def add_button(self, button):
        self.buttons.append(button)

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

play_button = Button(config.window_width // 2 - 100, config.window_height // 2 - 50, 200, 50, "Play")
exit_button = Button(config.window_width // 2 - 100, config.window_height // 2 + 20, 200, 50, "Exit")

start_menu = Menu("Start Menu", 0)
start_menu.add_button(play_button)
start_menu.add_button(exit_button)

game_over_menu = Menu("Game Over Menu", 1)
replay_button = Button(config.window_width // 2 - 100, config.window_height // 2 - 50, 200, 50, "Replay")
return_menu_button = Button(config.window_width // 2 - 100, config.window_height // 2 + 20, 200, 50, "Return to Menu")
exit_button = Button(config.window_width // 2 - 100, config.window_height // 2 + 100, 200, 50, "Exit")
game_over_menu.add_button(replay_button)
game_over_menu.add_button(return_menu_button)
game_over_menu.add_button(exit_button)

