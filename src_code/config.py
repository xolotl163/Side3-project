import pygame

#constants for the "literal" windows or screen
window_width = 1920
window_height = 1080
screen_center = (window_width / 2, window_height / 2)
player_movement_speed = 500
bullet_movement_speed = 250
const_limit_escenary = 25

#objects and instances constants
player_image = "src_code/resources/placeholders/player_placeholder.png"
enemy_image = "src_code/resources/placeholders/enemy_placeholder.png"
bullet_image = "src_code/resources/placeholders/bullet_placeholder.png"
obstacle_image = "src_code/resources/placeholders/obstacle_placeholder.png"
player_width = 50
player_height = 50
bullet_width = 16
bullet_height = 16
obstacle_width = 200
obstacle_height = 75

#in-game constants
max_shooted_bullets = 20

#in-game variables
dev_mode = True #used to show hitboxes in screen and others information, remember that hitboxes are shown in red and surfaces are shown in blue

#dictionaries, lists and other data structures that are important for the game

#general information of the game
game_state = {
    "game_menu": 0,
    "playing": 1,
    "game_over": 2
}
current_game_state = game_state["game_menu"]
fps = 60
background_color = "gray"
