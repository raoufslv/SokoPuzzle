from collections import deque
from copy import deepcopy
import numpy as np
from math import inf
import itertools

class Node:

    tab_stat = [] # The wall, space and obstacle of the puzzle are stored in a global variable to be used in the heuristic functions, and in the executeMove function of the class State 
    deadlock_map = [] # Check if the node is a deadlock state or not 

    def __init__(self, sokoPuzzle, parent=None, move="", cost=1): # Constructor of the class Node, which is used to represent a node in the search tree, sokoPuzzle is an instance of the class State, parent is the parent node, move is the move that leads to the current state, cost is the cost of the move
        self.state = sokoPuzzle
        self.parent = parent
        if self.parent == None: # If the parent is None, then the current node is the root node of the search tree and the cost of the move is 0 
            self.depth = 0 # The depth of the root node is 0
            self.cost = 0 # The cost of the root node is 0
            self.moves = move # The moves that lead to the root node is an empty string
        else :
            self.depth = self.parent.depth + 1 # The depth of the current node is the depth of the parent node plus 1
            self.cost = self.parent.cost + cost # The cost of the current node is the cost of the parent node plus the cost of the move 
            self.moves = self.parent.moves + move # The moves that lead to the current node is the moves that lead to the parent node plus the move that leads to the current node

    # Generate the successors
    def succ(self): # Return the successors of the current node, the successors are stored in a list, each successor is an instance of the class Node, the successors are generated by moving the robot in all the possible directions, and pushing the boxes in all the possible directions, the function also checks if the move is valid or not, and if the move leads to a deadlock state or not, and if the move leads to a state that has been visited before or not, and if the move leads to a state that has been generated before or not
        succs = deque() # The successors are stored in a deque to be used in the breadth first search algorithm, the deque is used to store the nodes in the frontier of the search tree, and the nodes are removed from the left of the deque, and the nodes are added to the right of the deque, so the nodes are removed in the order that they are added to the deque, which is the order of the breadth first search algorithm, 
        for m in self.state.moves: # Iterate over the possible moves of the robot and the boxes, the possible moves are stored in a list in the class State, the list is called moves, and the moves are stored in the following order: 'U', 'D', 'L', 'R', which means that the robot can move up, down, left, and right, and the boxes can be pushed up, down, left, and right, 
            succState = deepcopy(self.state) # Create a copy of the current state, the copy is used to generate the successor state, the copy is used to avoid changing the current state, and to avoid changing the states of the other successors that are generated from the current state 
            if succState.executeMove(m, Node.tab_stat): # Check if the move is valid or not
                #check if the state is a deadlock state or not
                #if not succState.isDeadlock(Node.deadlock_map): # Check if the state is a deadlock state or not
                succs.append(Node(succState, self, m)) # If the move is valid and the state is not a deadlock state, then add the successor to the list of the successors
        return succs # Return the list of the successors of the current node

    # Return the search solution
    def getSolution(self):  # Return the solution of the search problem, the solution is stored in a list, each element of the list is a string, the string is the move that leads to the next state, the solution is generated by backtracking from the goal node to the root node, and the moves that lead to the next state are stored in the moves attribute of the class Node, the moves are stored in the order of the moves that lead to the next state, so the solution is generated by reversing the moves attribute of the class Node
        node = self # The current node is the goal node
        solution = [] # The solution is stored in a list
        while node: # Iterate over the nodes in the search tree, the iteration stops when the current node is the root node, the root node is the node that has no parent node, so the iteration stops when the parent node is None
            height = len(node.state.tab_dyn) # The height of the puzzle is the number of rows in the puzzle
            width = len(node.state.tab_dyn[0]) # The width of the puzzle is the number of columns in the puzzle
            state = deepcopy(Node.tab_stat) # Create a copy of the wall, space and obstacle of the puzzle, the copy is used to print the puzzle, the copy is used to avoid changing the wall, space and obstacle of the puzzle
            for i, j in itertools.product(range(height), range(width)): # Iterate over the rows and columns of the puzzle 
                if node.state.tab_dyn[i][j] == 'R': # Check if the current cell is the robot cell or not, 
                    if state[i][j] == ' ': # Check if the current cell is a space cell or not
                        state[i][j] = 'R' # If the current cell is a space cell, then change the current cell to the robot cell, 
                    else: # If the current cell is not a space cell, then the current cell is a box cell
                        state[i][j] = '.' # Change the current cell to the goal cell
                elif node.state.tab_dyn[i][j] == 'B': # Check if the current cell is a box cell or not
                    if state[i][j] == ' ': # Check if the current cell is a space cell or not
                        state[i][j] = 'B' # If the current cell is a space cell, then change the current cell to the box cell
                    else: # If the current cell is not a space cell, then the current cell is a goal cell
                        state[i][j] = '*' # Change the current cell to the goal cell                 
            solution.append(state) # Add the current state to the solution
            node = node.parent # The current node is the parent node of the current node 
        solution = solution[::-1] # Reverse the solution, the solution is generated by backtracking from the goal node to the root node, so the solution is generated by reversing the moves attribute of the class Node, the moves are stored in the order of the moves that lead to the next state, so the solution is generated by reversing the moves attribute of the class Node
        return solution # Return the solution of the search problem 
    
    # Choose one of the available heuristics
    def costHeur(self, heuristic=1): # Return the cost of the current node
        heuristics = {1: self.heuristic1(),
                    2: self.heuristic2(),
                    3: self.heuristic3()} # The available heuristics are stored in a dictionary, the keys of the dictionary are the numbers of the heuristics, and the values of the dictionary are the values of the heuristics
        self.cost = self.cost + heuristics[heuristic] # The cost of the current node is the cost of the parent node plus the cost of the move plus the value of the heuristic
        
    
    """ First heuristic: Number of left storages """
    def heuristic1(self): # Return the value of the first heuristic, the value of the first heuristic is the number of left storages, the number of left storages is the number of goal cells that are not occupied by a box

        # Retrieve all the storage cells
        tab_stat = np.array(Node.tab_stat) # Convert the wall, space and obstacle of the puzzle to a numpy array, the numpy array is used to find the storage cells, the storage cells are the cells that are not walls, spaces or obstacles
        S_indices_x, S_indices_y = np.where(tab_stat == 'S') # Find the indices of the storage cells, the indices are stored in two lists, the first list is the list of the indices of the rows of the storage cells, and the second list is the list of the indices of the columns of the storage cells
        
        left_storage = len(S_indices_x) # The number of left storages is the number of storage cells
        # Count the number of the left storages
        for ind_x, ind_y in zip(S_indices_x, S_indices_y): # Iterate over the indices of the storage cells, zip is used to iterate over two lists at the same time
            if self.state.tab_dyn[ind_x][ind_y] == 'B': # Check if the current storage cell is occupied by a box or not
                left_storage -= 1 # If the current storage cell is occupied by a box, then decrease the number of left storages by one

        return left_storage # Return the value of the first heuristic

    """ Second heuristic: 2*Number of left storage cells + Min Manhattan Distance between blocks and storage goals """
    def heuristic2(self): # Return the value of the second heuristic, the value of the second heuristic is the number of left storages plus the minimum Manhattan distance between the blocks and the storage goals

        # Retrieve all the storage cells
        tab_stat = np.array(Node.tab_stat)
        S_indices_x, S_indices_y = np.where(tab_stat == 'S')

        # Retrieve all the blocks
        tab_dyn = np.array(self.state.tab_dyn)
        B_indices_x, B_indices_y = np.where(tab_dyn == 'B')

        sum_distance = 0
        storage_left = len(S_indices_x)
        for b_ind_x, b_ind_y in zip(B_indices_x, B_indices_y):

            # Get the distance between each box and the nearest storage
            min_distance = +inf
            for s_ind_x, s_ind_y in zip(S_indices_x, S_indices_y):
                distance = abs(b_ind_x-s_ind_x) +  abs(b_ind_y-s_ind_y)
                if distance == 0: storage_left -= 1
                if distance < min_distance:
                    min_distance = distance
            sum_distance += min_distance
        
        return sum_distance + 2*storage_left

    """ Third heuristic: Min Manhattan Distance between blocks and storage goals + Min Manhattan Distance between the robot and the blocks 
                        + 2 * Number of left storage cells"""
    def heuristic3(self):

        # Retrieve all the storage cells
        tab_stat = np.array(Node.tab_stat)
        S_indices_x, S_indices_y = np.where(tab_stat == 'S')

        # Retrieve all the blocks
        tab_dyn = np.array(self.state.tab_dyn)
        B_indices_x, B_indices_y = np.where(tab_dyn == 'B')

        sum_distance = 0
        storage_left = len(S_indices_x)
        min_distance_br = +inf
        for b_ind_x, b_ind_y in zip(B_indices_x, B_indices_y):

            # Get the distance between each box and the robot
            distance_br = abs(b_ind_x-self.state.robot_position[0]) + abs(b_ind_y-self.state.robot_position[1])
            if distance_br < min_distance_br:
                min_distance_br = distance_br

            # Get the distance between each box and the nearest storage
            min_distance = +inf
            for s_ind_x, s_ind_y in zip(S_indices_x, S_indices_y):
                distance = abs(b_ind_x-s_ind_x) +  abs(b_ind_y-s_ind_y)
                if distance == 0: storage_left -= 1
                if distance < min_distance:
                    min_distance = distance
            sum_distance += min_distance
                        
        return sum_distance + min_distance_br + 2*storage_left

