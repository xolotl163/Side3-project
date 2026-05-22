"""
general funcitons to use alongside the project
"""

import pygame
import math

def angle_to_forward_vector(rotation):
        angle_rad = math.radians(rotation)
        forward_x = math.cos(angle_rad)
        forward_y = math.sin(angle_rad)
        return (forward_x, forward_y)