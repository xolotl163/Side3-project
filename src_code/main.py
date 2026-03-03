# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
window_width = 1280
window_height = 720
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True

#general information of the game
game_state = {
    "game_menu": 0,
    "playing": 1,
    "game_over": 2
}
current_game_state = game_state["game_menu"]
fps = 60
background_color = "gray"

#fonts
font_title = pygame.font.SysFont(None, 50)
font_menu = pygame.font.SysFont(None, 30)

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
    screen.fill(background_color)

    keys = pygame.key.get_pressed() # get the state of all keyboard buttons, returns a list of booleans representing each key

    # logica de cambio de estados generales del juego
    if current_game_state == game_state["game_menu"]:
        background_color = "gray"
        #menu buttons
        play_button = pygame.Rect(window_width // 2 - 100, window_height // 2 - 50, 200, 50)
        exit_button = pygame.Rect(window_width // 2 - 100, window_height // 2 + 20, 200, 50)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse button click
                if play_button.collidepoint(event.pos):
                    current_game_state = game_state["playing"]
                elif exit_button.collidepoint(event.pos):
                    #se debe de tomar en cuenta todo el proceso de memoria y actualización de datos importantes al cerrar el programa
                    running = False

    if current_game_state == game_state["playing"]:
        background_color = "green"
        if keys[pygame.K_SPACE]:
            current_game_state = game_state["game_over"]

    if current_game_state == game_state["game_over"]:
        background_color = (145,145,145)
        #menu buttons
        replay_button = pygame.Rect(window_width // 2 - 100, window_height // 2 - 50, 200, 50)
        return_menu_button = pygame.Rect(window_width // 2 - 100, window_height // 2 + 20, 200, 50)
        exit_button = pygame.Rect(window_width // 2 - 100, window_height // 2 + 100, 200, 50)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse button click
                if replay_button.collidepoint(event.pos):
                    current_game_state = game_state["playing"]
                elif return_menu_button.collidepoint(event.pos):
                    current_game_state = game_state["game_menu"]
                elif exit_button.collidepoint(event.pos):
                    #se debe de tomar en cuenta todo el proceso de memoria y actualización de datos importantes al cerrar el programa
                    running = False
    

    # RENDER YOUR GAME HERE

    """
        nota: se tiene que separar en un archivo aparte la logica de los menus,
        con la finalidadde que el archivo main sea lo mas limpio posible.
    """

    #game menu rendering
    if current_game_state == game_state["game_menu"]:
        play_button_text = font_menu.render("Play", True, "black")
        exit_button_text = font_menu.render("Exit", True, "black")
        pygame.draw.rect(screen, "white", play_button)
        pygame.draw.rect(screen, "white", exit_button)
        screen.blit(play_button_text, (play_button.centerx - play_button_text.get_width() // 2, play_button.centery - play_button_text.get_height() // 2))
        screen.blit(exit_button_text, (exit_button.centerx - exit_button_text.get_width() // 2, exit_button.centery - exit_button_text.get_height() // 2))

    if current_game_state == game_state["game_over"]:
        replay_button_text = font_menu.render("Replay", True, "black")
        return_menu_button_text = font_menu.render("Return to menu", True, "black")
        exit_button_text = font_menu.render("Exit", True, "black")
        pygame.draw.rect(screen, "white", replay_button)
        pygame.draw.rect(screen, "white", return_menu_button)
        pygame.draw.rect(screen, "white", exit_button)
        screen.blit(replay_button_text, (replay_button.centerx - replay_button_text.get_width() // 2, replay_button.centery - replay_button_text.get_height() // 2))
        screen.blit(return_menu_button_text, (return_menu_button.centerx - return_menu_button_text.get_width() // 2, return_menu_button.centery - return_menu_button_text.get_height() // 2))
        screen.blit(exit_button_text, (exit_button.centerx - exit_button_text.get_width() // 2, exit_button.centery - exit_button_text.get_height() // 2))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(fps)  # limits FPS to 60
