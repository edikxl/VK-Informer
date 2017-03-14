import pygame,sys,os
from pygame import *
try:
	from engine import window
except:
	import window

class GUI():
	def __init__(self,pos='rightTop',winSize=None,standartWindow=None):
		self.setWindowPos(pos,winSize)
		pygame.init()
		pygame.font.init()
		self.clock = pygame.time.Clock()
		self.nowWin = None
		self.standartWindow = standartWindow
		self.winDict = {}
	def getWinSize(self):
		import ctypes
		user32 = ctypes.windll.user32
		screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
		return(screensize)
	def setWindowPos(self,pos,winSize):
		windowSize = self.getWinSize()
		if(winSize==None):
			winSize = windowSize
		if(pos=='rightTop'):
			x = windowSize[0]-winSize[0]
			y = 0
		elif(pos=='rightBottom'):
			x = windowSize[0]-winSize[0]
			y = windowSize[1]-winSize[1]
		elif(pos=='leftBottom'):
			x = 0
			y = windowSize[1]-winSize[1]
		else:
			x = 0
			y = 0
		os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i'%(x,y)
	def createWindow(self,name,winSize,caption=None,icon=None,winMode=0):
		self.winDict[name] = window.Window(winSize,caption,icon,winMode)
		if(self.standartWindow == None):
			self.standartWindow = name
	def getWindow(self,name):
		return(self.winDict[name])
	def blitWindow(self):
		if(self.nowWin == None):
			self.nowWin = self.standartWindow
			self.winDict[self.nowWin].init()
		windowName = self.nowWin
		window = self.winDict[windowName]
		window.blitPage()
	def tick(self,num):
		self.clock.tick(num)