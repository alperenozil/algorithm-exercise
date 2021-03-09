class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
    	print(self.data)
    	if(self.left):
    		print (self.left)
    	if(self.right): 
    		print (self.right)
        

root = Node(10)
root.left=9
root.right=11

root.PrintTree()