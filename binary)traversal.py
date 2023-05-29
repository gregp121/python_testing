from operator import mul
import re

# build tree logic
class TreeNode:
    def __init__(self, val): # This creates a class
        self.val = val
        self.left = None
        self.right = None

def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

# Build traversal logic
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

# Build sepator logic
def addSub(x):
    return re.split(r"([+-])", x[::-1], maxsplit=1)
def multiDiv(x):
    return re.split(r"([*/])", x[::-1], maxsplit=1)


# Build tree insertion
def treeBuilder():
    if any(operator in base for operator in ('+', '-')):
        baseSplice = addSub(base)
        # ['1 ', '+', ' 5 * 4']
        root = TreeNode(baseSplice[1])
        root.right = TreeNode(baseSplice[2])
        if len(addSub(baseSplice[0])) > 1:
            leftSplice = addSub(baseSplice[0])
            root.left = TreeNode(leftSplice[1])
        elif len(multiDiv(baseSplice[0])) > 1:
            leftSplice = multiDiv(baseSplice[0])
            root.left = TreeNode(leftSplice[1])
        else:
            root.left = TreeNode("0")
    else:
        root = TreeNode("+")
        root.right = TreeNode("0")



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


#print(inorderTraversal(root))

# So, if I want to solve 4 * 5 + 1, I split on the + 1 since that's what I want do do last. (Does it get more complicated if I have multiple +s)