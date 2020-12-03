import copy
import random

def okrunnerlist(team_name,nation,group):
    return_match = copy.deepcopy(team_name)
    for match in team_name:
        if team_name[match][1] == nation or team_name[match][0] == group :
            del return_match[match]
    return return_match
def draw(team_name,runner_team_name):
    match16 = []
    for match in team_name:
        teamlist = okrunnerlist(runner_team_name,team_name[match][1],team_name[match][0])
        rndteam = random.choice(list(teamlist.keys()))
        match16.append(match + " vs " + rndteam)
        del runner_team_name[rndteam]
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

print(draw(winner_team_name,runner_team_name))