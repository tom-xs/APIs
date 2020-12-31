from googleapiclient.discovery import build
from pytube import YouTube as yt
import json

SEARCH_INPUT = "swan goose raflum"

SERVICE_NAME = "youtube"
SERVICE_VERSION = "v3"
DEV_KEY = "AIzaSyD1HExOrJEk_lPwmOpH9k8fAKrXusQ6KDQ"

youtube = build(serviceName=SERVICE_NAME,version=SERVICE_VERSION,developerKey=DEV_KEY)

def getJsonForInput():
     responseDict = youtube.search().list(part="id, snippet",q=SEARCH_INPUT).execute()
     return json.dumps((responseDict["items"]),indent = 4)

def getListsVideosIds(json):
     listJson = json.split("\n")
     listNames = []
     listURLS = []

     for line in listJson:
          if("videoId" in line):
               listURLS.append("http://youtube.com/watch?v="+line.replace(" ","")[11:-1])
          if("title" in line):
               listNames.append(line[22:-2])
     
     return listNames, listURLS

def downloadaVideo(url):
     print("download iniciado")
     video = yt(url)
     video.streams.filter(only_audio=True)[0].download()
     print("download finalizado")

def printElements(listNames,listURLS):
     for i in range(0,len(listNames)):
          print(str(i) + " - "+ listNames[i] + " : " + listURLS[i])


def main():
     listaNames, listaURLs = getListsVideosIds(getJsonForInput())
     printElements(listaNames,listaURLs)
     downloadaVideo(listaURLs[0])


if __name__ == "__main__":
     main()



"""
TODO:1-checar se a musica é a que a pessoa procura  
     2-baixar musica 
     3-alterar metadados
"""