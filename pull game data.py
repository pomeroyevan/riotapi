import RiotAPI as api
import time
import datetime as dt

def main():

    user = api.riot_api('RGAPI-861a8ba6-b346-4445-99b0-ede3a12818e6')

    def player_champs(summoner, matches_quantity):
        while True:
            try:
                matchlist = user.tft_matches(summoner,0,matches_quantity)
                return matchlist
            except:
                time.sleep(61)
                continue
            break    
    
    def tier_champs(tier,division,qNames,qMatches):
        names = user.tft_rank_names(tier,qNames,division)
        champs_temp = []
        for n in names:
            champs_temp.append(player_champs(n,qMatches))
            
        store = open(f'{tier}-{division}_{qNames}x{qMatches}_{dt.date.today()}.txt', 'w')
        store.write(str(champs_temp))
        store.close
        
    tier_champs('diamond','I',1,1)


if __name__ == '__main__':
    main()