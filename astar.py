import pygame
import random
import math
from queue import PriorityQueue
import time
start = time.time()
WIDTH = 500  # size of the pygame screen
WIN = pygame.display.set_mode((WIDTH, WIDTH))  # setting the screen size
pygame.display.set_caption("A* Path Finding Algorithm Game!")

# colore palet:
RED = (220, 20, 60)
LIGHT_PINK = (255, 188, 217)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HOT_PINK = (255, 105, 180)
YELLOW = (255, 255, 102)
GREY = (128, 128, 128)
GREEN = (50, 205, 50)
# class Spot is responsible for the representing of the spot, it's colore,it's neighboring spots that aren't barriers all for our grid.


class Spot:
    # constructing fro the Spot class:
    def __init__(self, row, col, width, TotalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = TotalRows
    # get methods:

    def get_pos(self):
        return self.row, self.col

    def CLOSED_red(self):
        return self.color == RED

    def OPEND_green(self):
        return self.color == GREEN

    def BARRIER_black(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == LIGHT_PINK
    # setting methods:

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = YELLOW

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = LIGHT_PINK

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = GREEN

    def make_path(self):
        self.color = HOT_PINK

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))
    # method that chosce the fitted neighbors for spots in the paths of A*

    def update_neighbors(self, grid):
        # virtical and horizantal moves
        self.neighbors = []
        if self.row < self.total_rows - 1:  # DOWN
            if not grid[self.row + 1][self.col].BARRIER_black():
                self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0:  # UP
            if not grid[self.row - 1][self.col].BARRIER_black():
                self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1:  # RIGHT
            if not grid[self.row][self.col + 1].BARRIER_black():
                self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0:  # LEFT
            if not grid[self.row][self.col - 1].BARRIER_black():
                self.neighbors.append(grid[self.row][self.col - 1])
    # diagnal moves:
        if self.row < self.total_rows - 1 and self.col < self.total_rows - 1:  # DOWN-RIGHT
            if not grid[self.row + 1][self.col + 1].BARRIER_black():
                self.neighbors.append(grid[self.row + 1][self.col + 1])
        if self.row < self.total_rows - 1 and self.col > 0:  # DOWN-LEFT
            if not grid[self.row + 1][self.col - 1].BARRIER_black():
                self.neighbors.append(grid[self.row + 1][self.col - 1])
        if self.row > 0 and self.col > 0:  # UP-LEFT
            if not grid[self.row - 1][self.col - 1].BARRIER_black():
                self.neighbors.append(grid[self.row - 1][self.col - 1])
        if self.row > 0 and self.col < self.total_rows - 1:  # UP-RIGHT
            if not grid[self.row - 1][self.col + 1].BARRIER_black():
                self.neighbors.append(grid[self.row - 1][self.col + 1])

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
# for showing the correct path A* got


def reconstruct_path(came_from, current, draw):
    total_cost = 0.0
    while current in came_from:
        previous = came_from[current]
        current.make_path()
        # Calculate the cost between the current and previous nodes
        dx = current.row - previous.row
        dy = current.col - previous.col
        if dx == 1 and dy == 1:
            cost = 1.414213562
        else:
            cost = 1.0
        total_cost += cost
        current = previous
        draw()
    return True, total_cost
# A* implementation


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            success, total_cost = reconstruct_path(came_from, end, draw)
            end.make_end()
            if success:
                print("Total cost:", total_cost)
            return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start:
            current.make_closed()
    return False
# determaning the barier persentages and where they are located


def make_grid(rows, width):
    grid = []
    gap = width // rows
    num_obstacles = 0
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            obstacle_chance = random.randint(10, 91)
            if random.randint(1, 100) <= obstacle_chance and num_obstacles < rows*rows*obstacle_chance/100:
                spot.make_barrier()
                num_obstacles += 1
            grid[i].append(spot)
    print(f"Number of obstacles generated: {num_obstacles}")
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col
# main method :


def main(win, width):
    ROWS = 10
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
    pygame.quit()


end = time.time()
elapsed = end - start
print(f"Execution time: {elapsed} seconds")
main(WIN, WIDTH)
