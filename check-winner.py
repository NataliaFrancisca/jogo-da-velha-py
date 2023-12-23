def check_winner(matrix, currentplayer):
    def check_rows():
        for x in range(3):
            if all(matrix[x][i] == currentplayer for i in range(3)):
                return True

    def check_cols():
        for x in range(3):
            if all(matrix[i][x] == currentplayer for i in range(3)):
                return True;
    
    def check_diagonals():
        if all(matrix[i][i] == currentplayer for i in range(3)):
            return True;
        
        if all(matrix[i][2-i] == currentplayer for i in range(3)):
            return True;
        
       
    ## THIS WORKS, BUT IS TOO BIG
    # def check_rows():
    #     for x in range(3):
    #         winner = True;
    #         for i in range(3):
    #             if(matrix[x][i] != currentplayer):
    #                 winner = False;
    #         if(winner == True):
    #             break;
    #     return winner;
    
    # def check_cols():
    #     for x in range(3):
    #         winner = True;
    #         for i in range(3):
    #             if(matrix[i][x] != currentplayer):
    #                 winner = False;
    #             print(matrix[i][x]);
    #         if(winner == True):
    #             break;
    #     return winner;
    
 
    rows = check_rows();
    cols = check_cols();
    diagonals = check_diagonals();
    
    return rows or cols or diagonals;

isWinner = check_winner([['X', 'O', 'X'], ['X', 'O', 'X'], ['O', 'X', 'X']], "O");
print(isWinner);