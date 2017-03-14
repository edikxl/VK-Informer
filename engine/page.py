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
		self.imagesDict = {}
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
	def createImage(self,name,x,y,path):
		self.imagesDict[name] = {'surface':image.load(path),'path':path,'cord':(x,y)}
	def createText(self,name,text,size=22,x=0,y=0,color=(0,0,0),font='fonts/UbuntuBold.ttf',align='own',width=0,height=0,antialiasing=15):
		self.textDict[name] = {'text':text,'size':size,'font':font,'align':align,'color':color,'width':width,'height':height,'x':x,'y':y,'antialiasing':antialiasing}
	def createRect(self,name,x,y,w,h,color=(0,0,0),width=0):
		self.figuresDict[name] = {'type':'rect','rect':(x,y,w,h),'color':color,'width':width}
	def createCircle(self,name,x,y,r,color=(0,0,0),width=0):
		self.figuresDict[name] = {'type':'circle','radius':r,'color':color,'pos':(x,y),'width':width}
	def createArc(self,name,rect,start,stop,color=(0,0,0),width=1):
		self.figuresDict[name] = {'type':'arc','rect':rect,'start':start,'stop':stop,'color':color,'width':width}
	def createLine(self,name,start,end,color=(0,0,0),width=1):
		self.figuresDict[name] = {'type':'line','start':start,'end':end,'color':color,'width':width}
	def blitBG(self,screen):
		if(self.bg!=None):
			screen.blit(self.bg,(0,0))
	def blitButtons(self,screen,mousePos,mouseButton):
		self.button.checkEvent(mousePos,mouseButton)
		self.button.updateBlitList()
		self.button.useFunc()
		self.button.blit(screen)
	def blitText(self,screen,name=None):
		textDict = self.textDict
		if(name!=None):
			textDict = {name:self.textDict[name]}
		for i in textDict:
			t = textDict[i]
			textSurf = pygame.font.Font(t['font'],t['size']).render(t['text'],t['antialiasing'],t['color'])
			textWidth = textSurf.get_width()
			textHeight = textSurf.get_height()
			x = t['x']
			y = t['y']
			if(t['align']=='center'):
				x = t['x']+((t['width']-textWidth)/2)
				y = t['y']+((t['height']-textHeight)/2)
			elif(t['align']=='right'):
				x = t['x']+(t['width']-textWidth)
				y = t['y']+((t['height']-textHeight)/2)
			elif(t['align']=='left'):
				y = t['y']+((t['height']-textHeight)/2)
			screen.blit(textSurf,(x,y))
	def blitFigures(self,screen,name=None):
		figuresDict = self.figuresDict
		if(name!=None):
			figuresDict = {name:self.figuresDict[name]}
		for i in figuresDict:
			f = figuresDict[i]
			fType = f['type']
			if(fType=='rect'):
				pygame.draw.rect(screen,f['color'],f['rect'],f['width'])
			elif(fType=='circle'):
				pygame.draw.circle(screen,f['color'],f['pos'],f['radius'],f['width'])
			elif(fType=='line'):
				pygame.draw.line(screen,f['color'],f['start'],f['end'],f['width'])
			elif(fType=='arc'):
				pygame.draw.arc(screen,f['color'],f['rect'],f['start'],f['stop'],f['width'])
	def blitImages(self,screen,name=None):
		imagesDict = self.imagesDict
		if(name!=None):
			imagesDict = {name:self.imagesDict[name]}
		for i in imagesDict:
			image = imagesDict[i]
			screen.blit(image['surface'],image['cord'])
	def blit(self,screen,mousePos,mouseButton):
		self.blitBG(screen)
		self.blitFigures(screen)
		self.blitImages(screen)
		self.blitButtons(screen,mousePos,mouseButton)
		self.blitText(screen)