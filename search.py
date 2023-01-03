from node import *
from collections import deque
from tkinter import *

class Search: # Search class

    @staticmethod # BFS search algorithm 
    def breadthFirst(initial_node, window, deadlock_detection= False): # initial_node is a Node object representing the initial state of the puzzle
        
        
        # Check if the start element is the goal
        if initial_node.state.isGoal(Node.tab_stat): # Node.tab_stat is a 2D array of strings representing the state of the puzzle
            return initial_node, 0 # Return the initial node and the number of nodes expanded
        elif deadlock_detection:
            if initial_node.state.isDeadLock(Node.deadlock_map):
                return None, -1

        # Create the OPEN FIFO queue and the CLOSED list
        open = deque([initial_node]) # A FIFO queue of Node objects
        closed = list() # A list of Node objects 
       
        step = 0 # Number of nodes expanded
        while True: # Loop until the goal is found or the OPEN queue is empty
            
            step +=1 # Increment the number of nodes expanded
            # print (f'*** Step {step} ***') # Print the current step
            
            #delete the last label if existed
            try:
                label12.destroy()
            except:
                pass

            label12 = Label(window, text=f'*** Step {step} ***', bg='#c45242', fg='white') #erreur de pas ecrire au meme temps de recherche 
            label12.pack()
            window.update()

            # Check if the OPEN queue is empty => goal not found 
            if len(open) == 0: # If the OPEN queue is empty
                return None, -1 # Return None and -1
            
            # Get the first element of the OPEN queue
            current = open.popleft() # current is a Node object
            
            
            
            # Put the current node in the CLOSED list
            closed.append(current) # current is a Node object
            
            if deadlock_detection:
                if current.state.isDeadLock(Node.deadlock_map):
                    continue
                        
            # Generate the successors of the current node
            succ = current.succ() # succ is a list of Node objects
            while len(succ) != 0: # Loop until the successors list is empty
                child = succ.popleft() # child is a Node object

                # Check if the child is not in the OPEN queue and the CLOSED list
                if (child.state.tab_dyn not in [n.state.tab_dyn for n in closed] and \
                    child.state.tab_dyn not in [n.state.tab_dyn for n in open]): 

                    # Put the child in the OPEN queue 
                    open.append(child) # child is a Node object  

                    # Check if the child is the goal
                    if child.state.isGoal(Node.tab_stat):
                        label12.destroy()  #delete the last label
                        return child, step      # Return the child node and the number of nodes expanded 
    
        
    @staticmethod #Astart algorithm
    def Astar(init_node, window, heuristique=1, deadlock_detection=False):
        # Check if the start element is the goal
        if init_node.state.isGoal(Node.tab_stat): # Node.tab_stat is a 2D array of strings representing the state of the puzzle
                return init_node, 0 # Return the initial node and the number of nodes expanded
        elif deadlock_detection:
            if init_node.state.isDeadLock(Node.deadlock_map):
                return None, -1
        
        init_node.costHeur(heuristique)
        # Create the OPEN priority queue and the CLOSED list
        open = deque([init_node]) # A priority queue of Node objects
        closed = list() # A list of Node objects
        step=0
        while True: # Loop until the goal is found or the OPEN queue is empty
            step +=1 # Increment the number of nodes expanded
            # print (f'*** Step {step} ***') # Print the current step
            
            #delete the last label if existed
            try:
                label123.destroy()
            except:
                pass
            
            label123 = Label(window, text=f'*** Step {step} ***', bg='#c45242', fg='white')   #erreur de pas ecrire au meme temps de recherche 
            label123.pack()
            window.update()
            
            # Check if the OPEN queue is empty => goal not found
            if len(open) == 0: # If the OPEN queue is empty
                return None, -1 # Return None and -1
            
            # sort the open list by the f value
            open = deque(sorted(list(open), key=lambda node: node.cost))

            # Get the first element of the OPEN queue
            current = open.popleft() # current is a Node object

            # Put the current node in the CLOSED list
            closed.append(current) # current is a Node object

            # check if the current node is the goal
            if current.state.isGoal(Node.tab_stat):
                label123.destroy()  #delete the last label
                return current, step # Return the child node and the number of nodes expanded
            elif deadlock_detection:
                if current.state.isDeadLock(Node.deadlock_map):
                    continue
            
            
            # Generate the successors of the current node
            succ = current.succ() # succ is a list of Node objects
            while len(succ) != 0: # Loop until the successors list is empty
                child = succ.popleft() # child is a Node object
                child.costHeur(heuristique)
                # Check if the child is not in the OPEN queue
                if (child.state.tab_dyn in [node.state.tab_dyn for node in open]):
                    index = [node.state.tab_dyn for node in open].index(child.state.tab_dyn)
                    if child.cost < open[index].cost:
                        open[index] = child
                # check if the child is not in CLOSED list
                elif(child.state.tab_dyn not in [node.state.tab_dyn for node in closed]):
                    # Put the child in the OPEN queue 
                    open.append(child)
                # check if the child is in CLOSED list    
                else:
                    index = [node.state.tab_dyn for node in closed].index(child.state.tab_dyn)
                    if child.cost < closed[index].cost:
                        closed.remove(closed[index])
                        open.append(child)

                            
            
                    


    