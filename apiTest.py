import statsapi
playerid = statsapi.lookup_player('strasburg')[0]['id']
stats = statsapi.player_stats(playerid, '2019')
print(stats)