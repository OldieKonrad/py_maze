import random
from collections import defaultdict

WIDTH  = 10
HEIGHT = 5

class Maze():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.graph = defaultdict(lambda : set())
        self.grid = []
        
        self.genmaze(self.width, self.height)

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
            if (pnc, pnr) not in self.graph:
                lneighbors.append((pnc, pnr))
        return lneighbors
    
    def genmaze(self, width, height):
        self.width = width
        self.height = height
        self.graph = defaultdict(lambda : set())        
        
        spoint = (0, 0)
        epoint = (width-1, height-1)
        
        stack = [spoint]        # init stack with starting point
        self.graph[spoint] = set()  # init graph with starting point
        
        while stack:
            cn = stack[-1]
            lneighbors = self.neighbors(*cn)
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
