import pygame,sys
from pygame import *

def changeWindow(name):
	gui.nowWin = name
def changePage(window,name):
	gui.winDict[window].nowPage = name
def create(gui):
	miniWinSize = (300,250)
	gui.createWindow('mini',miniWinSize,'VKInformer',winMode=pygame.NOFRAME)
	mini = gui.getWindow('mini')
	mini.createPage('main',miniWinSize)
	miniMain = mini.getPage('main')