import requests as r
import access as a
import random

class riot_api(object):

    def __init__(self, keys):
        self.keys = keys
        
    def request(self, api_url, reg=a.region_lol):
        req = r.get(
            a.URL['base'].format(
                region = reg, 
                keys=self.keys,
                url = api_url
            )
        )
        print(req.url)
        print(req)
        return req.json()

    def summoner_by_name(self, name):
        api_url = a.URL['summoner_by_name'].format(
            sum_name = name
        )
        return self.request(api_url)

    def puuid(self, name):
        return self.summoner_by_name(name)['puuid']
    
    def tft_match_Ids(self, name, startq, countq):
        api_url = a.URL['tft_match_by_puuid'].format(
            puuid=self.puuid(name),
            start=startq,
            count=countq
        )
        return self.request(api_url,a.region_tft)
    
    def tft_matches(self, name, startq, countq):
        list_matchIds = self.tft_match_Ids(name, startq, countq)
        list_matches = []
        for m in list_matchIds:
            api_url = a.URL['tft_match_by_matchId'].format(
                matchId = m
            )
            list_matches.append(self.request(api_url, a.region_tft))
        return list_matches

    def tft_rank_names(self,tier,quantity,division = ''):
        players = []
        if tier in ['challenger','grandmaster','master']:
            api_url = a.URL['names_from_tft_rank'].format(
                rank = tier
            )
            rank_break = self.request(api_url)['entries']
        else:
            api_url = a.URL['names_from_tft_rank'].format(
                rank = f'entries/{tier.upper()}/{division}'
            )
            rank_break = self.request(api_url)
        for p in range(quantity):
            players.append(rank_break[random.randint(0,len(rank_break)-1)]['summonerName'])
        return players
    


