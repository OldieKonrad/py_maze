import pygame
from time import perf_counter
from MazeGenerator import Maze

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)


GRID_WIDTH = 50
GRID_HEIGHT = 50
TILE_SIZE = 8
WIDTH  = ((GRID_WIDTH *2)+1) * TILE_SIZE
HEIGHT = ((GRID_HEIGHT*2)+1) * TILE_SIZE

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def draw_grid(grid):
    
    for irow, row in enumerate(grid, 0):
        for icol, col in enumerate(row, 0):
            if grid[irow][icol] != 'X':
                top_left = (icol * TILE_SIZE, irow * TILE_SIZE)
                pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT*2+1):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH*2+1):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def main():
    stime = perf_counter()
    maze = Maze(GRID_WIDTH, GRID_HEIGHT)
    etime = perf_counter()
    print(f'maze generation took: {etime-stime:0.4f}')
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # quit game / close window
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:     # toggle to generate new maze
                    stime = perf_counter()
                    maze = Maze(GRID_WIDTH, GRID_HEIGHT)
                    etime = perf_counter()
                    print(f'maze generation took: {etime-stime:0.4f}')
                    
        screen.fill(GREY)
        draw_grid(maze.grid)
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()