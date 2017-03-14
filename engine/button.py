import pygame
from pygame import *

class Button():
	def __init__(self):
		self.btnDict = {}
		self.funcDict = {}
		self.blitList = []
		self.btnActive = None
		self.nowFunc = None
		self.btnEventData = [None,None]
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
	def checkColor(self,color):
		if(type(color)==str):
			color = self.colors[color]
		return(color)
	def createButton(self,name,x,y,width,height,color=(0,0,0),hoverColor=(100,100,100),clickColor=(200,200,200),display='block',winSize=None,image=None,imageHover=None,imageClick=None):
		self.btnDict[name] = {
			'name':name,
			'x':x,
			'y':y,
			'width':width,
			'height':height,
			'textPresence':0, #False
			'display':display
		}
		if(display=='center'):
			self.btnDict[name]['x'] = int((winSize[0]-width)/2)
		elif(display=='left'):
			self.btnDict[name]['x'] = 0
		elif(display=='right'):
			self.btnDict[name]['x'] = int(winSize[0]-width)
		self.btnDict[name]['endX'] = self.btnDict[name]['x']+self.btnDict[name]['width']
		self.btnDict[name]['endY'] = self.btnDict[name]['y']+self.btnDict[name]['height']
		btn = self.btnDict[name]
		if(image==None):
			eventList = [0,1,2]
			eventsColorList = [color,hoverColor,clickColor]
			for i in eventsColorList:
				if(type(i)==str):
					eventList[eventsColorList.index(i)] = Surface((width,height))
					eventList[eventsColorList.index(i)].fill(self.colors[i])
				elif(type(i)==tuple):
					eventList[eventsColorList.index(i)] = Surface((width,height))
					eventList[eventsColorList.index(i)].fill(i)
				else:
					eventList[eventsColorList.index(i)] = i
			simple = eventList[0]
			hover = eventList[1]
			click = eventList[2]
		else:
			simple = image.load(image)
			hover = image.load(imageHover)
			click = image.load(imageClick)
		btn['simple'] = simple
		btn['hover'] = hover
		btn['click'] = click
		self.funcDict[name]=None
	def createManyButtons(self,names,x,Kx,y,Ky,width,height,simpleColor=(0,0,0),hoverColor=(100,100,100),clickColor=(200,200,200),display='block',winSize=None,image=None,imageHover=None,imageClick=None):
		for i in range(len(names)):
			vList = [simpleColor,hoverColor,clickColor]
			for event in vList:
				if(type(event)==list):
					if(len(event)<len(vList) and i>=len(event)):
						var = i%len(event)
						vList[vList.index(event)] = vList[vList.index(event)][var]
					else:
						vList[vList.index(event)] = vList[vList.index(event)][i]
			self.createButton(names[i],int(x+Kx*i),int(y+Ky*i),width,height,vList[0],vList[1],vList[2],display,winSize,image,imageHover,imageClick)
	def setText(self,name,text='',textSize=22,textX=0,textY=0,textColor=(0,0,0),font='fonts/UbuntuBold.ttf',align='center',textAntialiasing=15):
		textColor = self.checkColor(textColor)
		btn = self.btnDict[name]
		btn['textPresence'] = 1 #True
		btn['text'] = text
		btn['textSize'] = textSize
		btn['textColor'] = textColor
		btn['font'] = font
		btn['align'] = align
		btn['textAntialiasing'] = textAntialiasing
		textSurface = pygame.font.Font(font,textSize).render(text,textAntialiasing,textColor)
		btn['textSurface'] = textSurface
		textWidth = textSurface.get_width()
		textHeight = textSurface.get_height()
		btn['textWidth'] = textWidth
		btn['textHeight'] = textHeight
		if(align=='center'):
			textX = (btn['width']-textWidth)/2
			textY = (btn['height']-textHeight)/2
		elif(align=='right'):
			textX = btn['width']-textWidth
			textY = (btn['height']-textHeight)/2
		elif(align=='left'):
			textX = 0
			textY = (btn['height']-textHeight)/2
		elif(align=='own'):
			textX = textX
			textY = textY
		btn['textX'] = textX
		btn['textY'] = textY
	def setFunc(self,name,funcType,var):
		self.funcDict[name] = [funcType,var]
	def useFunc(self):
		if(self.btnActive==0):
			btnFunc = self.nowFunc
			if(btnFunc!=None):
				data = self.btnEventData
				name = data[0]
				if(btnFunc[0]=='func'):
					if(len(btnFunc[1])>1):
						btnFunc[1][0](btnFunc[1][1])
					else:
						btnFunc[1][0]()
				self.nowFunc = None
		else:
			data = self.btnEventData
			if(data[0]!=None and data[1]=='click'):
				if(self.nowFunc==None):
					if(self.funcDict[data[0]]!=None):
						self.nowFunc = self.funcDict[data[0]]
	def updateBlitList(self):
		data = self.btnEventData
		self.blitList = []
		for i in self.btnDict:
			btn = self.btnDict[i]
			if(btn['display']!=None):
				if(data[0]==btn['name']):
					btnStyle = btn[data[1]]
				else:
					btnStyle = btn['simple']
				self.blitList.append([btnStyle,(btn['x'],btn['y'])])
				if(btn['textPresence']!=0):
					self.blitList.append([btn['textSurface'],(btn['x']+btn['textX'],btn['y']+btn['textY'])])
	def checkEvent(self,mousePos,mouseButton):
		for i in self.btnDict:
			btn = self.btnDict[i]
			if(mousePos[0]<=btn['endX'] and mousePos[0]>=btn['x'] and mousePos[1]>=btn['y'] and mousePos[1]<=btn['endY']):
				if(mouseButton[0]==1):
					self.btnEventData = [i,'click']
					self.btnActive = 1
					return
				else:
					self.btnActive = 0
					self.btnEventData = [i,'hover']
					return
		else:
			self.btnActive = 0
			self.btnEventData = [None,None]
	def blit(self,screen):
		for i in self.blitList:
			screen.blit(i[0],i[1])
"""
button = Button()
button.colors = colors
button.createButton('play',0,winSize[1]-100,winSize[0],100,rgb['white'],rgb['grey'],rgb['silver'])
button.setText('play','Change background color',35)
button.setFunc('play','func',[changeColor])
while(1==1):
	button.checkEvent(mousePos,mouseButton)
	button.updateBlitList()
	button.useFunc()
	button.blit(screen)
"""