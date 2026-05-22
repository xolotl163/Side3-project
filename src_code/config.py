import pygame

#constants
window_width = 1920
window_height = 1080
screen_center = (window_width / 2, window_height / 2)
player_movement_speed = 500
bullet_movement_speed = 250
const_limit_escenary = 25

bullet_width = 18
bullet_height = 34

player_image = "src_code/resources/placeholders/player_placeholder.png"
bullet_image = "src_code/resources/placeholders/bullet_placeholder.png"

#general variables

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
