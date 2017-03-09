import pygame,sys,os
from pygame import *

class Audio():
	def __init__(self,nowMusic=None,musicState='stop'):
		pygame.mixer.init()
		self.nowMusic = nowMusic
		self.musicState = musicState
		self.musicList = []
		self.soundDict = {}
	#Music
	def loadMusic(self,var):
		if(type(var)==int):
			pygame.mixer.music.load(self.musicList[var])
			self.nowMusic = self.musicList[var]
		elif(type(var)==str):
			pygame.mixer.music.load(var)
			self.nowMusic = var
	def playMusic(self):
		pygame.mixer.music.play()
		self.musicState = 'play'
	def pauseMusic(self):
		pygame.mixer.music.pause()
		self.musicState = 'pause'
	def unpauseMusic(self):
		pygame.mixer.music.unpause()
		self.musicState = 'play'
	def stopMusic(self):
		pygame.mixer.music.stop()
		self.musicState = 'stop'
	def restartMusic(self):
		pygame.mixer.music.rewind()
		self.musicState = 'play'
	def updateMusicList(self,path):
		musicList = os.listdir(path)
		self.musicList = []
		for i in musicList:
			if(i.find('.mp3')!=-1 or i.find('.ogg')!=-1):
				self.musicList.append(path+i)
	def checkPlaying(self):
		state = pygame.mixer.music.get_busy()
		if(state == 1):
			return('true')
		else:
			return('false')
	def setMusicVolume(self,vol):
		pygame.mixer.music.set_volume(vol)
	def getMusicVolume(self):
		return(pygame.mixer.music.get_volume())
	#Sounds
	def createSound(self,name,path):
		self.soundDict[name] = pygame.mixer.Sound(path)
	def playSound(self,name):
		self.soundDict[name].play()
	def setAudioVolume(self,vol):
		pygame.mixer.Sound.set_volume(vol)
	def getAudioVolume(self):
		return(pygame.mixer.Sound.get_volume())