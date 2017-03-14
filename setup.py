import pygame,sys,time as tm
from pygame import *
from engine import gui
from libs import VKAPI,windows,updater

if(__name__=='__main__'):
	vk = VKAPI.VK('configs','standart')
	vk.checkAuthKey()
	cfg = vk.nowCFG
	winPos = cfg['pos']
	gui = gui.GUI(winPos,(300,300))
	windows.create(gui,vk)
	startTime = tm.time()
	while(1==1):
		gui.tick(60)
		nowTime = tm.time()
		if(nowTime-startTime>cfg['updateTime']):
			updater.update(gui,vk)
			updateReady = False
			startTime = tm.time()
		gui.blitWindow()