/* Your Name
 * Physics91SI, Spring 2013
 * Lab #14, Part 2
 */

/*This file implements the update of the life board in pure C*/

#include <stdio.h>

/*
array[i,j] in python is equivalent to array[index2d(N,i,j)] in C
*/

int index2d(int N, int i, int j) {
	return i*N + j;
}


/*This function returns the number of live neighbors of the point indexed by [index_x, index_y] on the board*/
int getNeighbors(long* board,int index_x,int index_y, int N) {
	int neighbors = 0;
	/*Your code goes here*/
	return neighbors;
}

/*This function iterates over the grid and updates the values according to the rules of the game of life*/
void update_pure_c(long* board, int N) {
	int neighbors_arr[N*N];
/*Your code goes here*/
}

