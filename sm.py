import csv
import math
from time import perf_counter
from collections import deque
class Location():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adj = []
        self.valid = False
        self.visited = False

def RouteString(routes):
    o = "["
    for route in routes:
        o = o + route.name + ", "
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

def BFSBT(parent, start, end):
    path = [end]
    while(path[-1] != start):
        #print("Path:", path[-1])
        path.append(parent[path[-1]])
    path.reverse()
    return path

"""
Need to implement distance 
and 
figure out why path is so much longer and if thats ok
"""

def BreadthFirst(start, end):
    """
    Implementation modified from https://stackoverflow.com/a/8922151
    """
    print("Breadth-First Method")
    for x in ldict.items():
        x[1].visited = False
    parent = {}
    start.visited = True
    q = deque([start])
    while q:
        node = q.pop()
        #print(node)
        if node == end:
            return BFSBT(parent, start, end)
        for a in ldict.get(node.name).adj:
            if a.visited == False and a not in q:
                a.visited = True
                parent[a] = node
                q.append(a)

def DFSUtil(start, end, path=None):
    print(f"At {start.name}")
    start.visited = True
    if path is None:
        path = []
    path.append(start)
    il = True
    for a in start.adj:
        if not a.visited:
            print(f"Visit {a.name}")
            if a == end:
                print(f"Found Match {a.name}")
                path.append(a)
                il = False
                break 
            else:
                print(f"Recurse {a.name}")
                a.visited = True
                return DFSUtil(a, end, path)
        elif not il:
            break
        elif a.visited:
            continue
            #print(f"Backtracking {a.name}")
            #return DFSUtil(a, end, path)

    if not il:
        return path
    
def DFS(start, end):
    p = DFSUtil(start, end)
    print(p)
    return p
"""       
def DFS(start, end, dpath=None, e=None):
    if dpath is None:
        df = []
    else:
        df = dpath
    start.visited = True
    df.append(start)
    print(f"Visit @{start.name}")
    if start == end:
        print(f"Match found {start.name}\nReturning df: {df}")
        return df
    for a in start.adj:
        if not a.visited and a not in df:
            a.visited = True
            print(f"Recurse {a.name}")
            return DFS(a, end, df)
        elif a in df:
            for aa in a.adj:
                if not aa.visited:
                    print(f"other Recurse {aa.name}")
                    #df.pop()
                    aa.visited = True
                    return DFS(aa, end, df)
                else:
                    print(f"Back Recurse {aa.name}")
                    continue
                    #return DFS(f)
        elif a not in df:
            print(f"I Guess another back recurse {a.name}")
            f = df.pop()
            return DFS(f, end, df)
        else:
            continue
        #else:# a.visited and a in df:

"""
#return df
"""
    elif a not in df:
        print(f"Continuing {a.name}")
        f = df.pop(0)
        return DFS(f, end, df)
    else:
        continue
"""
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
        #print(f"Valid Start Town: {start}")
        s = False
    else:
        print(f"Invalid Starting Town {start}")
e = True
while e:
    end = input("Input Ending Town: ")
    if ldict.get(end):
        #print(f"Valid Ending Town: {end}")
        e = False
    else:
        print(f"Invalid Ending Town {end}")
method = 0
while method in range(0,7):
    method = input(f"0: Undirected(blind) Brute-Force\n1: Breadth-First\n2: Depth-First\n3: ID-DFS\n4: Best-First\n5: A*\n6: Change Cities\nSelect Method: ")
    try:
        method = int(method)
    except:
        print(f"Out of Range, Exiting")
        method = 9
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
        print(f"Using the Brute-Force Method:\nFound {len(bf)} routes, the Shortest Route was {finalstr} with a length of {shortdistance} miles in {finaltime} seconds.\n")
    elif method == 1:
        bfst = perf_counter()
        bfs = BreadthFirst(ldict.get(start), ldict.get(end))
        d = RouteDistance(bfs)
        bfse = perf_counter()
        finaltime = bfse - bfst
        o = RouteString(bfs)
        print(f"Found route {o} with a distance of {d} miles in {finaltime} seconds.\n")
    elif method == 2:
        print('Depth-First Method')
        dfst = perf_counter()
        for x in ldict.items():
            x[1].visited = False
        df = DFS(ldict.get(start), ldict.get(end))
        dfse = perf_counter()
        finaltime = dfse - dfst
        if df is not None:
            o = RouteString(df)
            d = RouteDistance(df)
        else:
            o = "Error"
            d = 0
        print(f"Found Route {o} with a distance of {d} miles in {finaltime} seconds\n")
    elif method == 3:
        IDDFS()
    elif method == 4:
        BestFirst()
    elif method == 5:
        AStar()
    elif method == 6:
        start = input("Input Start City: ")
        end = input("Input End City: ")
    else:
        exit

