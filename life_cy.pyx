# Your Name
# Physics 91SI, Spring 2013
# Lab #14, Part 1

import numpy as np
cimport numpy as np

# Get the pure C version of the update function from life.c
cdef extern from "life.h":
    void update_pure_c(long* board, int N)

def update_c(np.ndarray[dtype=long, ndim=2] board, int N):
    """A wrapper for the pure C version of the update function"""
    update_pure_c(<long*> board.data, N)

def update_cy(np.ndarray[long, ndim=2] board, int N):
    """The Cython version of the update function."""
    neighbors_arr = np.zeros([N, N], dtype = int)
    # Your code goes here

cdef int getNeighbors(
        np.ndarray[long, ndim=2] board, int index_x, int index_y, int N):
    neighbors = 0
    # Your code goes here
    return neighbors
