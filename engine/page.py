import pygame,sys,json
from pygame import *
from engine.button import *

class Page():
	def __init__(self,winSize):
		self.winSize = winSize
		self.bg = None
		self.colors = {
			'white':(255, 255, 255),
			'black':(0, 0, 0),
			'green' : (0, 128, 0),
			'blue' : (0, 0, 255),
			'lightBlue' : (173, 216, 230),
			'orange' : (255, 165, 0),
			'pumpkin':(255, 117, 24),
			'amber':(255, 126, 0),
			'yellow' : (255, 255, 0),
			'grey' : (133, 133, 133),
			'silver':(192, 192, 192)
		}
		self.button = Button()
		self.button.colors = self.colors
		self.textDict = {}
		self.figuresDict = {}
	def checkColor(self,color):
		if(type(color)==str):
			color = self.colors[color]
		return(color)
	def setBG(self,var):
		if(type(var)==str):
			if(var.find('.')!=-1):
				bg = image.load(var)
			else:
				bg = Surface(self.winSize)
				bg.fill(self.colors[var])
		elif(type(var)==tuple):
			bg = Surface(self.winSize)
			bg.fill(var)
		self.bg = bg
	def createText(self,name,text,size=22,x=0,y=0,color=(0,0,0),font='fonts/UbuntuBold.ttf',align='center',width=0,height=0,antialiasing=15):
		textSurf = pygame.font.Font(font,size).render(text,antialiasing,color)
		textWidth = textSurf.get_width()
		textHeight = textSurf.get_height()
		if(align=='center'):
			x = x+((width-textWidth)/2)
			y = y+((height-textHeight)/2)
		elif(align=='right'):
			x = x+(width-textWidth)
			y = y+((height-textHeight)/2)
		elif(align=='left'):
			y = y+((height-textHeight)/2)
		self.textDict[name] = {'surface':textSurf,'text':text,'size':size,'font':font,'align':align,'color':color,'cord':(x,y),'antialiasing':antialiasing}
	def createRect(self,name,x,y,w,h,color=(0,0,0)):
		size = (int(w),int(h))
		rect = Surface(size)
		rect.fill(color)
		self.figuresDict[name] = {'surface':rect,'type':'rect','size':size,'color':color,'cord':(x,y)}
	def blitBG(self,screen):
		if(self.bg!=None):
			screen.blit(self.bg,(0,0))
	def blitButtons(self,screen,mousePos,mouseButton):
		self.button.checkEvent(mousePos,mouseButton)
		self.button.updateBlitList()
		self.button.useFunc()
		self.button.blit(screen)
	def blitText(self,screen):
		for i in self.textDict:
			text = self.textDict[i]
			screen.blit(text['surface'],text['cord'])
	def blitFigures(self,screen):
		for i in self.figuresDict:
			figure = self.figuresDict[i]
			screen.blit(figure['surface'],figure['cord'])
	def blit(self,screen,mousePos,mouseButton):
		self.blitBG(screen)
		self.blitButtons(screen,mousePos,mouseButton)
		self.blitText(screen)
		self.blitFigures(screen)