import csv
import math
from time import perf_counter
import geopy
class Location():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj = []
        self.valid = False
        self.visited = False

def RouteString(route):
    o = "["
    for p in route:
        o = o + p.name + ", "
    o = o[:-2] + "]"
    return o

def RouteDistance(route):
    # Formula/Code modified from https://stackoverflow.com/a/64584687/19605485
    prev = None
    distance = 0
    for r in route:
        if prev is None:
            prev = r
            continue
        ola = math.radians(float(prev.x))
        olo = math.radians(float(prev.y))
        ela = math.radians(float(r.x))
        elo = math.radians(float(r.y))
        lad = ela - ola
        lod = elo - olo
        r = 6378127
        a = math.sin(lad / 2) ** 2 + math.cos(ola) * math.cos(ela) * math.sin(lod / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        dp = c * r
        distance = distance + dp
    return int((distance * 0.000621371) * 10**2) / 10**2
def BruteForce(start, end, path=[]):
    """
    Modified from ChatGPT 3.5
    Prompt: using python you are given a list of cities and a list of city adjacency pairs, i need to find a path with an undirected blind brute force search to get from one city to another
    Followup Prompt: can you do this without dfs
    """

    path = path + [start]
    if start.name == end.name:
        return [path]
    if ldict.get(start.name) is None:
        return []
    paths = []
    for p in ldict.get(start.name).adj:
        if p not in path:
            new = BruteForce(p, end, path)
            if new is None:
                continue
            for n in new:
                paths.append(n)

    return paths

def BreadthFirst():
    print("Breadth-First Method")

def DepthFirst():
    print('Depth-First Method')

def IDDFS():
    print("ID-DFS Method")

def BestFirst():
    print("Best-First Method")

def AStar():
    print("A* Method")

ldict = {}

with open("coordinates.csv", newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for r in reader:
        l = Location(name=r[0], x=r[1].lstrip(), y=r[2].lstrip())
        ldict[l.name] = l

with open("Adjacencies.txt", "r") as fa:
    lines = fa.readlines()
    for l in lines:
        l = l.replace(f"\n", "").rstrip()
        aj = l.split(" ")
        a = ldict.get(aj[0])
        if a:
            if a.adj is None:
                a.adj = []
            if ldict.get(aj[1]) is not None:
                a.adj.append(ldict.get(aj[1]))
        a = ldict.get(aj[1])
        if a:
            if a.adj is None:
                a.adj = []
            if ldict.get(aj[0]) is not None:    
                a.adj.append(ldict.get(aj[0]))

s = True
while s:
    start = input("Input Starting Town: ")
    if ldict.get(start):
        print(f"Valid Start Town: {start}")
        s = False
    else:
        print(f"Invalid Starting Town {start}")
end = input("Input Ending Town: ")
e = True
while e:
    if ldict.get(end):
        print(f"Valid Ending Town: {end}")
        e = False
    else:
        print(f"Invalid Ending Town {end}")

method = int(input(f"\t0: Undirected(blind) Brute-Force\n\t1: Breadth-First\n\t2:Depth-First\n\t3: ID-DFS\n\t4: Best-First\n\t5: A*\nSelect Method: "))
if method in range(0,5):
    if method == 0:
        bft = perf_counter()
        bf = BruteForce(start=ldict.get(start), end=ldict.get(end))
        finalstr = None
        shortest = None
        shortdistance = None
        for b in bf:      
            o = RouteString(b)
            d = RouteDistance(b)
            #print(d)
            if (shortest is None) or (d < shortdistance):
                shortest = b
                finalstr = o
                shortdistance = d
        bfte = perf_counter()
        finaltime = bfte - bft
        print(f"Using the Brute-Force Method:\nFound {len(bf)} routes, the Shortest Route was {finalstr} with a length of {shortdistance} miles in {finaltime} seconds.")
    elif method == 1:
        BreadthFirst()
    elif method == 2:
        DepthFirst()
    elif method == 3:
        IDDFS()
    elif method == 4:
        BestFirst()
    elif method == 5:
        AStar()
else:
    print("Incorrect Method Number")

