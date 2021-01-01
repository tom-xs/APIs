import musicbrainzngs
import json

musicbrainzngs.set_useragent("Learning programming with youtube api", "0.0", "txs@ecomp.poli.br")

result = musicbrainzngs.search_release_groups(query = "raflum")

def getUrllist(albumNameList,idList):
    newlistUrl = []
    newAlbumName = []

    for item in range(0,len(albumNameList)):
        try:
            newlistUrl.append(musicbrainzngs.get_release_group_image_list(idList[item])['images'][0]['image'])
            newAlbumName.append(albumNameList[item])
        except musicbrainzngs.musicbrainz.ResponseError:
            print("erro")
    return newAlbumName , newlistUrl

def getIdandNameLists():
    albumNameList = []
    idList = []

    for item in result["release-group-list"]:
        idList.append(item["id"])
        albumNameList.append(item["title"])

    return albumNameList , idList

albumNameList , idList = getIdandNameLists()

newListName , listUrl = getUrllist(albumNameList,idList)

print("dale")
