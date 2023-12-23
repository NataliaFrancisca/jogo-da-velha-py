import tkinter as tk;
from tkinter import messagebox, font

class Game:
    root = None;
    board = [[None, None, None], [None, None, None], [None, None, None]];
    
    def __init__(self, master=None):
        self.root = master;
        self.welcomePage();
        
    def welcomePage(self):
        self.fontePadrao = ("Lucida Sans", "10")
        
        frame = tk.Frame(self.root, height=500, width=500, background='Light Blue');
        frame['borderwidth'] = 2
        frame.pack();
        
        titulo = tk.Label(frame, text="JOGO DA VELHA COM PYTHON", font=('Lucida Sans', '16', 'bold'), background='Light Blue');
        titulo.pack(padx=(100, 100));
        titulo.pack(pady=(20, 0));
        
        button = tk.Button(frame, text='START', font=('Lucida Sans', '16', 'bold'), background='Yellow', command=lambda: self.startGame());
        button.pack(padx=(100,100))
        button.pack(pady=(100, 20));
        
    
    def startGame(self):
        game = tk.Toplevel();
        game.title("GAME");
        game.config(width=400, height=500, background='Light Green');
        
        self.createButtons(game);
        
        
    def createButtons(self, page=None):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = tk.Button(page, text="", font=('normal', 30), width=8, height=3,
                                             command=lambda row=i, col=j: self.click(row, col))
                self.board[i][j].grid(row=i, column=j)

        self.currentPlayer = "X";
        self.gameOver = False;
        
    def click(self, row, col):
        if(self.gameOver == False and self.board[row][col]['text'] == ""):
            self.board[row][col]['text'] = self.currentPlayer;
        
        if self.checkWinner(row, col):
            # print("Jogo da Velha", f"Jogador {self.currentPlayer} venceu!")
            messagebox.showinfo("Jogo da Velha", f"Jogador {self.currentPlayer} venceu!");
            self.game_over = True
        elif self.checkDraw():
            messagebox.showinfo("Jogo da Velha", "O jogo terminou em empate!");
            self.game_over = True;
        else:
            self.switchPlayer();
    
    def checkWinner(self, row, col):

        for x in range(3):
            print(self.board[x][col]);

        # check row
        if all(self.board[row][i]["text"] == self.currentPlayer for i in range(3)):
            return True  
           
        # check col
        if all(self.board[i][col]["text"] == self.currentPlayer for i in range(3)):
            return True;

        # check diagonals
        if all(self.board[i][i]["text"] == self.currentPlayer for i in range(3)):
            return True;
        
        if all(self.board[i][2-i]["text"] == self.currentPlayer for i in range(3)):
            return True;
    
        return False;
    
    def switchPlayer(self):
        self.currentPlayer = "O" if self.currentPlayer == 'X' else 'X';
        
    def checkDraw(self):
        return all(self.board[i][j]["text"] != "" for i in range(3) for j in range(3))
    
# game = Game();
# game.__init__();
# # game.createButtons();
# print(game.board);
# root.mainloop();

root = tk.Tk()
font.families()
root.title("Jogo da Velha")
Game(root)
root.mainloop()