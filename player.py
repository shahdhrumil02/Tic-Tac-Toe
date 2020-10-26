from tkinter import *
from tic_tac_toe import tictactoe
class player_info:
    player1=''
    player2=''
    def __init__(self,root):
        self.game = Label(root,text="Tic-Tac-Toe Game", font= "freestylescript 30 bold italic", fg= "#82c8ed", bg="black")
        self.game.place(x=150, y=50)

        self.p1 = Label(root, text= "First Player X: ", font= "times 15 bold",bg="#e0cd6c")
        self.p1.place(x =140, y =140)

        self.p2 = Label(root, text= "Second Player O: ", font= "times 15 bold",bg="#e0cd6c")
        self.p2.place(x =120, y =200)

        self.p1_name = Entry(root, width = 15, bd=5, font= "times 10 bold")
        self.p1_name.place(x=280, y=140)
        
        self.p2_name = Entry(root, width = 15, bd=5, font= "times 10 bold")
        self.p2_name.place(x=280, y=200)

        self.submit = Button(root, text="Submit", bd=5, font="arial 12 bold", command= self.player_detail)
        self.submit.place(x=250,y=270)

    def player_detail(self):
        player1= self.p1_name.get()
        player2= self.p2_name.get() 
        #print(player1+"\n"+player2)
        tic = tictactoe(player1,player2)
        

def main():
    root = Tk()
    p = player_info(root)
    root.title("Tic Tac Toe")
    root.geometry("600x475")
    root.config(bg="#e0cd6c")
    root.resizable(False,False)
    root.mainloop() 

if __name__ == "__main__":
    main()       