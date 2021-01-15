from googleapiclient.discovery import build
from pytube import YouTube as yt
import musicbrainzngs
import json

SERVICE_NAME = "youtube"
SERVICE_VERSION = "v3"
DEV_KEY = ""

youtube = build(serviceName=SERVICE_NAME,version=SERVICE_VERSION,developerKey=DEV_KEY)

musicbrainzngs.set_useragent("Learning programming with youtube api", "0.0", "txs@ecomp.poli.br")

def searchRecording(ALBUM_SEARCH_INPUT):
     return musicbrainzngs.search_recordings(query=ALBUM_SEARCH_INPUT)

def getRecordingList(dic):
     recordingList = []
     count = 0

     for item in dic["recording-list"]:
          string = str(count) + " - "
          count+=1
          string = string + item['title']
          string = string+ " - " +item['release-list'][0]['title']
          recordingList.append(string)

     return recordingList

def getJsonForInput(USER_INPUT):
     responseDict = youtube.search().list(part="id, snippet",q=USER_INPUT).execute()
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

def printElements(listNames,listURLS):
     for i in range(0,len(listNames)):
          print(str(i) + " - "+ listNames[i] + " : " + listURLS[i])

def downloadVideo(url):
     print("download iniciado")
     video = yt(url)
     video.streams.filter(only_audio=True)[0].download()
     print("download finalizado")


def main():
     SONG_INPUT = input("escreva o nome da música que você quer baixar: ")
     YTlistNames, YTlistURLs = getListsVideosIds(getJsonForInput(SONG_INPUT))
     printElements(YTlistNames , YTlistURLs)
     YTN_INPUT = int(input("digite o nº da música que você quer baixar: "))
     print(str(YTN_INPUT) + " - "+ YTlistNames[YTN_INPUT] + " : " + YTlistURLs[YTN_INPUT])

     ALBUM_SEARCH_INPUT = input("escreva o nome da música para cover art e metadados: ")
     result = searchRecording(ALBUM_SEARCH_INPUT)

     MBRecordingList = getRecordingList(result)
     MBN_INPUT = input("digite o nº da música com os metadados desejados: ")



     print("dale")



if __name__ == "__main__":
     main()
