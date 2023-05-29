from operator import mul
import re

class TreeNode:
    def __init__(self, val): # This creates a class
        self.val = val
        self.left = None
        self.right = None

def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

def inorderTraversalUtil(root, answer):
    if root is None:
        return # This cleanly handles non-existent "nodes"

    inorderTraversalUtil(root.left, answer) # This makes the left the root then applies, repeat
    inorderTraversalUtil(root.right, answer)
    if root.val == "+":
        print(answer)
        sum1 = sum(int(answer[0]), int(answer[1]))
        answer = [sum1]
        print(sum(answer))
    if root.val == "*":
        print(answer)
        product1 = mul(int(answer[0]),  int(answer[1]))
        answer = [product1]
        print("Traversal says: multiply")
    answer.append(root.val)
    

    return

base = "4 * 5 + 1"
# addition = base.split('(+)')
addition = re.split(r'(\+)', base[::-1], maxsplit=1) #This gets separator



additionNode = addition[1]
remainder = addition[0]
remainderArray = remainder.split('*')
remainderNode1 = remainderArray[0]
remainderNode2 = remainderArray[1]
print(addition[1])

root = TreeNode("+")
root.left = TreeNode("*")
root.left.left = TreeNode(remainderNode1)
root.left.right = TreeNode(remainderNode2) # If we are doing inorder, we want to split on the addition last because then it is the last node
root.right = TreeNode(additionNode)

print(inorderTraversal(root))

# So, if I want to solve 4 * 5 + 1, I split on the + 1 since that's what I want do do last. (Does it get more complicated if I have multiple +s)