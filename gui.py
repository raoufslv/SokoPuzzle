from tkinter import *
import itertools
import winsound
from search import Search
from sokoPuzzle import *
from node import *
import time

board1 = [['O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'S', ' ', 'B', ' ', 'O'],
        ['O', ' ', 'O', 'R', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O']]

board2 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'O'],
        ['O', ' ', ' ', 'O', 'O', 'O', ' ', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', 'O', '.', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
        ['O', ' ', ' ', 'B', ' ', ' ', 'O', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', ' ', 'O', ' ', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

board3 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', ' ', ' ', ' ', 'O', ' ', ' ', 'O'],
        ['O', ' ', ' ', 'B', 'R', ' ', ' ', 'O'],
        ['O', ' ', ' ', ' ', 'O', 'B', ' ', 'O'],
        ['O', 'O', 'O', 'O', 'O', ' ', 'S', 'O'],
        ['O', 'O', 'O', 'O', 'O', ' ', 'S', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

board4 = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', ' ', ' ', 'O', 'O', 'O'],
        ['O', 'O', ' ', ' ', 'O', 'O', 'O'],
        ['O', 'O', ' ', '*', ' ', ' ', 'O'],
        ['O', 'O', 'B', 'O', 'B', ' ', 'O'],
        ['O', ' ', 'S', 'R', 'S', ' ', 'O'],
        ['O', ' ', ' ', ' ', ' ', 'O', 'O'],
        ['O', 'O', 'O', ' ', ' ', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O']]

board5 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'S', 'O', ' ', ' ', 'O', 'O'],
        ['O', ' ', ' ', ' ', ' ', 'B', ' ', 'O', 'O'],
        ['O', ' ', 'B', ' ', 'R', ' ', ' ', 'S', 'O'],
        ['O', 'O', 'O', ' ', 'O', ' ', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'B', 'O', ' ', 'O', 'O', 'O'],
        ['O', 'O', 'O', ' ', ' ', 'S', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

board8 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', ' ', 'R', ' ', ' ', ' ', ' ', 'O', ' ', ' ', 'O'],
          ['O', ' ', 'B', ' ', 'B', ' ', 'B', ' ', ' ', ' ', 'O'],
          ['O', ' ', 'B', 'O', 'O', 'O', 'O', ' ', 'B', ' ', 'O'],
          ['O', 'O', ' ', ' ', 'S', 'S', 'S', 'O', ' ', 'O', 'O'],
          ['O', 'O', 'S', 'S', 'S', '*', ' ', 'B', ' ', ' ', 'O'],
          ['O', 'O', ' ', 'O', '*', ' ', 'O', ' ', ' ', ' ', 'O'],
          ['O', 'O', ' ', ' ', ' ', ' ', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]


#--------------------------- Extra Levels To Test ---------------------------#
#--------------------------- Astar - Heuristique3 ---------------------------#

EXboard1 = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'S', ' ', 'O', ' ', 'R', 'O'],
          ['O', ' ', ' ', 'O', 'B', ' ', 'O'],
          ['O', 'S', ' ', ' ', 'B', ' ', 'O'],
          ['O', ' ', ' ', 'O', 'B', ' ', 'O'],
          ['O', 'S', ' ', 'O', ' ', ' ', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard2 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'S', 'S', 'S', ' ', 'O', 'O', 'O'],
          ['O', ' ', 'S', ' ', 'B', ' ', ' ', 'O'],
          ['O', ' ', ' ', 'B', 'B', 'B', ' ', 'O'],
          ['O', 'O', 'O', 'O', ' ', ' ', 'R', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard3 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', ' ', ' ', ' ', ' ', 'O', 'O', 'O'],
          ['O', ' ', ' ', ' ', 'B', ' ', ' ', 'O'],
          ['O', 'S', 'S', 'S', '*', 'B', 'R', 'O'],
          ['O', ' ', ' ', ' ', 'B', ' ', ' ', 'O'],
          ['O', ' ', ' ', ' ', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

EXboard4 = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'S', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', ' ', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'S', ' ', 'S', ' ', 'O', 'O', 'O', 'O'],
            ['O', ' ', 'B', ' ', 'B', 'B', ' ', ' ', 'O'],
            ['O', 'O', 'O', 'S', ' ', ' ', 'B', 'R', 'O'],
            ['O', 'O', 'O', ' ', ' ', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]


#-------------------------------------------------------      Gui_class (pour l'interface de level)     ---------------------------------------------------------------------------------------


class Gui:
    def __init__(self, board, search_algo, deadlock_detection, type ="watch", num_step_level = 0):  # passer comme paremetre le nom de search_algo, si avec detection de deadlock ou pas (deadlock_detection) et le type de jeux, et le nombre minimal de step pour ce niveau(each one of them is declared manualy,(pour le type de jeux "play"))
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=63*self.width, height=63*self.height)
        self.canvas.pack()
        self.search_algo = search_algo
        self.final_steps = False
        self.legnth_solution = 0
        self.num_steps = 0
        self.deadlock_detection = deadlock_detection
        self.type = type
        self.num_step_level = num_step_level
        
        
        
        #make a button to close the window
        self.button = Button(self.window, text="Exit", padx=10, bg='#263D42', pady=4, command=self.close)
        self.button.pack(side=RIGHT)
        
        # make a button to back to the level
        self.button = Button(self.window, text="Back", padx=10, bg='#263D42', pady=4, command=self.Back)
        self.button.pack(side=LEFT)
        
        if self.type == "watch":
            # make a button to start the search
            self.button = Button(self.window, text="Start", padx=10, bg='#263D42', pady=4, command=self.start)
            self.button.pack()

        if self.type == "play":
            self.step_parcouru = 0
            self.initial_node, self.sokoPuzzle = create_initial_node(self.board, type='play')            
            #listen to the keyboard for the arrdzqsqzows keys and move the robot with the functions located in the class SokoPuzzle, then update the board with the function update_board located in the class Gui
            self.window.bind('<KeyPress>', self.move) # 
                
        
        
        # vider Node.deadlock_map pour si l'utilsateur a fait le button 'back' aprés a rentrer dans le level
        Node.deadlock_map = [] 
        self.draw_board()
        
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def start(self):
        show_solution(self, self.board, self.search_algo, self.deadlock_detection, self.window)

    def close(self):
        self.window.destroy()
        
    def Back(self):
        self.window.destroy()
        Level(self.search_algo, self.deadlock_detection, type=self.type)

    def draw_board(self,final_steps=False):
        # recuperer les photos
        self.obstacle = PhotoImage(file="images/obstacle.png")
        self.vide = PhotoImage(file="images/vide.png")
        self.cible = PhotoImage(file="images/cible.png")
        self.cibla = PhotoImage(file="images/cibla.png")
        self.robot = PhotoImage(file="images/robot.png")
        self.bloc = PhotoImage(file="images/bloc.png")
        self.blocible = PhotoImage(file="images/blocible.png")
        self.DeadCoin = PhotoImage(file="images/DeadCoin.png")
        self.DeadLigne = PhotoImage(file="images/DeadLigne.png")

        for i, j in itertools.product(range(self.height), range(self.width)): # placer les photos sur le window
            if self.board[i][j] == 'O':
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.obstacle)
            elif self.board[i][j] == 'S':
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.vide)
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.cible)
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.cibla)
            elif self.board[i][j] == 'B':
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.bloc)
            elif self.board[i][j] == 'R':
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.vide)
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.robot)
            elif self.board[i][j] == '*':
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.blocible)
            elif self.board[i][j] == '.':
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.vide)
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.cible)
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.robot)
            else:
                self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.vide)
                
            # tester si la case est une deadlock coin ou line par tester dans la matrice deadlock_map
            # tester si deadlock_map est declarer ou pas encore
            
            try: # on a fait la notion 'try-except' pour si l'utilisateur a pas utiliser la detection de deadlock, ou si il a utilisé mais cet itération c'est la premiere itération donc on ne draw pas les Deadlock(on l'affiche seulement dans la periode de solution) 
                if self.deadlock_detection: 
                    if Node.deadlock_map[i][j] == 'D':
                        self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.DeadCoin)
                    elif Node.deadlock_map[i][j] == 'L':
                        self.canvas.create_image(63*j, 63*i, anchor=NW, image=self.DeadLigne)
            except:
                pass
        
        if self.final_steps: # si cet itéraion est la derniere, donc on fait des messages
            if self.deadlock_detection:
                self.label = Label(self.window, text="L'algorithme de "+ self.search_algo + " avec detection de deadlock : ", bg='green', fg='white')
            else:
                self.label = Label(self.window, text="L'algorithme de "+ self.search_algo + " sans detection de deadlock : ", bg='green', fg='white')
            self.label.pack()
            # make a label to show the number of steps de l'algorithme
            self.label = Label(self.window, text="Nombre de steps utilisé par cet algorithme : " + str(self.num_steps), bg='#c45242', fg='white')
            self.label.pack()
            
            # make a label to show the number of steps necessaire pour resoudre le probleme
            self.label = Label(self.window, text="Nombre de steps minimum pour gagner est : " + str(self.legnth_solution), bg='#c45242', fg='white')
            self.label.pack()
                 
    def update_board(self, board, final_steps=False, legnth_solution=0, num_steps=0):
        self.final_steps = final_steps
        self.legnth_solution = legnth_solution
        self.num_steps = num_steps
        self.board = board
        self.canvas.delete("all")
        self.draw_board()
        self.window.update()
 
    def move(self, event):  #pour jouer le jeux
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.Bloean = False
            #move the robot to the left
            if event.keysym == 'Left':
                self.Bloean = self.sokoPuzzle.left(self.initial_node.tab_stat)
            #move the robot to the right
            elif event.keysym == 'Right':
                self.Bloean = self.sokoPuzzle.right(self.initial_node.tab_stat)
            #move the robot to the top
            elif event.keysym == 'Up':
                self.Bloean = self.initial_node.state.up(self.initial_node.tab_stat)
            #move the robot to the bottom
            elif event.keysym == 'Down':
                self.Bloean = self.initial_node.state.down(self.initial_node.tab_stat)
            
            if self.Bloean:
                self.step_parcouru = self.step_parcouru + 1
            else:
                # make a sound when the robot can't move, but let the user continue to play when the sound is playing
                winsound.PlaySound('sounds/bababooey.wav', winsound.SND_ASYNC) 

                
            height = len(self.initial_node.state.tab_dyn) # The height of the puzzle is the number of rows in the puzzle
            width = len(self.initial_node.state.tab_dyn[0]) # The width of the puzzle is the number of columns in the puzzle
            state = deepcopy(Node.tab_stat) # Create a copy of the wall, space and obstacle of the puzzle, the copy is used to print the puzzle, the copy is used to avoid changing the wall, space and obstacle of the puzzle
            for i, j in itertools.product(range(height), range(width)): # Iterate over the rows and columns of the puzzle 
                if self.initial_node.state.tab_dyn[i][j] == 'R': # Check if the current cell is the robot cell or not, 
                    if state[i][j] == ' ': # Check if the current cell is a space cell or not
                        state[i][j] = 'R' # If the current cell is a space cell, then change the current cell to the robot cell, 
                    else: # If the current cell is not a space cell, then the current cell is a box cell
                        state[i][j] = '.' # Change the current cell to the goal cell
                elif self.initial_node.state.tab_dyn[i][j] == 'B': # Check if the current cell is a box cell or not
                    if state[i][j] == ' ': # Check if the current cell is a space cell or not
                        state[i][j] = 'B' # If the current cell is a space cell, then change the current cell to the box cell
                    else: # If the current cell is not a space cell, then the current cell is a goal cell
                        state[i][j] = '*' # Change the current cell to the goal cell  
                
                
                        
            #update the board            
            self.update_board(state)
            #if is i goal state, then write a message
            if self.initial_node.state.isGoal(self.initial_node.tab_stat):
                self.label = Label(self.window, text="Bravo, vous avez gagné", bg='green', fg='white')
                self.label.pack()
                if self.step_parcouru == self.num_step_level:
                    self.label = Label(self.window, text="Et avec le nombre de steps minimum !!! ("+str(self.step_parcouru) +")", bg='green', fg='white')
                    self.label.pack()
                else:
                    self.label = Label(self.window, text="vous avez fait " + str(self.step_parcouru) + " de step", bg='#c45242', fg='white')
                    self.label.pack()
                    self.label = Label(self.window, text="le nombre minimal est : " + str(self.num_step_level), bg='#c45242', fg='white')
                    self.label.pack()
                self.window.update()
                self.window.unbind("<Key>")
                self.window.eval('tk::PlaceWindow . center')
                self.window.mainloop()
                return

        
        
