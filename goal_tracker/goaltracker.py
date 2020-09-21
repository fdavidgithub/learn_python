from datastructs import TreeNode

def build():
    root = TreeNode("Carrier")
    
    node0 = TreeNode("English")

    node1 = TreeNode("Artificial Intelligence")
    node1.addChild(TreeNode("Neural Network"))
    node1.addChild(TreeNode("Machine Learning"))
    node1.addChild(TreeNode("Data Science"))

    root.addChild(node0)
    root.addChild(node1)

    return root
    
if __name__ == '__main__':
    goal = build()
    goal.printTree()
    pass
    
