import requests
import pymongo
#from random import randint

class Urlshortener():
  __id = 1000000000
  __urlidlist = {}

  def shortenUrl(self,originalUrl):
    if self.urlvalidation(originalUrl):
      if originalUrl in self.__urlidlist:
        __id = self.__urlidlist[originalUrl]
        shortenUrl = self.encode(__id)
      else:
        self.__urlidlist[originalUrl] = self.__id
        shortenUrl = self.encode(self.__id)
        self.__id += 1

      return "severosurl.com/"+str(shortenUrl)
    else:
      return "Url: "+originalUrl+" Is invalid \n  " 

  def encode(self, id):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tam = len(characters)

    retencode = []

    while id > 0:
      value = id % tam
      retencode.append(characters[value])
      id = id // tam
    
    return "".join(retencode[::-1])

  def urlvalidation(self,url):
    try:
      response = requests.get(url)
      if response.status_code == 200 :
        return True
    except:
      return False


    
