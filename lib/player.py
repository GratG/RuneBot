import os

import requests
import json
import pandas

import numpy

from datetime import datetime
from win10toast import ToastNotifier

class player:
    def __init__(self, n):
        print("player {} initiated".format(n))
        self.name = n
        self.data = call_player(n)

        
    
def call_player(n):
    
    stats = ['Overall', 'attack', 'defence', 'strength', 'constitution', 
              'ranged', 'magic', 'cooking', 'woodcutting', 'fletching', 
              'fishing', 'firemaking', 'crafting', 'smithing', 'mining',
              'herblore', 'agility', 'thieving', 'slayer', 'farming',
              'runecrafting', 'hunter', 'construction', 'summoning',
              'dungeoneering', 'divination', 'invention', 'archaeology',
              'necromancy']
              
    response = requests.get("https://secure.runescape.com/m=hiscore/index_lite.ws?player={}".format(n))
    if(response.ok):
        print("response ok")
    else:
        print("response not ok")
        return
    stat_list = []
    stat_list = response.text.splitlines()
    
    i = 0
    data = {}
    for s in stats:
        data[s] = stat_list[i]
        i += 1
    print(type(data))
    jdata = json.dumps(data)
    return data 
    


