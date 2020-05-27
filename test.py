# -*- coding: utf-8 -*-
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

    def move_minusx(self):
        self.xpose -= self.xspeed
    
    def move_y(self):
        self.ypose += self.yspeed

    def move_minusy(self):
        self.ypose -= self.yspeed

    def stat(self):
        print(self.xpose, self.ypose, self.xspeed, self.yspeed)
    
    def funkn(self):
        print(__name__)
