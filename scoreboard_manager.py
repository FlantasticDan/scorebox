from typing import List, Tuple
from math import sqrt

import numpy as np
import cv2

from camera_manager import CameraManager

class ScoreboardManager:

    def __init__(self, source: CameraManager, corner_pin: List[Tuple[int, int]]):
        self.corner_pin = corner_pin
        self.source: CameraManager = source

        self.aspect_ratio: int = None
        self.dimensions: Tuple[int, int] = None

        self.calculate_scoreboard_dimensions()

    def calculate_scoreboard_dimensions(self):
        self.aspect_ratio = get_aspect_ratio(self.corner_pin)
        self.dimensions = get_dimensions(self.corner_pin, self.aspect_ratio)
        
        print(self.dimensions)


def get_dimensions(corner_pin: List[Tuple[int, int]], aspect_ratio: int) -> Tuple[int, int]:
    '''
    Given the corners of a perspective warped rectangle, and it's estimated aspect ratio,
    return the maximum dimensions of the un-warped rectangle without scaling.
    '''
    top = get_line_length(corner_pin[0], corner_pin[1])
    bottom = get_line_length(corner_pin[3], corner_pin[2])
    left = get_line_length(corner_pin[0], corner_pin[3])
    right = get_line_length(corner_pin[1], corner_pin[2])

    horizontal = int(min(top, bottom))
    vertical = int(min(left, right))

    if vertical < horizontal:
        height = vertical
        width = int(aspect_ratio * height)
    else:
        width = horizontal
        height = int(width / aspect_ratio)
    
    return (width, height)

def get_line_length(point_a: Tuple[int, int], point_b: Tuple[int, int]) -> int:
    '''Given two points, return the distance of the line between them.'''
    x_a = point_a[0]
    y_a = point_a[1]
    x_b = point_b[0]
    y_b = point_b[1]

    return sqrt(sqr(x_a - x_b) + sqr(y_a - y_b))

def sqr(value: int) -> int:
    return value * value

def get_aspect_ratio(corner_pin: List[Tuple[int, int]]) -> int:
    '''
    Given four points (x,y) of a rectangle in Top Left, Top Right, Bottom Right, Bottom Left order,
    estimate the undistored rectangle's aspect ratio.
    '''

    # Algorithm by Zhengyou Zhang and Li-Wei He as part "Whiteboard scanning and image enhancement":
    # https://www.microsoft.com/en-us/research/uploads/prod/2016/11/Digital-Signal-Processing.pdf

    # Implementation based on the work of HugoRune's psuedo-code:
    # https://stackoverflow.com/questions/1194352/proportions-of-a-perspective-deformed-rectangle

    m1x = corner_pin[3][0]
    m1y = corner_pin[3][1]

    m2x = corner_pin[2][0]
    m2y = corner_pin[2][1]

    m3x = corner_pin[0][0]
    m3y = corner_pin[0][1]

    m4x = corner_pin[1][0]
    m4y = corner_pin[1][1]

    u0 = 1280 / 2
    v0 = 720 / 2

    m1x = m1x - u0
    m1y = m1y - v0
    m2x = m2x - u0
    m2y = m2y - v0
    m3x = m3x - u0
    m3y = m3y - v0
    m4x = m4x - u0
    m4y = m4y - v0

    k2 = (((m1y - m4y)*m3x - (m1x - m4x)*m3y + m1x*m4y - m1y*m4x) /
          ((m2y - m4y)*m3x - (m2x - m4x)*m3y + m2x*m4y - m2y*m4x))
    k3 = (((m1y - m4y)*m2x - (m1x - m4x)*m2y + m1x*m4y - m1y*m4x) /
          ((m3y - m4y)*m2x - (m3x - m4x)*m2y + m3x*m4y - m3y*m4x))

    f_squared = (-((k3*m3y - m1y)*(k2*m2y - m1y) + (k3*m3x - m1x)*(k2*m2x - m1x)) /
                  ((k3 - 1)*(k2 - 1)))

    aspect_ratio = sqrt(
        (sqr(k2 - 1) + sqr(k2*m2y - m1y)/f_squared + sqr(k2*m2x - m1x)/f_squared) /
        (sqr(k3 - 1) + sqr(k3*m3y - m1y)/f_squared + sqr(k3*m3x - m1x)/f_squared)
    )

    return aspect_ratio
