# Your Name
# Physics91SI, Spring 2013
# Lab #14, Part 0

"""
This file animates the game of life. It implements the update of the board
in both pure Python and Cython.

"""

from matplotlib import use
use("Tkagg")
from matplotlib import pyplot as plt
plt.ion()
import numpy as np

cy_compiled = True
try: import life_cy
except ImportError:
    cy_compiled = False
    print ('Warning: module life_cy not yet implemented. Do not use "c" or '
           '"cython" mode')

def update_py(board, N):
    neighbors_arr = np.zeros((N, N))
    for i in range(1, N-1):
        for j in range(1, N-1):
            neighbors_arr[i, j] = getNeighbors(board, i, j, N)
    for i in range(1, N-1):
        for j in range(1, N-1):
            neighbors = neighbors_arr[i, j]
            if board[i, j] == 0:
                if neighbors == 3:
                    board[i, j] = 1
            elif board[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    board[i, j] = 0

def getNeighbors(board, index_x, index_y, N):
    neighbors = 0
    for k in [-1,0,1]:
        for l in [-1,0,1]:
            if not (k == 0 and l == 0):
                if board[index_x+k,index_y + l] != 0:
                    neighbors += 1
    return neighbors

def life(N, p, plotting=True, version="python"):
    """
    This function plays the game of life. It takes the following arguments:
    N = the length of the board (N by N board)
    p = the probability of a cell being alive at the initial setup
    plotting = whether or not to plot the progress (set to false for speed
        measurements)
    version = "python", "c" or "cython"; execute the code in one of these
        3 languages
    
    """

    num_iterations = 20
    board = np.int_(np.random.binomial(1, p, size=(N, N)))
    board[0,:] = 0
    board[-1,:] = 0
    board[:,0] = 0
    board[:,-1] = 0

    # Label the appropriate function 'update' so we can call it repeatedly
    if version.lower() == "c":
        if not cy_compiled: raise NotImplementedError(
                                   '"c" version not yet written or compiled')
        update = life_cy.update_c
    elif version.lower() == "cython":
        if not cy_compiled: raise NotImplementedError(
                                   '"cython" version not yet written or '
                                   'compiled')
        update = life_cy.update_cy
    elif version.lower() == "python": update = update_py
    else: raise NameError, ('Please use a valid version: '
                            '"python", "cython", or "c"')
    for i in range(num_iterations):
        update(board, N)
        if plotting: plot_board(board)

def plot_board(board):
    plt.imshow(board, interpolation="nearest", vmin=0, vmax=1)
    plt.show()
    plt.gcf().canvas.flush_events()

