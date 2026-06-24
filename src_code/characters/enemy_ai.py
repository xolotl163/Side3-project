
import math
import utils.behavior_tree as BH

enemy_brain = BH.BehaviorTree("Enemy Brain", "0")

"""
Conditions are defined
"""
@enemy_brain.condition("player_close")
def player_pretty_close(enemy, player):
    dist = math.hypot(
        player.x - enemy.x,
        player.y - enemy.y
    )
    return (dist < 60) #evaluates the condictions (dist < 60) and returns a boolean

@enemy_brain.condition("player_in_vision")
def see_player(enemy, player):
    dist = math.hypot(
        player.x - enemy.x,
        player.y - enemy.y
    )
    return (dist < 300)

@enemy_brain.condition("alone")
def alone(enemy, player):
    return True

"""
Actions are defined
"""
@enemy_brain.action("move_to_player")
def move_to_player(enemy, player, delta_time):
    enemy.move_towards(
        player.x,
        player.y,
        delta_time
    )

@enemy_brain.action("wait")
def idle(enemy, player, delta_time):
    #we just lef this function "as is" due to its nature
    #the enemy is waiting for the player to be near and doesn't move
    pass

"""
BHT is build
Priorities go from top to bottom
The order here is critical, the "brain" will evaluate the rules in the exact order ther are agreggated
"""
enemy_brain.add_rule("player_in_vision", "move_to_player")
enemy_brain.add_rule("alone", "wait")