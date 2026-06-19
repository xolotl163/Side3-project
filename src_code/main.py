
import config
import pygame
pygame.init()

#selfmade imports
import characters.character as character
import general_objects.bullet as bullet
import general_objects.obstacle as obstacle

# pygame setup - start
screen = pygame.display.set_mode((config.window_width, config.window_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
# pygame setup - end

#general objets and values to the excecution
player = character.Player(config.window_width // 2, (config.window_height // 2)+150, config.player_width, config.player_height, config.player_image)
obstacle = obstacle.Obstacle(config.window_width // 2, config.window_height // 2,config.obstacle_width,config.obstacle_height,config.obstacle_image)
player_bullets = []  
obstacles = [] #this list is used more than 1 obstacles are needed
obstacles.append(obstacle)

while running:
    
    """ 
        poll for events
        By separating the event polling from the game logic, we can ensure that we are processing all events that have occurred since the last frame, 
        and we can also avoid missing any events that may have occurred while we were processing the game logic.      
    """
    delta_time = clock.tick(config.fps) / 1000.0  # limits FPS to 60

    events = pygame.event.get()  # returns a list of all events that have occurred since the last time this function was called
    keys = pygame.key.get_pressed() # get the state of all keyboard buttons, returns a list of booleans representing each key

    """ Logic of the game -> starts """
    #player logic
    player.move(keys,delta_time)  # move the player based on the keys that are currently pressed
   # player.rotate(pygame.mouse.get_pos(), delta_time)  # rotate the player to look at the mouse cursor
    
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
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if len(player_bullets) < config.max_shooted_bullets:
                    player.shoot(player_bullets)
                    player_bullets[-1].add_observer(obstacle)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(config.background_color)   

    #for the bullets
    for bullet in player_bullets:
        bullet.reposition(bullet.direction, delta_time)
        if bullet.is_active == True:
            bullet.check_collisions(obstacles)
    
    #for the obstacles
    for obst in obstacles:
        obst.check_is_active()

    #instances are liberated 
    player_bullets = [b for b in player_bullets if b.is_active]
    obstacles = [b for b in obstacles if b.is_active]
    """ logic of the game - ends """

    # RENDER YOUR GAME HERE -> starts
    for bullet in player_bullets:
        bullet.draw(screen)
        
        if config.dev_mode == True:
            pygame.draw.rect(screen, "red", bullet.rect, 2)

    for obst in obstacles:
        obst.draw(screen)
        if config.dev_mode == True:
            pygame.draw.rect(screen, "red", obstacle.rect, 2)

    #objects draw
    player.draw(screen)

    #hitboxes draw
    if config.dev_mode == True:
        #surfaces
        pygame.draw.rect(screen, "blue", player.rect, 2)  # draw the player's rect for debugging purposes
        
        #hitboxes
        pygame.draw.rect(screen, "red", player.hitbox, 2)

    # RENDER YOUR GAME HERE -> ends

    # flip() the display to put your work on screen
    pygame.display.flip()
