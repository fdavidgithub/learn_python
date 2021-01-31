class Datum:
    def __init__ (self, name):
        self.name = name
        self.value = 0
        self.ref = None

class TreeNode:
    def __init__ (self, Datum):
        self.data = Datum
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent

        return level

    def printTree(self):
        if self.parent:
            spaces = ' ' * self.getLevel() * 2
            prefix = spaces + "|---"
        else:
            prefix = "|"

        print(prefix + self.data.name + " (" + str(self.data.value) + "%)")

        if self.children:
            for child in self.children:
                child.printTree()

