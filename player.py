class Player:
    def __init__(self, player="X"):
        self.player = player;
        
    def set(self, player):
        self.player = player;
        
    def get(self):
        return self.player;

    def switch(self):
        result = "O" if self.get() == "X" else "X";
        self.set(result);