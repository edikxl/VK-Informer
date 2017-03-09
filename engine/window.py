import pygame,sys
from pygame import *
try:
	from engine import page
except:
	import page

class Window():
	def __init__(self,winSize,caption=None,icon=None,winMode=0,standartPage=None):
		self.winSize = winSize
		self.winMode = winMode
		self.caption = caption
		self.icon = icon
		self.screen = pygame.display.set_mode(self.winSize,self.winMode)
		if(self.caption!=None):
			pygame.display.set_caption(self.caption)
		if(type(self.icon)==str):
			pygame.display.set_icon(image.load(self.icon))
		#...
		self.nowPage = None
		self.standartPage = standartPage
		self.pageDict = {}	
	def checkExit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				break
	def createPage(self,name,winSize):
		self.pageDict[name] = page.Page(winSize)
		if(self.standartPage == None):
			self.standartPage = name
	def getPage(self,name):
		return(self.pageDict[name])
	def blitPage(self):
		self.checkExit()
		mousePos = pygame.mouse.get_pos()
		mouseButton = pygame.mouse.get_pressed()
		if(self.nowPage == None):
			self.nowPage = self.standartPage
		pageName = self.nowPage
		page = self.pageDict[pageName]
		page.blit(self.screen,mousePos,mouseButton)
		pygame.display.flip()