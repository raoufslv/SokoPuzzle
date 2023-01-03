import numpy as np

""" Representations:
O => Obstacle
S => Storage
B => Block
R => Robot
* => Block on a storage
. => Robot on a storage """

class SokoPuzzle:

    def __init__(self, tab_dyn, robot_position): #tab_dyn is a 2D array of strings representing the state of the puzzle and robot_position is a tuple of ints representing the position of the robot    
        
        # Initialize the SokoPuzzle Board
        self.tab_dyn = tab_dyn
        self.robot_position = robot_position 
                
        # List of the robot's moves
        self.moves = ["U", "D", "L", "R"]        

    def isDeadLock(self, deadlock_map):
        # Retrieve all the storage cells
        S_indices_x, S_indices_y = np.where(np.logical_or(np.array(deadlock_map) == 'D', np.array(deadlock_map) == 'L')) # S_indices_x and S_indices_y are 1D arrays of ints representing the indices of the storage cells in the puzzle board
        
        # Check if the storage cells contain blocks
        for ind_x, ind_y in zip(S_indices_x, S_indices_y):
            if self.tab_dyn[ind_x][ind_y] == 'B':
                return True
        return False
    
    def isGoal(self, tab_stat): # Check if the puzzle is solved or not by checking if all the blocks are on a storage, tab_stat is a 2D array of strings representing the state of the puzzle

        # Retrieve all the storage cells
        S_indices_x, S_indices_y = np.where(np.array(tab_stat) == 'S') # S_indices_x and S_indices_y are 1D arrays of ints representing the indices of the storage cells in the puzzle board
        
        # Check if the storage cells contain blocks
        for ind_x, ind_y in zip(S_indices_x, S_indices_y):
            if self.tab_dyn[ind_x][ind_y] != 'B':
                return False
        return True

    def executeMove(self, action, tab_stat): # Execute the robot's move and return the new state of the puzzle board and the new position of the robot after the move is executed, action is a string representing the robot's move and tab_stat is a 2D array of strings representing the state of the puzzle
        if action == "U":
            return (self.up(tab_stat))  
        if action == "D":
            return (self.down(tab_stat))
        if action == "L":
            return (self.left(tab_stat))
        if action == "R":
            return (self.right(tab_stat))

    def up(self, tab_stat):

        # Get the robot position
        robot_x, robot_y = self.robot_position

        # Move the robot up: U => [-1, 0]
        robot_x = robot_x-1
        
        # Check if the robot is moving towards a block
        if self.tab_dyn[robot_x][robot_y] == 'B':
            # Moving the box
            box_x, box_y = robot_x-1, robot_y
            # If the robot is not pushing another box and is moving the box towards an empty space or storage
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x+1][robot_y] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True            

        else: # The robot is moving towards an empty space, a storage or a wall
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x+1][robot_y] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'                
                return True

        return False

    def down(self, tab_stat):

        # Get the robot position
        robot_x, robot_y = self.robot_position

        # Move the robot down: D => [1, 0]
        robot_x = robot_x+1

        # Check if the robot is moving towards a block
        if self.tab_dyn[robot_x][robot_y] == 'B':
            # Moving the box
            box_x, box_y = robot_x+1, robot_y
            # If the robot is not pushing another box and is moving the box towards an empty space or storage
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x-1][robot_y] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True
            
        else: # The robot is moving towards an empty space, a storage or a wall
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x-1][robot_y] = ' '
                self.tab_dyn[robot_x][robot_y] = 'R'                
                return True

        return False
            
    def left(self, tab_stat):

        # Get the robot position
        robot_x, robot_y = self.robot_position

        # Move the robot left: L => [0, -1]
        robot_y = robot_y-1

        # Check if the robot is moving towards a block
        if self.tab_dyn[robot_x][robot_y] == 'B':
            # Moving the box
            box_x, box_y = robot_x, robot_y-1
            # If the robot is not pushing another box and is moving the box towards an empty space or storage
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y+1] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True
            
        else: # The robot is moving towards a space, a storage or a wall
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y+1] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'                
                return True

        return False

    def right(self, tab_stat):

        # Get the robot position
        robot_x, robot_y = self.robot_position

        # Move the robot right: R => [0, 1]
        robot_y = robot_y+1

        # Check if the robot is moving towards a block
        if self.tab_dyn[robot_x][robot_y] == 'B':
            # Moving the box
            box_x, box_y = robot_x, robot_y+1
            # If the robot is not pushing another box and is moving the box towards an empty space or storage
            if self.tab_dyn[box_x][box_y] != 'B' and (tab_stat[box_x][box_y] == ' ' or tab_stat[box_x][box_y] == 'S'):
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y-1] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'
                self.tab_dyn[box_x][box_y] = 'B'
                return True
        
        else: # The robot is moving towards an empty space, a storage or a wall
            if tab_stat[robot_x][robot_y] == ' ' or tab_stat[robot_x][robot_y] == 'S':
                self.robot_position = (robot_x, robot_y)
                self.tab_dyn[robot_x][robot_y-1] = ' ' 
                self.tab_dyn[robot_x][robot_y] = 'R'                
                return True

        return False 

    



    
            
                






    

