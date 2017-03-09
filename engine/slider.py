class Slider():
	def __init__(self):
		self.sliderDict = {}
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
	def getType(self,elem):
		if(type(elem)==tuple):
			return('color')
		elif(type(elem)==str):
			if(elem.find('.')!=-1):
				return('image')
			else:
				return('color')
		else:
			print('Something strange: '+str(type(elem)))
			return(None)
	def checkColor(self,color):
		if(type(color)==str):
			color = self.colors[color]
		return(color)
	def createSlider(self,name,x,y,length,width,height,bg=None,line=None,
		stick=None,stickSize=None,hover=None,click=None,nowPos=0,display='block'):
		if(stickSize==None):
			stickSize = (int(round(width/length/2)),height*3)
		self.sliderDict[name] = {
			'length':length,
			'x':x,
			'y':y,
			'length':length,
			'width':width,
			'height':height,
			'bg':bg,
			'bgSurface':None,
			'line':line,
			'lineSurface':None,
			'stick':stick,
			'stickSize':stickSize,
			'stickSurface':None,
			'hover':hover,
			'click':click,
			'nowPos':nowPos,
			'display':display
		}
		slider = self.sliderDict[name]
		checkList = [bg,line,stick]
		nameList = ['bgSurface','lineSurface','stickSurface']
		sizeList = [(width,height*3),(width,height),stickSize]
		cordList = [(x,y-height),(x,y),(int(round(x+width/length*nowPos)),y-height)]
		for i in checkList:
			if(i!=None):
				iType = self.getType(i)
				index = checkList.index(i)
				if(iType == 'color'):
					size = sizeList[index]
					iSurface = Surface(size)
					iSurface.fill(self.checkColor(i))
				elif(iType == 'image'):
					iSurface = image.load(i)
				slider[nameList[index]] = [iSurface,cordList[index]]
	def setStick(self,name,event):
		slider = self.sliderDict[name]
		if(slider['display']!=None):
			event = slider[event]
			if(event!=None):
				eventType = self.getType(event)
				if(eventType == 'color'):
					surface = Surface(slider['stickSize'])
					surface.fill(self.checkColor(event))
				elif(eventType == 'image'):
					surface = image.load(event)
				x = slider['x']
				width = slider['width']
				length = slider['length']
				nowPos = slider['nowPos']
				size = slider['stickSize']
				cord = ((int(round(x+width/length*nowPos)))-size[0]/2,slider['y']-slider['height'])
				slider['stickSurface'] = [surface,cord]
	def checkMove(self,mousePos,mouseButton):
		for i in self.sliderDict:
			slider = self.sliderDict[i]
			if(slider['display']!=None):
				mX = mousePos[0]
				mY = mousePos[1]
				slX = slider['x'] # sl - slider, st - stick, s - slider and stick
				stX = int(round(slider['x']+slider['width']/slider['length']*slider['nowPos']))
				endSlX = slider['x']+slider['width']
				endStX = stX+slider['stickSize'][0]
				sY = slider['y'] - slider['height']
				endSY = slider['y']+slider['height']*2
				if(mX>=slX and mX<=endSlX and mY>=sY and mY<=endSY):
					if(mouseButton[0]==1):
						slider['nowPos'] = round((mX-slX)/(slider['width']/slider['length']))
						self.setStick(i,'click')
					elif(mX>=stX and mX<=endStX):
						self.setStick(i,'hover')
					else:
						self.setStick(i,'stick')
				else:
					self.setStick(i,'stick')
	def blit(self,screen):
		for elem in self.sliderDict:
			slider = self.sliderDict[elem]
			if(slider['display']!=None):
				surfList = ['bgSurface','lineSurface','stickSurface']
				for i in surfList:
					surf = slider[i]
					if(surf!=None):
						screen.blit(surf[0],surf[1])
"""
slider = Slider()
slider.colors = colors
slider.createSlider('musicVolume',20,20,10,200,10,bg=None,line=colors['orange'],stick=colors['black'],
		hover=colors['amber'],click=colors['yellow'])
while(1==1):
	slider.checkMove(mousePos,mouseButton)
	slider.blit(screen)
"""