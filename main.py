class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a node into the BST
def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root

# Function to search a value in the BST
def search(root, key):
    if root is None or root.value == key:
        return root
    
    if key < root.value:
        return search(root.left, key)
    
    return search(root.right, key)

# Function to find the minimum value node in the tree (used for deletion)
def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

# Function to delete a node from the BST
def delete_node(root, key):
    if root is None:
        return root
    
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with two children: get the inorder successor (smallest in the right subtree)
        temp = find_min(root.right)
        root.value = temp.value  # Replace root's value with successor's value
        root.right = delete_node(root.right, temp.value)  # Delete the successor
    
    return root

# Inorder traversal (Left, Root, Right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Preorder traversal (Root, Left, Right)
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder traversal (Left, Right, Root)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Menu-driven program
def menu():
    root = None
    while True:
        print("\n--- Binary Search Tree Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")
        
        choice = int(input("Enter your choice (1-7): "))
        
        if choice == 1:
            value = int(input("Enter value to insert: "))
            root = insert(root, value)
            print(f"{value} inserted into the tree.")
        
        elif choice == 2:
            value = int(input("Enter value to delete: "))
            root = delete_node(root, value)
            print(f"{value} deleted from the tree.")
        
        elif choice == 3:
            value = int(input("Enter value to search: "))
            result = search(root, value)
            if result:
                print(f"Value {value} found in the tree.")
            else:
                print(f"Value {value} not found in the tree.")
        
        elif choice == 4:
            print("Inorder Traversal: ", end = "")
            inorder_traversal(root)
            print()
        
        elif choice == 5:
            print("Preorder Traversal: ", end = "")
            preorder_traversal(root)
            print()
        
        elif choice == 6:
            print("Postorder Traversal: ", end = "")
            postorder_traversal(root)
            print()
        
        elif choice == 7:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu-based program
if __name__ == "__main__":
    menu()
