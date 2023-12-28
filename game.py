class Game:
    def __init__(self, player):
        self.gameIsOver = False;
        self.player = player;
        self.matrix_game = [[None, None, None], [None, None, None], [None, None, None]];
        
    def validateGame(self, row, col):
        if self.checkIsWinner(row, col):
            self.finishGame();
            return f"JOGADOR {self.player.get()} VENCEU!";
        elif self.checkIsDraw():
            self.finishGame();
            return "O JOGO TERMINOU EM EMPATE"
        else:
            self.player.switch();
    
    def checkIsWinner(self, row, col):
        currentPlayer = self.player.get();
        
        if all(self.matrix_game[row][i]["text"] == currentPlayer for i in range(3)):
            return True  
           
        if all(self.matrix_game[i][col]["text"] == currentPlayer for i in range(3)):
            return True;

        if all(self.matrix_game[i][i]["text"] == currentPlayer for i in range(3)):
            return True;
        
        if all(self.matrix_game[i][2-i]["text"] == currentPlayer for i in range(3)):
            return True;
    
        return False;

    def checkIsDraw(self):
        return all(self.matrix_game[i][j]["text"] != "" for i in range(3) for j in range(3))
    
    def finishGame(self):
        self.gameIsOver = True;