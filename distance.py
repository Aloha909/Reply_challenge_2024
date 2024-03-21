# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:33:36 2024

@author: letou
"""

def distance (x1, y1, x2, y2):
    from math import sqrt
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return(distance)
