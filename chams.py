import copy
import random
import operator
def okrunnerlist(team_name,nation,group):
    return_match = copy.deepcopy(team_name)
    for match in team_name:
        if team_name[match][1] == nation or team_name[match][0] == group :
            del return_match[match]
    return return_match
def draw(team_name,runner_team_name):
    match16 = []
    cnt = 0
    while cnt != 8:
        match = []
        ok = 0
        for match_ck in team_name:
            if len(okrunnerlist(runner_team_name,team_name[match_ck][1],team_name[match_ck][0])) == 1:
                ok = 1
                match = match_ck
        if ok == 0:
            match = random.choice(list(team_name.keys()))
        teamlist = okrunnerlist(runner_team_name,team_name[match][1],team_name[match][0])
        rndteam = random.choice(list(teamlist.keys()))
        match16.append(match + " vs " + rndteam)
        del runner_team_name[rndteam]
        del team_name[match]
        cnt = cnt + 1
    return match16




winner_team_name = {'Bayern Muenchen' : ['A','Germany'],
             'Borussia Moenchengladbach' :['B','Germany'], #B
             'Manchester City' : ['C','England'],
             'Liverpool' :['D','England'],
             'Chelsea' : ['E','England'],
             'Borussia Dortmund' : ['F','Germany'], # or 2
             'Barcelona' : ['G','Spain'], # or 2
             'Manchester United' : ['H','England']} # or ManU
runner_team_name ={
             'ATM' : ['A','Spain'],     #or ATM
             'Shakhtar Donetsk' : ['B','Ukraine'], #B
             'Porto' : ['C','Portugal'],
             'Atalanta' : ['D','Netherland'], #or Atalanta
             'Sevilla' : ['E','Spain'],
             'Juventus' : ['G','Italy'], # or 1
             'Lazio':['F','Italy'], # or Club Brugge
             'Paris Saint-Germain' : ['H','France']}

matchcount = dict()
count = 0
while count != 100000:
    try:
        matchlist = draw(copy.deepcopy(winner_team_name),copy.deepcopy(runner_team_name))
    except:
        continue
    for match in matchlist:
        if match in matchcount :
            matchcount[match] = matchcount[match] + 1
        else:
            matchcount[match] = 1
    count = count + 1
matchcount = sorted(matchcount.items(),key=lambda x: x[1],reverse=True)
print(matchcount)