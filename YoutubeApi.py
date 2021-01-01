from googleapiclient.discovery import build
from pytube import YouTube as yt
import musicbrainzngs
import json

SERVICE_NAME = "youtube"
SERVICE_VERSION = "v3"
DEV_KEY = "AIzaSyD1HExOrJEk_lPwmOpH9k8fAKrXusQ6KDQ"

youtube = build(serviceName=SERVICE_NAME,version=SERVICE_VERSION,developerKey=DEV_KEY)

musicbrainzngs.set_useragent("Learning programming with youtube api", "0.0", "txs@ecomp.poli.br")

def searchAlbum(ALBUM_SEARCH_INPUT):
     return musicbrainzngs.search_release_groups(query=ALBUM_SEARCH_INPUT)

def getJsonForInput(USER_INPUT):
     responseDict = youtube.search().list(part="id, snippet",q=USER_INPUT).execute()
     return json.dumps((responseDict["items"]),indent = 4)

def getIdandNameLists(result):
    albumNameList = []
    idList = []

    for item in result["release-group-list"]:
        idList.append(item["id"])
        albumNameList.append(item["title"])

    return albumNameList , idList

def getUrllist(albumNameList,idList):
    newlistUrl = []
    newAlbumName = []

    for item in range(0,len(albumNameList)):
        try:
            newlistUrl.append(musicbrainzngs.get_release_group_image_list(idList[item])['images'][0]['image'])
            newAlbumName.append(albumNameList[item])
        except musicbrainzngs.musicbrainz.ResponseError:
    return newAlbumName , newlistUrl

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
     YTN_INPUT = int(input("escolha o numero do elementos que você quer baixar: "))
     print(str(YTN_INPUT) + " - "+ YTlistNames[YTN_INPUT] + " : " + YTlistURLs[YTN_INPUT])


     ALBUM_SEARCH_INPUT = input("escreva o nome do album/artista para cover art: ")
     result = searchAlbum(ALBUM_SEARCH_INPUT)

     MBalbumNameList , MBidList = getIdandNameLists(result)
     MBalbumNameList , MBlistUrl = getUrllist(MBalbumNameList , MBidList)

     print("dale")



if __name__ == "__main__":
     main()
