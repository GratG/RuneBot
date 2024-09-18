import os

import requests
import json
import pandas

import numpy
from win10toast import ToastNotifier

CONST_STATS = ['Overall', 'attack', 'defence', 'strength', 'constitution', 
              'ranged', 'magic', 'cooking', 'woodcutting', 'fletching', 
              'fishing', 'firemaking', 'crafting', 'smithing', 'mining',
              'herblore', 'agility', 'thieving', 'slayer', 'farming',
              'runecrafting', 'hunter', 'construction', 'summoning',
              'dungeoneering', 'divination', 'invention', 'archaeology',
              'necromancy']
class player:
    def __init__(self, n):
        print("player {} initiated".format(n))
        self.data = call_player(n)
        self.name = n
        self.rankList = {}
        self.levelList = {}
        self.expList = {}
        for s in CONST_STATS:
            dataSet = self.data[s]
            dataList = dataSet.split(",")
            self.rankList[s] = dataList[0]
            self.levelList[s] = dataList[1]
            self.expList[s] = dataList[2]


        
    
def call_player(n):
    
              
    response = requests.get("https://secure.runescape.com/m=hiscore/index_lite.ws?player={}".format(n))
    print("Response is type:",type(response.text))
    
    if(response.ok):
        print("response ok")
    else:
        print("response not ok")
        return
    stat_list = []
    stat_list = response.text.splitlines()
    
    i = 0
    data = {}
    data['name'] = n
    for s in CONST_STATS:
        data[s] = stat_list[i]
        i += 1
    
    
    with open('data.json', 'w') as file:
        json.dump(data, file)
    return data 
    


#call_player("VarroMalleus")