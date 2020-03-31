'''
Author: @Troy Stanich
Title: Assignment 3
Part 3: Test Script
'''

from generator import LCG
from generator import SCG
from point import Point
import time

def main():
    '''
    Function to be called if script is run directly
    '''

    #LCG Instance
    genLCG = LCG(1,1103515245,12345,2**32)

    #SCG Instance
    genSCG = SCG(6,1103515245,12345,2**32)

    #Values used for transforming [0,1] range to [-1,1] range
    oldMin = 0
    oldRange = 1
    newMin = -1
    newRange = 2

    #Counters
    inCircleLCG = 0
    inCircleSCG = 0

    for i in range(10**7):
        
        #Create two random numbers, X and Y, between [-1,1]
        xCoorLCG = ((((next(genLCG)/(2**32)) - oldMin) * newRange) / oldRange) +newMin
        yCoorLCG = ((((next(genLCG)/(2**32)) - oldMin) * newRange) / oldRange) +newMin

        #Create an instance of the Point class with the generated numbers as the X and Y parameters
        pointLCG = Point(xCoorLCG, yCoorLCG)
        
        #Check the distance, if less than one, increase counter
        if pointLCG.distance() < 1:
            inCircleLCG += 1

        #Create two random numbers, X and Y, between [-1,1]
        xCoorSCG = ((((next(genSCG)/(2**32)) - oldMin) * newRange) / oldRange) +newMin
        yCoorSCG = ((((next(genSCG)/(2**32)) - oldMin) * newRange) / oldRange) +newMin

        #Create an instance of the Point class with the generated numbers as the X and Y parameters
        pointSCG = Point(xCoorSCG, yCoorSCG)

        #Check the distance, if less than one, increase counter
        if pointSCG.distance() < 1:
            inCircleSCG += 1

    print(f"The obtained ratio for the LCG Generator is {inCircleLCG/(10**7)}")
    print(f"The obtained ratio minus the theoretical is {inCircleLCG/(10**7) - 0.78539816339}")

    print(f"The obtained ratio for the SCG Generator is {inCircleSCG/(10**7)}")
    print(f"The obtained ratio minus the theoretical is {inCircleSCG/(10**7) - 0.78539816339}")



if __name__ == "__main__":
    
    '''
    Creates a time stamp at beginning
    Runs the main() function
    Creates a time stamp at finish
    Prints the difference in time stamps for total runtime
    '''

    startTime = time.time()
    main()
    print(f"This program took {time.time() - startTime} seconds to execute.")