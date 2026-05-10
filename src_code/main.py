
import config
import pygame
pygame.init()

#selfmade imports
from menus.menus import start_menu, game_over_menu

# pygame setup - start

#fonts
font_title = pygame.font.SysFont(None, 50)
font_menu = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((config.window_width, config.window_height))
clock = pygame.time.Clock()
running = True
# pygame setup - end

while running:
    
    """ 
        poll for events
        By separating the event polling from the game logic, we can ensure that we are processing all events that have occurred since the last frame, 
        and we can also avoid missing any events that may have occurred while we were processing the game logic.      
    """
    events = pygame.event.get()  # returns a list of all events that have occurred since the last time this function was called
    keys = pygame.key.get_pressed() # get the state of all keyboard buttons, returns a list of booleans representing each key

    #global events
    for event in events:
        if event.type == pygame.QUIT:  # check for the QUIT event, which happens when the user clicks the close button
            running = False

    """ Logic of the game """
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(config.background_color)

    keys = pygame.key.get_pressed() # get the state of all keyboard buttons, returns a list of booleans representing each key

    # logica de cambio de estados generales del juego
    if config.current_game_state == config.game_state["game_menu"]:
        config.background_color = "gray"
        #menu buttons
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse button click
                print("Click en jugar")
                if start_menu.buttons[0].rect.collidepoint(event.pos):
                    config.current_game_state = config.game_state["playing"]
                elif start_menu.buttons[1].collidepoint(event.pos):
                    #Check the process of memory and important data update when closing the program
                    running = False

    if config.current_game_state == config.game_state["playing"]:
        config.background_color = "green"
        if keys[pygame.K_SPACE]:
            config.current_game_state = config.game_state["game_over"]

    if config.current_game_state == config.game_state["game_over"]:
        config.background_color = (145,145,145)
        #menu buttons
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse button click
                if game_over_menu.buttons[0].rect.collidepoint(event.pos):
                    config.current_game_state = config.game_state["playing"]
                elif game_over_menu.buttons[1].rect.collidepoint(event.pos):
                    config.current_game_state = config.game_state["game_menu"]
                elif game_over_menu.buttons[2].rect.collidepoint(event.pos):
                    #Check the process of memory and important data update when closing the program
                    running = False
    

    # RENDER YOUR GAME HERE -> starts

    """
        nota: se tiene que separar en un archivo aparte la logica de los menus,
        con la finalidadde que el archivo main sea lo mas limpio posible.
    """

    #game menu rendering
    if config.current_game_state == config.game_state["game_menu"]:
        start_menu.draw(screen)

    if config.current_game_state == config.game_state["game_over"]:
        game_over_menu.draw(screen)

     # RENDER YOUR GAME HERE -> ends

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(config.fps)  # limits FPS to 60
