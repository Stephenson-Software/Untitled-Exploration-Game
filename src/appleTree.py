from entity import Entity


# @author Daniel McCoy Stephenson
# @since August 8th, 2022
class AppleTree(Entity):
    def __init__(self):
        Entity.__init__(self, "Apple Tree")
        self.color = (139, 69, 19)
    
    def getColor(self):
        return self.color