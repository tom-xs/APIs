from googleapiclient.discovery import build
import json

SEARCH_INPUT = ""

SERVICE_NAME = "youtube"
SERVICE_VERSION = "v3"
DEV_KEY = ""

youtube = build(serviceName= SERVICE_NAME,version=SERVICE_VERSION,developerKey=DEV_KEY)

def getJsonForInput():
     responseDict = youtube.search().list(part="id, snippet",q=SEARCH_INPUT).execute()
     return json.dumps((responseDict["items"]),indent = 4)

def getDicVideosIds(json):
     listJson = json.split("\n")
     dicReturn = {}

     for line in listJson:
          if("videoId" in line):
               value = "http://youtube.com/watch?v="+line.replace(" ","")[11:-1]
          if("title" in line):
               key = line[22:-2]
               dicReturn[key]=value
     
     return dicReturn

def printDicElements(dic):
     for k,v in dic.items():
          print(k, ":", v)

dic = getDicVideosIds(getJsonForInput())

printDicElements(dic)



"""
TODO:1-checar se a musica é a que a pessoa procura  
     2-baixar musica 
     3-alterar metadados
"""