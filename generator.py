'''
Author: @Troy Stanich
Title: Assignment 3
Part 3: Random Number Generator Classes
'''

class LCG:
    '''
    Class for a Linear Congruential Generator
    '''
    def __init__(self, x_not, a, c, m):
        self.seed = x_not
        self.reference = x_not
        self.multiplier = a
        self.increment = c
        self.modulus = m

    def __next__(self):
        '''
        Allows instances to be used in next()
        '''
        return self.getNextRandom()
    
    def nextNum(self):
        '''
        Function attribute to define the recurrence relation
        Updates the reference, i.e the last generated number
        Returns the reference
        '''
        self.reference = ((self.multiplier * self.reference + self.increment) % self.modulus)
        return self.reference

    def getSeed(self):
        '''
        Returns the seed
        '''
        return self.seed

    def setSeed(self, newSeed):
        '''
        Sets a new seed, resets the reference
        The next generated number will be initialized using the new seed
        '''
        self.seed = newSeed
        self.reference = newSeed

    def initializeGen(self):
        '''
        Initializes generator
        Always generates number using current seed
        '''
        self.reference = self.seed
        return self.nextNum()
    
    def getNextRandom(self):
        '''
        Generates new number
        '''
        return self.nextNum()

    def getRandomList(self, length):
        '''
        Returns a list of randomly generated numbers
        Input: Length of list, i.2 amount of generated numbers
        '''
        randList = []
        for i in range(length):
            randList.append(self.nextNum())
        return randList


class SCG(LCG):
    '''
    Class for SCG
    Inherits LCG Class
    '''
    def __init__(self, x_not, a, c, m):
        '''
        An error is raised if the seed is not valid
        '''
        LCG.__init__(self, x_not, a, c, m)
        if x_not % 4 != 2:
            raise ValueError("Xo mod 4 does not equal 2.")
            
    def nexNum(self):
        '''
        Overides from LCG Class
        Updates recurrence relation
        '''
        self.reference = ((self.reference(self.reference + 1)) % self.modulus)
        return self.reference

if __name__ == "__main__":
    
    newLCG = LCG(1,1103515245,12345,2**32)
   
    print(newLCG.getSeed())
    newLCG.setSeed(2)
    print(newLCG.getSeed())
    newLCG.setSeed(1)

    print(newLCG.initializeGen())
    print(newLCG.getNextRandom())
    print(newLCG.getRandomList(2))

    newSCG = SCG(6,1103515245,12345,2**32)
   
    print(newSCG.getSeed())
    newSCG.setSeed(2)
    print(newSCG.getSeed())
    newSCG.setSeed(1)

    print(newSCG.initializeGen())
    print(newSCG.getNextRandom())
    print(newSCG.getRandomList(2))