import musicbrainzngs
import json

musicbrainzngs.set_useragent("Learning programming with youtube api", "0.0", "txs@ecomp.poli.br")

#def searchAlbum(album):
#    result = musicbrainzngs.search_recordings(query = album)
#
#def searchArtist(artist):
#    result = musicbrainzngs.search_artists(query = artist)

result = musicbrainzngs.search_release_groups(query = "raflum")

def delAlbumwithoutCover(albumNameList,idList):
    newAlbumNamelist = []
    newIdList = []
    for i in range(0,len(albumNameList)):
        try:
            musicbrainzngs.get_release_group_image_list(idList[i])
            newAlbumNamelist.append(albumNameList[i])
            newIdList.append(idList[i])
        except musicbrainzngs.musicbrainz.ResponseError:
            print("erro xd")

    return newAlbumNamelist , newIdList

def getUrllist(list):
    listUrl = []

    for item in range(0,len(list)):
        listUrl.append(musicbrainzngs.get_release_group_image_list(idList[item])['images'][0]['image'])
    
    return listUrl

def getIdandNameLists():
    albumNameList = []
    idList = []

    for item in result["release-group-list"]:
        idList.append(item["id"])
        albumNameList.append(item["title"])

    return albumNameList , idList

albumNameList , idList = getIdandNameLists()

#albumNameList , idList = delAlbumwithoutCover(idList , albumNameList)

listUrl = getUrllist(idList)

print("dale")
