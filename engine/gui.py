import pygame,sys
from pygame import *
try:
	from engine import window
except:
	import window

class GUI():
	def __init__(self,standartWindow=None):
		pygame.init()
		pygame.font.init()
		self.clock = pygame.time.Clock()
		self.nowWin = None
		self.standartWindow = standartWindow
		self.winDict = {}
	def createWindow(self,name,winSize,caption=None,icon=None,winMode=0):
		self.winDict[name] = window.Window(winSize,caption,icon,winMode)
		if(self.standartWindow == None):
			self.standartWindow = name
	def getWindow(self,name):
		return(self.winDict[name])
	def blitWindow(self):
		if(self.nowWin == None):
			self.nowWin = self.standartWindow
		windowName = self.nowWin
		window = self.winDict[windowName]
		window.blitPage()
	def tick(self,num):
		self.clock.tick(num)