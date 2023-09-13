region_lol = 'na1'
region_tft = 'americas'
summoner_name = 'TheNuclearToast'
URL = {
    'base' : 'https://{region}.api.riotgames.com/{url}{keys}',
    'summoner_by_name' : 'lol/summoner/v4/summoners/by-name/{sum_name}?api_key=',
    'tft_match_by_puuid' : 'tft/match/v1/matches/by-puuid/{puuid}/ids?start={start}&count={count}&api_key=',
    'tft_match_by_matchId' : 'tft/match/v1/matches/{matchId}?api_key=',
    'names_from_tft_rank' : 'tft/league/v1/{rank}?api_key='
}