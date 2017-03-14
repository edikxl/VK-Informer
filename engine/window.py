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
		if(self.caption!=None):
			pygame.display.set_caption(self.caption)
		if(type(self.icon)==str):
			pygame.display.set_icon(image.load(self.icon))
		#...
		self.nowPage = None
		self.standartPage = standartPage
		self.pageDict = {}
		self.afterBlitDict = {}
	def init(self):
		self.screen = pygame.display.set_mode(self.winSize,self.winMode)
	def updateAfterBlitDict(self,page,elemList):
		self.afterBlitDict[page].append(elemList)
	def checkExit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				break
	def createPage(self,name,winSize):
		self.pageDict[name] = page.Page(winSize)
		self.afterBlitDict[name] = []
		if(self.standartPage == None):
			self.standartPage = name
	def getPage(self,name):
		return(self.pageDict[name])
	def blitPage(self):
		self.checkExit()
		mousePos = pygame.mouse.get_pos()
		mouseButton = pygame.mouse.get_pressed()
		self.screen.blit(Surface(self.winSize),(0,0))
		if(self.nowPage == None):
			self.nowPage = self.standartPage
		pageName = self.nowPage
		page = self.pageDict[pageName]
		page.blit(self.screen,mousePos,mouseButton)
		for i in self.afterBlitDict[pageName]:
			if(i[0]=='figure'):
				page.blitFigures(self.screen,i[1])
			elif(i[0]=='text'):
				page.blitText(self.screen,i[1])
			elif(i[0]=='image'):
				page.blitImages(self.screen,i[1])
		pygame.display.update()