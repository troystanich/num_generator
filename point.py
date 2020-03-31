'''
Author: @Troy Stanich
Title: Assignment 3
Part 3: Point Class
'''

import math

class Point:
    '''
    Class for points on a coordinate system
    Stores X and Y coordinates
    '''
    def __init__(self, x_coor, y_coor):
        self.x = x_coor
        self.y = y_coor

    def distance(self):
        '''
        Returns the distance of point from origin (0,0)
        '''
        distance = math.sqrt(self.x**2 + self.y**2)
        return distance

if __name__ == "__main__":
    point = Point(2,2)
    print(point.x)
    print(point.y)
    print(point.distance())