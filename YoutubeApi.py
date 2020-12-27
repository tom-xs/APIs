from googleapiclient.discovery import build
import json

SEARCH_INPUT = "raflum swwan goose"

youtube = build(serviceName="youtube",version="v3",developerKey="AIzaSyD1HExOrJEk_lPwmOpH9k8fAKrXusQ6KDQ")

reponseDict = youtube.search().list(part="id, snippet",q=SEARCH_INPUT).execute()

print(json.dumps(reponseDict["items"],indent=4))
