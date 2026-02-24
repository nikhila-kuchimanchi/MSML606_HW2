#NO AI OR EXTERNAL TOOLS WERE USED FOR THIS HOMEWORK ASSIGNMENT

# PROBLEM 1 - EXPRESSION TREE

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_expression_tree(postfix_tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in postfix_tokens:

        # If token is an operator
        if token in operators:
            # Pop right first, then left
            right = stack.pop()
            left = stack.pop()

            # Create operator node and push
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.append(node)

        else:
            # Operand - create node and push
            stack.append(TreeNode(token))

    # Final element - root
    return stack[0]


#print tree 
def print_inorder(node):
    if node:
        print("(", end="")
        print_inorder(node.left)
        print(node.value, end="")
        print_inorder(node.right)
        print(")", end="")


# Example test
if __name__ == "__main__":
    postfix = ["3", "4", "+", "2", "*"]
    root = build_expression_tree(postfix)

    print("Inorder expression:")
    print_inorder(root)
    print()

# PROBLEM 2 - TREE TRAVERSALS

def prefix_traversal(root):
    #Preorder traversal (Root, Left, Right)
    
    if root is None:
        return []

    return [root.value] + \
           prefix_traversal(root.left) + \
           prefix_traversal(root.right)


def postfix_traversal(root):
    #Postorder traversal (Left, Right, Root)

    if root is None:
        return []

    return postfix_traversal(root.left) + \
           postfix_traversal(root.right) + \
           [root.value]


def infix_traversal(root):
    
    #Inorder traversal (Left, Root, Right)
    #Adds parentheses for operator nodes
    
    if root is None:
        return []

    
    if root.left is None and root.right is None:
        return [root.value]

    return ['('] + \
           infix_traversal(root.left) + \
           [root.value] + \
           infix_traversal(root.right) + \
           [')']


# Testing Example

if __name__ == "__main__":
    postfix = ["3", "4", "+", "2", "*"]
    root = build_expression_tree(postfix)

    print("Prefix:", prefix_traversal(root))
    print("Infix:", infix_traversal(root))
    print("Postfix:", postfix_traversal(root))