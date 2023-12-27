import tkinter as tk;
from tkinter import messagebox, font;

class Game():
    root = tk.Tk();
    font.families();
    
    matrix_game = None;
    frame = None;
    
    currentPlayer = None;
    gameIsOver = None;
    
    def __init__(self):
        self.root.title('JOGO DA VELHA COM PYHTON')

        self.matrix_game = [[None, None, None], [None, None, None], [None, None, None]];
        self.currentPlayer = "X";
        self.gameIsOver = False;
        
        self.frame = tk.Frame(self.root, background='Light Green');
        self.frame.pack();
    
        self.welcomePage();
    
        
    def welcomePage(self):
        view = tk.Frame(self.frame, height=400, width=400, background='Light Green');
        
        titulo = tk.Label(view, text="JOGO DA VELHA COM PYTHON", font=('Lucida Sans', '16', 'bold'), background='Light Green');
        titulo.pack(padx=(100, 100));
        titulo.pack(pady=(20, 0));

        button = tk.Button(view, text='START', font=('Lucida Sans', '16', 'bold'), background='Pink', command=lambda: self.startGame(view));
        button.pack(padx=(100,100))
        button.pack(pady=(100, 20)); 
        
        view.pack();
    
    def startGame(self, view):
        view.destroy();
        self.createButtons();
        
    def createButtons(self):
        board_frame = tk.Frame(self.frame);
        
        for i in range(3):
            for j in range(3):
                self.matrix_game[i][j] = tk.Button(board_frame, text="", font=('Lucida Sans', '28', 'bold'), width=8, height=3, background="Pink", 
                                            command=lambda row=i, col=j: self.onClickButton(row, col))
                self.matrix_game[i][j].grid(row=i, column=j)

        board_frame.pack(padx=(50, 50));
        board_frame.pack(pady=(50, 50));
    
    def onClickButton(self, row, col):
        # check if the user clicked in a button that was already clicked
        if(self.matrix_game[row][col]['text'] != ""):
            return False;
            
        if(self.gameIsOver == False and self.matrix_game[row][col]['text'] == ""):
            self.matrix_game[row][col]['text'] = self.currentPlayer;
        
        if self.checkIsWinner(row, col):
            messagebox.showinfo("JOGO DA VELHA COM PYHTON", f"JOGADOR {self.currentPlayer} VENCEU!", icon=('info'));
            self.finishGame();
        elif self.checkIsDraw():
            messagebox.showinfo("JOGO DA VELHA COM PYHTON", "O JOGO TERMINOU EM EMPATE");
            self.finishGame();
        else:
            self.switchPlayer();
    
    def checkIsWinner(self, row, col):

        # check row
        if all(self.matrix_game[row][i]["text"] == self.currentPlayer for i in range(3)):
            return True  
           
        # check col
        if all(self.matrix_game[i][col]["text"] == self.currentPlayer for i in range(3)):
            return True;

        # check diagonals
        if all(self.matrix_game[i][i]["text"] == self.currentPlayer for i in range(3)):
            return True;
        
        if all(self.matrix_game[i][2-i]["text"] == self.currentPlayer for i in range(3)):
            return True;
    
        return False;
         
    def checkIsDraw(self):
        return all(self.matrix_game[i][j]["text"] != "" for i in range(3) for j in range(3))
    
    def switchPlayer(self):
        self.currentPlayer = "O" if self.currentPlayer == "X" else "X";
    
    def finishGame(self):
        self.gameIsOver = True;
        self.frame.destroy();
        self.__init__();
    

game = Game();
game.root.mainloop();

