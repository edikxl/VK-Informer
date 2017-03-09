import json,sys,os,webbrowser,requests as req

class VK:
	def __init__(self,cfgPath,standartCfgName):
		self.cfgPath = cfgPath
		self.standartCFG = self.getConfig(standartCfgName)
		self.updateNowCFG()
	def getConfig(self,name):
		return(json.loads(open(self.cfgPath+'\\'+name+'.cfg','r').read()))
	def updateNowCFG(self):
		self.nowCFGName = self.standartCFG['nowCFG']
		self.nowCFG = self.getConfig(self.nowCFGName)
	def checkAuthKey(self):
		if(len(self.nowCFG['accessToken'])==0):
			self.createAccessKey()
			sys.exit()
	def createAccessKey(self):
		link = 'https://oauth.vk.com/authorize?'
		clientID = '5909764'
		redirect = 'https://oauth.vk.com/blank.html'
		display = 'page'
		responseType = 'token'
		version = '5.62'
		scope = 'friends,messages,wall,offline,notifications,email'
		site = link+'client_id='+clientID+'&display='+display+'&redirect_uri='+redirect+'&scope='+scope+'&response_type='+responseType+'&v='+version
		webbrowser.open(site)
	def request(self,methodName,params=None):
		site = 'https://api.vk.com/method/'
		url = site+methodName+'?'
		if(params!=None):
			for i in params:
				if(type(params[i])!=str):
					params[i] = str(params[i])
				url = url+'&'+i+'='+params[i]
		index = url.find('&')
		url = url[:index]+url[index+1:]
		r = req.post(url)
		requestDict = json.loads((r.content).decode('utf-8'))
		if(requestDict.get('error')==None):
			return(requestDict)
		else:
			if(requestDict['error']['error_code']==5):
				self.createAccessKey()
				sys.exit()
			else:
				import time as tm
				nowTime = str(round(tm.time()))
				open('logs/'+nowTime+'.txt','w').write(str(requestDict))
				sys.exit()
	def getMessageNumber(self):
		requestDict = self.request('messages.get',{'out':'0','count':self.nowCFG['maxMsg'],'access_token':self.nowCFG['accessToken'],'version':'5.62'})
		num = 0
		response = requestDict['response']
		for msgDict in response:
			if(response.index(msgDict)!=0):
				if(msgDict['read_state']!=1):
					num+=1
		return(num)
	def getLastActivity(self):
		requestDict = self.request('messages.getLastActivity',{'user_id':self.nowCFG['userID'],'access_token':self.nowCFG['accessToken'],'version':'5.62'})
		resp = requestDict['response']
		activityDict = {
			'online':resp['online'],
			'time':resp['time']
		}
		return(activityDict)
	def getNewsNumber(self):
		startTime = self.getLastActivity()['time']
		requestDict = self.request('newsfeed.get',{'filters':'post','start_time':startTime,'access_token':self.nowCFG['accessToken'],'version':'5.62'})
		return(len(requestDict['response']['items']))