class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.visited = 0

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right == None:
                    current.right = Node(value)
                    return
                current = current.right

    def fromArray(self, array):
        for value in array:
            self.insert(value)

    def search(self, value)->bool:
        self.visited = 0
        current = self.root

        while current != None:
            self.visited += 1

            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def min(self):
        self.visited = 0
        if self.root == None:
            return None

        current = self.root
        while current.left != None:
            self.visited += 1
            current = current.left

        self.visited += 1
        return current.value

    def max(self):
        self.visited = 0
        if self.root == None:
            return None

        current = self.root
        while current.right != None:
            self.visited += 1
            current = current.right

        self.visited += 1
        return current.value

    def visitedNodes(self)->int:
        return self.visited
