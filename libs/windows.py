import pygame,sys,os
from pygame import *
try:
	from libs import updater
except:
	import updater
rgb = {
	'lightBlue':(43,87,147),
	'blue':(36,51,71),
	'white':(255,255,255),
	'pureGreen':(37,167,40),
	'pureRed':(167,37,37),
	'pureGray':(99,99,111)
}
#Buttons func
def changeWindow(name):
	gui.nowWin = name
	gui.getWindow(gui.nowWin).init()
def changePage(window,name):
	gui.winDict[window].nowPage = name
def exit():
	pygame.quit()
	sys.exit()
def hide():
	pygame.display.iconify()
def update():
	updater.update(gui,vk)
#...
def create(GUI,VK):
	global gui
	global vk
	gui = GUI
	vk = VK
	createMini()
	createNormal()
def createNormal():
	normalWinSize = (800,600)
	gui.createWindow('normal',normalWinSize,'VK Informer')
	normal = gui.getWindow('normal')
	normal.createPage('main',normalWinSize)
	nM = normal.getPage('main')
	nM.createRect('head',0,0,800,100,rgb['lightBlue'])
	nM.createRect('body',0,100,800,500,rgb['blue'])
def createMini():
	miniWinSize = (300,300)
	gui.createWindow('mini',miniWinSize,'VK Informer',winMode=pygame.NOFRAME)
	mini = gui.getWindow('mini')
	mini.createPage('main',miniWinSize)
	mM = mini.getPage('main')
	#AFTERBLITDICT
	afterFigureList = ['exit1','exit2','max1','max2','hide']
	for i in afterFigureList:
		mini.updateAfterBlitDict('main',['figure',i])
	mini.updateAfterBlitDict('main',['image','update'])
	#Parts
	mM.createRect('head',0,0,300,30,rgb['lightBlue'])
	mM.createRect('body',0,30,300,270,rgb['blue'])
	mM.createRect('test',0,30,300,70)
	mM.createCircle('status',244+28,30+35,15,rgb['pureGray'])
	#Buttons
	normal = rgb['lightBlue']
	hover = rgb['blue']
	click = rgb['white']
	#Update
	mM.button.createButton('update',200-34,0,33,30,normal,hover,click)
	mM.button.setFunc('update','func',[update])
	mM.createImage('update',200-34,0,'data\\image\\icons\\updateMini.png')
	#Hide
	mM.button.createButton('hide',200,0,33,30,normal,hover,click)
	mM.button.setFunc('hide','func',[hide])
	mM.createLine('hide',(200+5,13),(200+27,13),rgb['white'],3)
	#Minimize
	mM.button.createButton('maximize',234,0,33,30,normal,hover,click)
	mM.button.setFunc('maximize','func',[changeWindow,'normal'])
	mM.createRect('max1',234+7,4,19,18,rgb['white'],1)
	mM.createRect('max2',234+5,7,18,17,rgb['white'],1)
	#Exit
	mM.button.createButton('exit',268,0,32,30,normal,hover,click)
	mM.button.setFunc('exit','func',[exit])
	mM.createLine('exit1',(268+6,5),(268+25,24),rgb['white'],3)
	mM.createLine('exit2',(268+6,24),(268+25,5),rgb['white'],3)
	#Texts
	mM.createText('programName','VK Informer',25,10,0,rgb['white'],align='own')
	mM.createText('username','None',40,0,30,rgb['white'],width=245,height=70,align='center')
	#Images
	mM.createImage('messagesIcon',10,100,'data\image\icons\\vkMessages.png')
	mM.createImage('newsIcon',10,165,'data\image\icons\\vkNews.png')
	mM.createImage('notificationsIcon',10,230,'data\image\icons\\vkNotifications.png')
	#Info
	mM.createText('messages','Сообщения',25,70,110,rgb['white'])
	mM.createCircle('messages',270,125,17,rgb['lightBlue'])
	mM.createText('messagesNum','0',25,265,110,rgb['white'])
	#
	mM.createText('news','Новости',25,70,175,rgb['white'])
	mM.createCircle('news',270,190,17,rgb['lightBlue'])
	mM.createText('newsNum','0',25,265,175,rgb['white'])
	#
	mM.createText('notifications','Уведомления',25,70,245,rgb['white'])
	mM.createCircle('notifications',270,260,17,rgb['lightBlue'])