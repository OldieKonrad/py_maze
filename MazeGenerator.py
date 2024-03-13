import random
from collections import defaultdict, deque

WIDTH  = 3
HEIGHT = 3

class Maze():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.graph = defaultdict(lambda : set())
        self.grid = []
        
        #self.genmaze(self.width, self.height)
        self.genmazewilson(self.width, self.height)

    def neighbors(self, col, row):
        noffset = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        lneighbors = []
        
        for (co, ro) in noffset:
            pnc = col+co
            pnr = row+ro
            
            if pnc < 0 or pnr < 0:
                continue
            if pnc >= self.width or pnr >= self.height:
                continue
            
            lneighbors.append((pnc, pnr))
        return lneighbors
    
    def genmaze(self, width, height):
        # backtrack / dfs algorithmus
        self.width = width
        self.height = height
        self.graph = defaultdict(lambda : set())        
        
        spoint = (0, 0)
        epoint = (width-1, height-1)
        
        stack = [spoint]       # init stack with starting point
        self.graph[spoint] = set()  # init graph with starting point
        
        while stack:
            cn = stack[-1]
            lneighbors = [n for n in self.neighbors(*cn) if n not in self.graph]
            #print(lneighbors)
            
            match len(lneighbors):
                case 0:
                    stack.pop()
                case 1:
                    stack.pop()
                    np = lneighbors[0]
                    stack.append(np)
                    self.graph[cn].add(np)
                    self.graph[np]
                    continue
                case _:
                    np = random.choice(lneighbors)
                    stack.append(np)
                    self.graph[cn].add(np)
                    self.graph[np]
                    
        self.graph_to_grid()

    def genmazewilson(self, width, height):
        # wilson algorithmus
        self.width = width
        self.height = height

        self.graph = defaultdict(lambda : set())

        # init all unused cells
        unusedCells = {(x, y) for y in range(height) for x in range(width)}

        # take a random unused cell as a rudimentaty graph
        rcell = random.sample(list(unusedCells), 1)[0]
        unusedCells.remove(rcell)
        self.graph[rcell]

        # find a random path from a random unused cell to a cell in the graph
        while len(unusedCells):
            # find random path to cell in graph
            rcell = random.sample(list(unusedCells), 1)[0]
            unusedCells.remove(rcell)

            # init stack with the random cell
            stack = [rcell]
            while stack:
                cn = stack[-1]
                lneighbors = self.neighbors(*cn)
                # choice one of neighbors as next cell in path
                np = random.choice(lneighbors)
                # if chosen neighbar allready in path - connect stack cells to path
                if np in self.graph:
                    # back edge
                    self.graph[np].add(cn)
                    # empty stack
                    while stack:
                        cn = stack.pop()
                        self.graph[cn].add(np)
                        np = cn
                    # continue with next random unused cell
                elif np in set(stack):
                    # got neighbor in own path
                    # backtrack stack to this neighbor and return all cells above to unused cells
                    while stack[-1] != np:
                        unusedCells.add(stack.pop())
                elif np in unusedCells:
                    # prolong path and remove from unused cells
                    stack.append(np)
                    unusedCells.remove(np)
        self.graph_to_grid()                 

    def graph_to_grid(self):
        self.grid =  [['X' for _ in range(self.width*2+1)] for __ in range(self.height*2+1)]
        
        for (col, row) in self.graph.keys():
            pnr = row*2+1
            pnc = col*2+1
            self.grid[pnr][pnc] = ' '
            for (ncol, nrow) in self.graph[(col, row)]:
                pnrow = nrow*2+1
                pncol = ncol*2+1
                
                per = (pnr+pnrow)//2
                pec = (pnc+pncol)//2
                self.grid[per][pec] = ' '      
            
        return


if __name__ == '__main__':

    maze = Maze(WIDTH, HEIGHT)

    for row in maze.grid:
        for col in row:
            print(col, end='')
        print() 
    
    # for k, v in graph.items():
    #     print(k, v)
