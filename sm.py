import csv

# Binary Tree implementation from https://stackoverflow.com/a/28864021

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value       
class Tree:
    def __init__(self):
        self.root = None
    def add(self, value):
        if self.root is None:
            self.root = value
        else:
            self.addNode(value, self.root)

    def addNode(self, value, node):
        if value < node.value:
            if node.left is not None:
                self.addNode(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self.addNode(value, node.right)
            else:
                node.right = Node(value)

class Location():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

locations = []
ldict = {}

with open("coordinates.csv", newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for r in reader:
        l = Location(name=r[0], x=r[1].lstrip(), y=r[2].lstrip())
        locations.append(l)
        ldict[l.name] = (l.x, l.y)


print(locations)
print(ldict)

method = input(f"Select Method:\n\t0: Undirected(blind) Brute-Force\n\t1: Breadth-First\n\t2:Depth-First\n\t3: ID-DFS\n\t4: Best-First\n\t5: A*\n")
if method in [range(0,5)]:
    print(method) 

start = input("Input Starting Town")
end = input("Input Ending Town")