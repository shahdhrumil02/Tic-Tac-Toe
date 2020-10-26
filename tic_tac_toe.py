from tkinter import *
from tkinter import messagebox

class tictactoe():
    total_moves = 0
    def __init__(self,p1,p2):
        self.player1_name = p1
        self.player2_name = p2
        #Toplevel.__init__(self)
        self.b = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
        self.d = [[0,0,0],
                 [0,0,0],
                 [0,0,0]]
        for i in range(3):
            for j in range(3):
                self.b[i][j]= Button(width = 4, font="times 60 bold", bg ="black", command= lambda r=i, c=j: self.write(r,c))
                self.b[i][j].grid(row= i,column=j)
        self.player = 'X'
        self.play = False

    def write(self,r,c):
        global total_moves
        if self.player == 'X' and self.d[r][c] == 0 and self.play == False:
            self.b[r][c].configure(text= 'X', fg="white")
            self.total_moves += 1
            self.d[r][c] = 'X'
            self.player='O'
            
        if self.player == 'O' and self.d[r][c] == 0 and self.play == False:
            self.b[r][c].configure(text= 'O', fg="white")
            self.total_moves += 1
            self.d[r][c]= 'O'
            self.player="X"

        self.winner(self.player1_name,self.player2_name)
    
    def winner(self,name1,name2):
        global total_moves
        for i in range(3):
            if self.d[i][0] == self.d[i][1] == self.d[i][2] != 0:
                if self.d[i][0] == self.d[i][1] == self.d[i][2] == 'X':
                    self.d[i][0] = self.b[i][0].configure(fg="red") 
                    self.d[i][1] = self.b[i][1].configure(fg="red")
                    self.d[i][2] = self.b[i][2].configure(fg="red")
                    messagebox.askokcancel("Result",name1+" Wins",icon="info")

                if self.d[i][0] == self.d[i][1] == self.d[i][2] == 'O':
                    self.d[i][0] = self.b[i][0].configure(fg="red") 
                    self.d[i][1] = self.b[i][1].configure(fg="red")
                    self.d[i][2] = self.b[i][2].configure(fg="red")
                    messagebox.askokcancel("Result",name2+" Wins",icon="info")

                self.play = True
                break

        for i in range(3):
            if self.d[0][i] == self.d[1][i] == self.d[2][i] != 0:
                if self.d[0][i]== self.d[1][i] == self.d[2][i] == 'X':
                    self.d[0][i] = self.b[0][i].configure(fg="red") 
                    self.d[1][i] = self.b[1][i].configure(fg="red")
                    self.d[2][i] = self.b[2][i].configure(fg="red")
                    messagebox.askokcancel("Result",name1+" Wins",icon="info")

                if self.d[0][i]== self.d[1][i] == self.d[2][i] == 'O':
                    self.d[0][i] = self.b[0][i].configure(fg="red") 
                    self.d[1][i] = self.b[1][i].configure(fg="red")
                    self.d[2][i] = self.b[2][i].configure(fg="red")
                    messagebox.askokcancel("Result",name2+" Wins",icon="info")

                self.play = True
                break
            
            if self.d[0][0] == self.d[1][1] == self.d[2][2] != 0:
                if self.d[0][0] == self.d[1][1] == self.d[2][2] == 'X':
                    self.d[0][0] = self.b[0][0].configure(fg = "red")
                    self.d[1][1] = self.b[1][1].configure(fg = "red")
                    self.d[2][2] = self.b[2][2].configure(fg = "red")
                    messagebox.askokcancel("Result",name1+" Wins",icon="info")

                if self.d[0][0] == self.d[1][1] == self.d[2][2] == 'O':
                    self.d[0][0] = self.b[0][0].configure(fg = "red")
                    self.d[1][1] = self.b[1][1].configure(fg = "red")
                    self.d[2][2] = self.b[2][2].configure(fg = "red")
                    messagebox.askokcancel("Result",name2+" Wins",icon="info")
                self.play = True
                break

            if self.d[2][0] == self.d[1][1] == self.d[0][2] != 0:
                if self.d[2][0] == self.d[1][1] == self.d[0][2] == 'X':
                    self.d[2][0] = self.b[2][0].configure(fg = "red")
                    self.d[1][1] = self.b[1][1].configure(fg = "red")
                    self.d[0][2] = self.b[0][2].configure(fg = "red")
                    messagebox.askokcancel("Result",name1+" Wins",icon="info")
                if self.d[2][0] == self.d[1][1] == self.d[0][2] == 'O':
                    self.d[2][0] = self.b[2][0].configure(fg = "red")
                    self.d[1][1] = self.b[1][1].configure(fg = "red")
                    self.d[0][2] = self.b[0][2].configure(fg = "red")
                    messagebox.askokcancel("Result",name2+" Wins",icon="info")
                self.play = True
                break

            if self.total_moves == 9:
                messagebox.showinfo("Result", "Game is Draw")
                break
