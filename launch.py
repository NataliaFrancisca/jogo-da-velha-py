from view import View;

class Initialize:
    def __init__(self):
        self.view = View(self.restart);
        self.view.run();
    
    def restart(self):
        Initialize();
        
game = Initialize();

