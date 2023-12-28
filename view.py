from player import Player;
from game import Game;

import tkinter as tk;
from tkinter import messagebox, font;

class View:
    def __init__(self, restart_callback):
        self.root = tk.Tk()
        self.frame = None;
        
        font.families();
        
        self.player = Player();
        self.game = Game(self.player);
        
        self.restart = restart_callback
        
        self.pageView();
        
    def pageView(self):
        self.frame = tk.Frame(self.root, background='Light Green', height=500, width=500);
        self.frame.pack();
        
        self.welcomeView();
        
    def welcomeView(self):
        view = tk.Frame(self.frame, height=400, width=400, background='Light Green');
        
        titulo = tk.Label(view, text="JOGO DA VELHA COM PYTHON", font=('Lucida Sans', '16', 'bold'), background='Light Green');
        titulo.pack(padx=(100, 100), pady=(20, 0))

        button = tk.Button(view, text='START', font=('Lucida Sans', '16', 'bold'), background='Pink', command=lambda: self.startGame(view));
        button.pack(padx=(100, 100))
        button.pack(pady=(100, 20)); 
        
        view.pack();

    def startGame(self, view):
        view.destroy();
        self.createGridButtons();
        
    def createGridButtons(self):
        grid_frame = tk.Frame(self.frame);
        
        for i in range(3):
            for j in range(3):
                self.game.matrix_game[i][j] = tk.Button(grid_frame, text="", font=('Lucida Sans', '28', 'bold'), width=8, height=3, background="Pink", 
                                            command=lambda row=i, col=j: self.onButtonClick(row, col))
                self.game.matrix_game[i][j].grid(row=i, column=j)

        grid_frame.pack(padx=(50, 50));
        grid_frame.pack(pady=(50, 50));

    def onButtonClick(self, row, col):
        if(self.game.matrix_game[row][col]['text'] != ""):
            return False;
        
        if(self.game.gameIsOver == False and self.game.matrix_game[row][col]['text'] == ""):
            self.game.matrix_game[row][col]['text'] = self.player.get();
        
        if(self.game.validateGame(row, col)):
            message = self.game.validateGame(row, col);
            messagebox.showinfo("JOGO DA VELHA COM PYTHON", message, icon=('info'));
            self.destroy();

    def run(self):
        self.root.mainloop()
        
    def destroy(self):
        self.root.withdraw()
        self.restart()