import json

with open('scores.json') as f:
    jsondata = json.load(f)

for game in jsondata['Summary']:
    HomeTeam = game['rugbyTeam']['home']['name']
    AwayTeam = game['rugbyTeam']['away']['name']
    League = game['tour']['name']
    HomeScore = game['score']['total']['home']
    AwayScore = game['score']['total']['away']

    print(League, "|", HomeTeam, HomeScore, "-", AwayScore, AwayTeam)

