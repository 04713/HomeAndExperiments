import os; os.system('clear')
"""test player"""

class Player():
    def __init__(self, xpose, ypose, xspeed, yspeed):
        self.xpose = xpose
        self.ypose = ypose
        self.xspeed = xspeed
        self.yspeed = yspeed

    def move_x(self):
        self.xpose += self.xspeed

    def move_y(self):
        self.ypose += self.yspeed        

