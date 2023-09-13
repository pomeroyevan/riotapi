import matplotlib.pyplot as plt
import RiotAPI as api
import time

def main():

    user = api.riot_api('RGAPI-861a8ba6-b346-4445-99b0-ede3a12818e6')
    sum_name = 'Banger123456789'


    def store_champs(mList,puuid,placement,include_champ_tier = False):
        match_count = 0
        st=0
        champ_dict = {}
        print(mList)
        for m in mList:
            for p in m['info']['participants']:
                if p['puuid'] == puuid and p['placement'] <= placement:
                    match_count += 1
                    for champ in p['units']:
                        print(champ)
                        if include_champ_tier:
                            ctemp = f'{champ["character_id"][5:]} {champ["tier"]}'
                        else:
                            ctemp = f'{champ["character_id"][5:]}'
                            
                        if not ctemp in champ_dict:
                            champ_dict[ctemp] = 1
                        else:
                            champ_dict[ctemp] += 1
        print(st)
        return champ_dict
                        
    def player_champs(summoner, matches_quantity,placement,include_champ_tier = False):
        while True:
            try:
                matchlist = user.tft_matches(summoner,0,matches_quantity)
                return store_champs(matchlist,user.puuid(summoner),placement, include_champ_tier)
            except:
                time.sleep(61)
                continue
            break    

    
    def tier_champs(tier,division,qNames,qMatches,placement,include_champ_tier = False):
        names = user.tft_rank_names(tier,qNames,division)
        champs_temp = []
        champs_return = {}
        for n in names:
            champs_temp.append(player_champs(n,qMatches,placement,include_champ_tier))
        print(len(champs_temp))
        for player in champs_temp:
            for champ in player:
                if not champ in champs_return:
                    champs_return[champ] = player[champ]
                else:
                    champs_return[champ] += player[champ]
        return champs_return
        
    print(tier_champs('challenger','',1,1,8))


if __name__ == '__main__':
    main()