#--------------------------------------------------------         start_game_class (la premeire page de jeux)        ---------------------------------------------------------------------------------------

class start_game_class:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=300, height=300)
        self.canvas.pack()
        
        self.bg = PhotoImage(file="images/bg.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
        

        # make a button to start the game
        self.button0 = Button(self.window,text="Start game", padx=5, bg='#33EE88', pady=2, command=self.start_game)
        button0_canvas = self.canvas.create_window( 115, 260, 
                                       anchor = "nw",
                                       window = self.button0)
        
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()
        
    def start_game(self):
        self.window.destroy()
        choice()
    


#---------------------------------------------------------         start_game_class(pour choisir le type de jeux)        ---------------------------------------------------------------------------------------

class choice: #make the user choose if he want to play or to see the algorithm in action
    def __init__(self):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        
        self.bg = PhotoImage(file="images/bg_sokoban.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
        
        #make a heading label saying "what do you want to do ?"
        self.label = Label(self.window, text="What do you want to do ?", bg='#c45242', font=("Arial", 18))
        # make it pretty by adding some padding around the text and raduis to the corners of the label
        self.label.config(padx=3, pady=2, borderwidth=2)
        label_canvas = self.canvas.create_window( 20, 60,
                                        anchor = "nw",
                                        window = self.label)
        
        # make a button to start the game
        self.button0 = Button(self.window,text="Be the one who plays", padx=5, bg='#33EE88', pady=3, font=("Arial", 13), command=self.start_game)
        button0_canvas = self.canvas.create_window( 60, 150, 
                                       anchor = "nw",
                                       window = self.button0)
        
        # make a button to start the game
        self.button1 = Button(self.window,text="Watch the algorithms in action", padx=5, bg='#33EE88', pady=3, font=("Arial", 13), command=self.start_game2)
        button1_canvas = self.canvas.create_window( 60, 220, 
                                       anchor = "nw",
                                       window = self.button1)
        
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()

    def start_game(self):
        self.window.destroy()
        Level(type='play')

    def start_game2(self):
        self.window.destroy()
        search_method()
        
        
#--------------------------------------------------------------------         search_method class(pour choisir algorithme de recherche)        ---------------------------------------------------------------------------------------
    
class search_method:
    def __init__(self):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.pack()
    
        self.bg = PhotoImage(file="images/bg_sokoban.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
        
        # make a button Back
        self.button0 = Button(self.window,text="Back", padx=5, bg='#537365', pady=2, command=self.Back)
        button0_canvas = self.canvas.create_window( 20, 20, 
                                       anchor = "nw",
                                       window = self.button0)
        # make a button Exit
        self.button0 = Button(self.window,text="Exit", padx=5, bg='#537365', pady=2, command=self.Exit)
        button0_canvas = self.canvas.create_window( 350, 20, 
                                       anchor = "nw",
                                       window = self.button0)
        
        # add a text label to the window
        self.label = Label(self.window, text="Choose a search method :",bg='#c45242', font=("Arial", 18))
        # make it pretty by adding some padding around the text and raduis to the corners of the label
        self.label.config(padx=3, pady=2, borderwidth=2)
        label_canvas = self.canvas.create_window( 20, 60,
                                        anchor = "nw",
                                        window = self.label)

        
        # make a button to start the game
        self.button0 = Button(self.window,text="Breadth First", padx=5, bg='#559776', font=("Arial", 13), pady=1, command=self.BFS)
        button0_canvas = self.canvas.create_window( 70, 130, 
                                       anchor = "nw",
                                       window = self.button0)
        
        self.button0 = Button(self.window,text="Astar avec heuristic 1", padx=5, bg='#559776', font=("Arial", 13), pady=1, command=self.Astar1)
        button0_canvas = self.canvas.create_window( 70, 170, 
                                       anchor = "nw",
                                       window = self.button0)
        
        self.button0 = Button(self.window,text="Astar avec heuristic 2", padx=5, bg='#559776', font=("Arial", 13), pady=1, command=self.Astar2)
        button0_canvas = self.canvas.create_window( 70, 210, 
                                       anchor = "nw",
                                       window = self.button0)
        
        self.button0 = Button(self.window,text="Astar avec heuristic 3", padx=5, bg='#559776', font=("Arial", 13), pady=1, command=self.Astar3)
        button0_canvas = self.canvas.create_window( 70, 250, 
                                       anchor = "nw",
                                       window = self.button0)
        
        # make a check box to choose if we want to use deadlock detection or not
        self.var = IntVar()
        self.check = Checkbutton(self.window, text="Avec detection de deadlock", variable=self.var, bg='#559776', font=("Arial", 13))
        self.check.config(padx=5, pady=1, borderwidth=2)
        check_canvas = self.canvas.create_window( 70, 290,
                                        anchor = "nw",
                                        window = self.check)
        
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()
    
    def Back(self):
        self.window.destroy()
        choice()
        
    def Exit(self):
        self.window.destroy()
        
    def BFS(self):
        self.window.destroy()
        #recuperer la valeur de la check box
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False

        Level("BFS", deadlock_detection, "watch")
    
    def Astar1(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("Astar,heuristic1", deadlock_detection, "watch")
        
    def Astar2(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("Astar,heuristic2", deadlock_detection, "watch")
        
    def Astar3(self):
        self.window.destroy()
        if self.var.get() == 1:
            deadlock_detection = True
        else:
            deadlock_detection = False
        Level("Astar,heuristic3", deadlock_detection, "watch")
        
        

#--------------------------------------------------------------------         Level class(pour choisir le level)        ---------------------------------------------------------------------------------------
       
class Level:
    def __init__(self, search_algo = "BFS", deadlock_detection = False, type = "watch"):
        self.window = Tk()
        self.window.title("Sokoban")
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        self.search_algo = search_algo
        self.deadlock_detection = deadlock_detection
        self.type = type
        
        self.bg = PhotoImage(file="images/bg_sokoban.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg)
        

        # make a button Back
        self.button0 = Button(self.window,text="Back", padx=5, bg='#537365', pady=2, command=self.Back)
        button0_canvas = self.canvas.create_window( 20, 20, 
                                       anchor = "nw",
                                       window = self.button0)
        # make a button Exit
        self.button0 = Button(self.window,text="Exit", padx=5, bg='#537365', pady=2, command=self.Exit)
        button0_canvas = self.canvas.create_window( 350, 20, 
                                       anchor = "nw",
                                       window = self.button0)
        self.button1 = Button(self.window,text="Level 1", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.level1)
        button1_canvas = self.canvas.create_window( 70, 70, 
                                       anchor = "nw",
                                       window = self.button1)
        # make the font size bigger for the button

        
        self.button2 = Button(self.window,text="Level 2", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.level2)
        button2_canvas = self.canvas.create_window( 70, 120, 
                                       anchor = "nw",
                                       window = self.button2)
        self.button3 = Button(self.window,text="Level 3", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.level3)
        button3_canvas = self.canvas.create_window( 70, 170, 
                                       anchor = "nw",
                                       window = self.button3)
        self.button4 = Button(self.window,text="Level 4", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.level4)
        button4_canvas = self.canvas.create_window( 70, 220, 
                                       anchor = "nw",
                                       window = self.button4)
        self.button5 = Button(self.window,text="Level 5", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.level5)
        button5_canvas = self.canvas.create_window( 70, 270, 
                                       anchor = "nw",
                                       window = self.button5)
        
        
        self.buttonEXTRA1 = Button(self.window,text="EXTRA Level 1", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.levelEXTRA1)
        buttonEXTRA1_canvas = self.canvas.create_window( 200, 70, 
                                       anchor = "nw",
                                       window = self.buttonEXTRA1)
        
        self.buttonEXTRA2 = Button(self.window,text="EXTRA Level 2", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.levelEXTRA2)
        buttonEXTRA2_canvas = self.canvas.create_window( 200, 120, 
                                       anchor = "nw",
                                       window = self.buttonEXTRA2)
        
        self.buttonEXTRA3 = Button(self.window,text="EXTRA Level 3", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.levelEXTRA3)
        buttonEXTRA3_canvas = self.canvas.create_window( 200, 170, 
                                       anchor = "nw",
                                       window = self.buttonEXTRA3)
        
        self.buttonEXTRA4 = Button(self.window,text="EXTRA Level 4", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.levelEXTRA4)
        buttonEXTRA4_canvas = self.canvas.create_window( 200, 220, 
                                       anchor = "nw",
                                       window = self.buttonEXTRA4)
        
        self.button8 = Button(self.window,text="EXTRA Level X", padx=5, bg='#c45242', pady=2, font=("Arial", 13), command=self.level8)
        button8_canvas = self.canvas.create_window( 200, 270, 
                                       anchor = "nw",
                                       window = self.button8)
        
        self.window.eval('tk::PlaceWindow . center')
        self.window.mainloop()
        
    
    def Back(self):
        self.window.destroy()
        if self.type == "watch":
            search_method()
        elif self.type == "play":
            choice()
        
    def Exit(self):
        self.window.destroy()
        
        
    def level1(self):
        self.window.destroy()
        Gui(board1,self.search_algo, self.deadlock_detection, self.type, 4)
        
    def level2(self):
        self.window.destroy()
        Gui(board2,self.search_algo, self.deadlock_detection, self.type, 29)
    
    def level3(self):
        self.window.destroy()
        Gui(board3,self.search_algo, self.deadlock_detection, self.type, 33)
    
    def level4(self):
        self.window.destroy()
        Gui(board4,self.search_algo, self.deadlock_detection, self.type, 30)
    
    def level5(self):
        self.window.destroy()
        Gui(board5,self.search_algo, self.deadlock_detection, self.type, 25)
    
    def level8(self):
        self.window.destroy()
        Gui(board8,self.search_algo, self.deadlock_detection, self.type, 0)
        
    def levelEXTRA1(self):
        self.window.destroy()
        Gui(EXboard1,self.search_algo, self.deadlock_detection, self.type, 41)
        
    def levelEXTRA2(self):
        self.window.destroy()
        Gui(EXboard2,self.search_algo, self.deadlock_detection, self.type, 55)
    
    def levelEXTRA3(self):
        self.window.destroy()
        Gui(EXboard3,self.search_algo, self.deadlock_detection, self.type, 30)
    
    def levelEXTRA4(self):
        self.window.destroy()
        Gui(EXboard4,self.search_algo, self.deadlock_detection, self.type, 83)

            

#--------------------------------------------------------------------         create_initial_node Fonction (pour creer le noeud initial)       ---------------------------------------------------------------------------------------
    
def create_initial_node(board=None, type='watch'):        
        
        height = len(board)
        width = len(board[0])
                
        # deviser le tableau sur deux, un dynamique et un statique
        tab_dyn = [['']*width for _ in range(height)]
        tab_stat = [['']*width for _ in range(height)]
        deadlock_map = [['']*width for _ in range(height)] # initialiser la variable
        
        for i, j in itertools.product(range(height), range(width)):
            if board[i][j] == 'R':
                robot_position = (i, j) 
                tab_dyn[i][j] = 'R'
                tab_stat[i][j] = ' '
            elif board[i][j] == 'B':
                tab_dyn[i][j] = 'B'
                tab_stat[i][j] = ' '
            elif board[i][j] == 'S' or board[i][j] == 'O' or board[i][j] == ' ':
                tab_dyn[i][j] = ' '   
                tab_stat[i][j] = board[i][j]         
            elif board[i][j] == '*':
                tab_dyn[i][j] = 'B'
                tab_stat[i][j] = 'S'
            else: # self.board[i][j] == '.'
                robot_position = (i, j) 
                tab_dyn[i][j] = 'R'
                tab_stat[i][j] = 'S'

        Node.tab_stat = tab_stat # Create the static board 
        
        # remplire deadlock_map avec D dans les coins bloqué
        for i, j in itertools.product(range(height), range(width)):
            if(tab_stat[i][j] == ' ' and tab_stat[i][j-1] == 'O' and tab_stat[i-1][j] == 'O') or (tab_stat[i][j] == ' ' and tab_stat[i][j+1] == 'O' and tab_stat[i-1][j] == 'O') or (tab_stat[i][j] == ' ' and tab_stat[i][j-1] == 'O' and tab_stat[i+1][j] == 'O') or (tab_stat[i][j] == ' ' and tab_stat[i][j+1] == 'O' and tab_stat[i+1][j] == 'O'):
                deadlock_map[i][j] = 'D'
            else:
                deadlock_map[i][j] = ' '
                
        
        # remplire deadlock_map avec L ou il existe des deadlocks lineaires
        for i, j in itertools.product(range(height), range(width)):
            
            if deadlock_map[i][j] == 'D':
                # verifier quel coin est bloqué de les 4 coins
                # enft on verifier just deux coins (top gauche et bottom droit) et pour chaque coin on verifer vertical et horizontal
                
                # on commence avec le coin top gauche
                if tab_stat[i][j-1] == 'O' and tab_stat[i-1][j] == 'O':
                    
                    # verifier si il existe un deadlock lineaire en horizontal
                    deadlock_line = False
                    for k in range(j+1, width):
                        if deadlock_map[i][k] == 'D':
                            deadlock_line = True
                            break
                        elif Node.tab_stat[i][k] != ' ' or Node.tab_stat[i-1][k] != 'O':
                            deadlock_line = False
                            break
                    #fin de boucle
                    if deadlock_line:
                        for k in range(j+1, k):
                            deadlock_map[i][k] = 'L'
                    
                    # verifier si il existe un deadlock lineaire en vertical
                    deadlock_line = False        
                    for k in range(i+1, height):
                        if deadlock_map[k][j] == 'D':
                            deadlock_line = True
                            break
                        elif Node.tab_stat[k][j] != ' ' or Node.tab_stat[k][j-1] != 'O':
                            deadlock_line = False
                            break
                    if deadlock_line:
                        for k in range(i+1, k):
                            deadlock_map[k][j] = 'L'
                        
                # et maintenent avec le coin bottom droit            
                elif tab_stat[i][j+1] == 'O' and tab_stat[i+1][j] == 'O':
                    deadlock_line = False
                    for k in range(j-1, 0, -1):
                        if deadlock_map[i][k] == 'D':
                            deadlock_line = True
                            break
                        elif Node.tab_stat[i][k] != ' ' or Node.tab_stat[i+1][k] != 'O':
                            deadlock_line = False
                            break
                    if deadlock_line:
                        for k in range(j-1, k, -1):
                            deadlock_map[i][k] = 'L'
                    
                    deadlock_line = False
                    for k in range(i-1, 0, -1):
                        if deadlock_map[k][j] == 'D':
                            deadlock_line = True
                            break
                        elif Node.tab_stat[k][j] != ' ' or Node.tab_stat[k][j+1] != 'O':
                            deadlock_line = False
                            break
                    if deadlock_line:
                        for k in range(i-1, k, -1):
                            deadlock_map[k][j] = 'L'
                            
        Node.deadlock_map = deadlock_map # Create the deadlock board
        sokoPuzzle = SokoPuzzle(tab_dyn, robot_position)
        initial_node = Node(sokoPuzzle)
        if type == 'watch':
            return initial_node # Return the initial node
        else:
            return initial_node, sokoPuzzle # cet return pour le type de jeux 'play'
            


#--------------------------------------------------------------------         show_solution Function(pour commence la recherche)       ---------------------------------------------------------------------------------------

def show_solution(gui, board, search_algo, deadlock_detection, window):
    initial_node = create_initial_node(board=board) # Create the initial nodes
    match search_algo:
        case 'BFS':
            goalNode, num_steps = Search.breadthFirst(initial_node, window, deadlock_detection)
        case 'Astar,heuristic1':
            goalNode, num_steps = Search.Astar(initial_node, window,1, deadlock_detection) # Search the solution
        case 'Astar,heuristic2':
            goalNode, num_steps = Search.Astar(initial_node, window,2, deadlock_detection) # Search the solution
        case 'Astar,heuristic3':
            goalNode, num_steps = Search.Astar(initial_node, window,3, deadlock_detection) # Search the solution
    if goalNode:
        solution = goalNode.getSolution()
        for action in solution:
            gui.update_board(action)
            time.sleep(0.05)  
        gui.update_board(action, True, len(solution)-1, num_steps)
        # print(f"\nla longeur de solution avec le noeud initial prise en compte est : {len(solution)}")
    else:
        labelerreur = Label(window, text=f'Optimal solution not found', bg='#c45242', fg='white')   #erreur de pas ecrire au meme temps de recherche 
        labelerreur.pack()
        window.update()
        #print ("Optimal solution not found") 
           
        
        
#--------------------------------------------------------------------         Main        ---------------------------------------------------------------------------------------

start_game_class()