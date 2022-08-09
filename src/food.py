import random
from entity import Entity


# @author Daniel McCoy Stephenson
# @since August 8th, 2022
class Food(Entity):
    def __init__(self):
        Entity.__init__(self, "Food")
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    
    def getColor(self):
        return self.color