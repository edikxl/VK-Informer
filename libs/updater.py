def update(gui,vk):
	rgb = {
		'lightBlue':(43,87,147),
		'blue':(36,51,71),
		'white':(255,255,255),
		'pureGreen':(37,167,40),
		'pureRed':(167,37,37),
		'pureGray':(99,99,111)
	}
	#Info
	infoDict = {
		'msgNum':vk.getMessageNumber(),
		'lastActivity':vk.getLastActivity(),
		'newsNum':vk.getNewsNumber()
	}	#Checking
	if(gui.nowWin == 'mini'):
		win = gui.getWindow('mini')
		if(win.nowPage == 'main'):
			page = win.getPage('main')
			page.textDict['messagesNum']['text'] = str(infoDict['msgNum'])
			page.textDict['newsNum']['text'] = str(infoDict['newsNum'])
			if(infoDict['lastActivity']['online']==1):
				color = rgb['pureGreen']
			else:
				color = rgb['pureRed']
			page.figuresDict['status']['color'] = color