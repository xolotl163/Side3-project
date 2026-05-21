
import config
import pygame
pygame.init()

#selfmade imports
import characters.character as character

# pygame setup - start
screen = pygame.display.set_mode((config.window_width, config.window_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
# pygame setup - end

player = character.Player(config.window_width // 2, 1050, 50, 50, config.player_image)

while running:
    
    """ 
        poll for events
        By separating the event polling from the game logic, we can ensure that we are processing all events that have occurred since the last frame, 
        and we can also avoid missing any events that may have occurred while we were processing the game logic.      
    """
    delta_time = clock.tick(config.fps) / 1000.0  # limits FPS to 60

    events = pygame.event.get()  # returns a list of all events that have occurred since the last time this function was called
    keys = pygame.key.get_pressed() # get the state of all keyboard buttons, returns a list of booleans representing each key

    #global events
    for event in events:
        #these two events are for quitting the game, one is for when the user clicks the close button, and the other is for when the user presses the escape key
        if event.type == pygame.QUIT:  # check for the QUIT event, which happens when the user clicks the close button
            print ("Quitting the game...")
            running = False
        if event.type == pygame.KEYDOWN:  # check for keydown events
            if event.key == pygame.K_ESCAPE:  # if the key pressed is the escape key
                print ("Quitting the game...")
                running = False

        #player events
        if event.type == pygame.MOUSEMOTION:
            player.rotate(pygame.mouse.get_pos(), delta_time)  # rotate the player to look at the mouse cursor

    """ Logic of the game """
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(config.background_color)
    
    #player logic
    player.move(keys,delta_time)  # move the player based on the keys that are currently pressed

    # RENDER YOUR GAME HERE -> starts
    player.draw(screen)
    pygame.draw.rect(screen, "red", player.rect, 2)  # draw the player's rect for debugging purposes
    # RENDER YOUR GAME HERE -> ends

    # flip() the display to put your work on screen
    pygame.display.flip()
