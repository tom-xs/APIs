from googleapiclient.discovery import build
import json

SEARCH_INPUT = "raflum swwan goose"

SERVICE_NAME = "youtube"
SERVICE_VERSION = "v3"
DEV_KEY = ""

youtube = build(serviceName= SERVICE_NAME,version=SERVICE_VERSION,developerKey=DEV_KEY)

reponseDict = youtube.search().list(part="id, snippet",q=SEARCH_INPUT).execute()

print(json.dumps(reponseDict["items"],indent=4))

"""
TODO:1-checar se a musica é a que a pessoa procura  
     2-baixar musica 
     3-alterar metadados
"""
