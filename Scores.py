import requests
import json
from csv import writer

url = "https://supersport.com/api/rugby/v4/feed/score/summary"

querystring = {"eventStatus":"3","startDate":"1649455200","endDate":"1649541599","pageSize":"100","orderAscending":"false","region":"za"}

payload = ""
headers = {
    "authority": "supersport.com",
    "accept": "application/json",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cookie": "_gid=GA1.2.1598209652.1650061949; _gcl_au=1.1.1606404431.1650061950; cookie_consent_performance=1; cookie_consent_targeting=0; permutive-id=c24ff889-d151-4387-9023-bca6f764bf7e; OptanonAlertBoxClosed=2022-04-15T22:32:40.289Z; cookie_consent_settings_set=1; _gat=1; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+16+2022+00^%^3A50^%^3A36+GMT^%^2B0200+(South+Africa+Standard+Time)&version=6.23.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001^%^3A1^%^2CC0002^%^3A0^%^2CC0004^%^3A0&geolocation=^%^3B&AwaitingReconsent=false; _dc_gtm_UA-3921485-3=1; _dc_gtm_UA-2819420-3=1; _ga_2CG5ZT6Q2H=GS1.1.1650061951.1.1.1650063037.57; _ga=GA1.1.649685662.1650061949",
    "dnt": "1",
    "referer": "https://supersport.com/rugby/results/",
    "sec-ch-ua": "^\^"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

jsondata = json.loads(response.text)

with open('Scores.csv', 'w', encoding='utf=8', newline='') as f:
    thewriter = writer(f)
    header = ['League', '|', 'Home Team', 'Home Score', '-', 'Away Score', 'Away Team']
    thewriter.writerow(header)
    
    for game in jsondata['Summary']:
        HomeTeam = game['rugbyTeam']['home']['name']
        AwayTeam = game['rugbyTeam']['away']['name']
        League = game['tour']['name']
        HomeScore = game['score']['total']['home']
        AwayScore = game['score']['total']['away']
    
        info = [League, "|", HomeTeam, HomeScore, "-", AwayScore, AwayTeam]
        thewriter.writerow(info)