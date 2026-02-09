class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, car):
        new_node = Node(None, None, car)

        if self.head == None:
            self.head = new_node
            return

        if car.price < self.head.data.price:
            new_node.nextNode = self.head
            self.head.prevNode = new_node
            self.head = new_node
            return

        current = self.head
        while (current.nextNode != None and current.nextNode.data.price <= car.price):
            current = current.nextNode

        if current.nextNode != None:
            next_node = current.nextNode
            new_node.nextNode = next_node
            new_node.prevNode = current
            current.nextNode = new_node
            next_node.prevNode = new_node
            return

        current.nextNode = new_node
        new_node.prevNode = current
        

class Car:
    def __init__(self, identification: int, name: str, brand: str, price: int, active: bool):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


db = LinkedList()


def init(cars):
    db.head = None
    for car in cars:
        db.push(car)


def add(car):
    db.push(car)
    return None

def updateName(identification, name):
    current = db.head

    while current != None:
        if current.data.identification == identification:
            current.data.name = name
            return None
        current = current.nextNode

    return None

def updateBrand(identification, brand):
    current = db.head

    while current != None:
        if current.data.identification == identification:
            current.data.brand = brand
            return None  
        current = current.nextNode

    return None


def activateCar(identification):
    current = db.head

    while current != None:
        if current.data.identification == identification:
            current.data.active = True
            return None 
        current = current.nextNode

    return None 


def deactivateCar(identification):
    current = db.head

    while current != None:
        if current.data.identification == identification:
            current.data.active = False
            return None 
        current = current.nextNode

    return None 


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    result = 0
    current = db.head

    while current != None:
        if current.data.active == True:
            result += current.data.price
        current = current.nextNode

    return result


def clean():
    db.head = None
    return None
