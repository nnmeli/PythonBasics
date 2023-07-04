"""

Project 1 - Shall we play a game?


In this project, you are asked to implement functions that will 
enable you (and others) to play the game of sliders. 
The objective of this game is to form the board so that all the 
numbers are ordered on the board. Usually, there is an 
empty block that will let you move blocks around, but you will 
use number 0 for this purpose.

"""

my_name = "Muhammet Melih Tumur"
my_id = "200102002036"
my_email = "m.tumur2020@gtu.edu.tr"

import random

def generate(row,column):
    carpim=row*column
    sayilar=[]
    for i in range(carpim):
        sayilar.append(i)
    
    matrix=[]
    
    
    for i in range(2,carpim,row):
        while sayilar!=[]:
            #gecici_liste=[]
            gecici_liste=sayilar[:row]
            matrix.append(gecici_liste)
            for i in range(row):
                i*sayilar.pop(0)
                
            
           
    
    return matrix
            
def print_board(board):
   
   for i in range(len(board)):
       print(*board[i], sep = "\t" , ) 
       
    
    
def shuffle(board , times=20) :
    a=""
    
    
    for i in range(times) :
        a += move_random(board)
    
    return a
    
def get_board_size(board):
    sonuc=(len(board[0]), len(board))
    return sonuc
    
def move_right(board):
    
    for a in range(len(board)):    
        for i in board[a] :
            if i == 0 :
                if board[a].index(0) != (len(board[a])-1):                
                    konum=board[a].index(0)
                    board[a][konum],board[a][konum+1]=board[a][konum+1],board[a][konum]
                   
                    return 1
                else :
                    return 0
    
    
def move_left(board):
    
    for a in range(len(board)):    
        for i in board[a] :
            if i == 0 :
                if board[a].index(0) != 0:                
                    konum=board[a].index(0)
                    board[a][konum],board[a][konum-1]=board[a][konum-1],board[a][konum]
                   
                    return 1
                else :
                    return 0

def move_up(board):
    
    for a in range(len(board)):    
        for i in board[a] :
            if i == 0 :
                if board.index(board[a]) != 0:                
                    konum=board[a].index(0)
                    board[a][konum],board[a-1][konum]=board[a-1][konum],board[a][konum]
                   
                    return 1
                else :
                    return 0
    

def move_down(board):
    
    for a in range(len(board)):    
        for i in board[a] :
            if i == 0 :
                if board.index(board[a]) != (len(board)-1):               
                    konum=board[a].index(0)
                    board[a][konum],board[a+1][konum]=board[a+1][konum],board[a][konum]
                   
                    return 1
                else :
                    return 0
    
def reset(board):
    a=len(board[0])
    b=len(board)
    gecici_board = generate(a, b)
    for i in range(len(board)):
        board[i]=gecici_board[i]        
    
            
    
def is_solved(board):
    a=len(board[0])
    b=len(board)
    gecici_board = generate(a, b)
    if board == gecici_board:
        return True 
    else :
        return False 


def move(board, moves):
    a=list(moves)
    
    
    def mover(x):
        s=0
        if (x == "R" or x == "r") :
            s += move_right(board)
            
        if (x == "L" or x == "l" ) :
            s += move_left(board)
            
        if (x == "U" or x == "u")  :
            s += move_up(board)
            
        if (x == "D" or x == "d" ) :
            s += move_down(board)
            
        return s
    
    
    
    s=0
    for i in range(len(a)) :
        
        s += mover(a[i])
    return s
    
   
    
    
   
def rotate(board):
    board[:]=(list(zip(*board[:])))
    
    for i in range(len(board)) :
        
        board[i]=list(board[i][::-1])
        
        
   
def is_valid(board):
    a=[]
    for i in range(len(board)) :
        for k in board[i]:
            a.append(k)
    c=0
    for i in range(len(board)*len(board[0])) : 
        c+=1
    if sorted(a) == list(set(a)) :
        for i in a : 
            if i >= c :
                return False
            else :
                return True 
    else : 
        return False
            
         
        
def move_random(board):
    yonler=["L","R","U","D"]
    
    
    for i in range(10**1000) :
        yon=random.choice(yonler)
        if 0 < move(board, yon):
            break
    
    return yon
   
    

def play_interactive(board=None):
    #b=[]
    hamle=""
    if board == None : 
        row=int(input("Row Number :"))
        column=int(input("Column Number :"))
        board=generate(row, column)
        for i in range(20) :
            move_random(board)
        
    if is_valid(board) == False :
        return (" " , -2)


    def mover(x):
       s=0
       if (x == "R" or x == "r") :
           s += move_right(board)
           
       if (x == "L" or x == "l" ) :
           s += move_left(board)
           
       if (x == "U" or x == "u")  :
           s += move_up(board)
           
       if (x == "D" or x == "d" ) :
           s += move_down(board)
           
       return s
   
    
    
    for i in range(100**10000):
        if board == generate(len(board), len(board[0])) : 
            break
     
        print_board(board)
        giris=(input("Yon giriniz : "))
        
        if (giris == "q" or giris=="Q" ): 
            return hamle , -1
        elif  (giris == "M" or giris=="m") :
            hamle += move_random(board)
        if giris=="R" or giris=="r" or giris=="l" or giris=="L" or giris=="U" or giris=="u" or giris=="d" or giris=="D" :
            if mover(giris) == 1 :
                hamle += giris 
        else :
            print("Wrong Move")
        
    print_board(board)
    print(len(hamle))
    return hamle,len(hamle)
        

   
"""    
def play(board,moves):
    a=list(moves)
    s=0 
    if is_valid(board)==False :
        return -2
    
    if board == generate(len(board), len(board[0]) ):
        return 0
    
    for i in range(len(a)):
        if board == generate(len(board), len(board[0]) ):
            return s
            break
        else :
            s += move(board, a[i])
   
    return s
"""    
   







