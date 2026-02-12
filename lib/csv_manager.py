import csv
import os, sys, discord
from datetime import datetime
CONST_STATS = ['Overall', 'attack', 'defence', 'strength', 'constitution', 
              'ranged', 'magic', 'cooking', 'woodcutting', 'fletching', 
              'fishing', 'firemaking', 'crafting', 'smithing', 'mining',
              'herblore', 'agility', 'thieving', 'slayer', 'farming',
              'runecrafting', 'hunter', 'construction', 'summoning',
              'dungeoneering', 'divination', 'invention', 'archaeology',
              'necromancy']

class csv_manager():
    def __init__(self):
        pass

    def resourcePath(relativePath):
        try:
            basePath = sys._MEIPASS
        except:
            basePath = os.path.abspath(".")

        return os.path.join(basePath, relativePath)
    
    def ensure_dir(self):
        directory = os.path.dirname('csv')
        print(directory)
        if not os.path.exists('csv'):
            os.makedirs('csv')
    
    def save_csv(self, p):
        fieldnames = CONST_STATS
        fieldnames.append('date/time')
        print(fieldnames)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string)
        if not os.path.exists('csv/{}'.format(p.name)):
            os.makedirs('csv/{}'.format(p.name))
            with open('csv/{}/rank-values.csv'.format(p.name), 'w', newline='') as csvFile:
                csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
                csvWriter.writeheader()
            with open('csv/{}/level-values.csv'.format(p.name), 'w', newline='') as csvFile:
                csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
                csvWriter.writeheader()
            with open('csv/{}/exp-values.csv'.format(p.name), 'w', newline='') as csvFile:
                csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
                csvWriter.writeheader()
        rankList = p.rankList
        levelList = p.levelList
        expList = p.expList
    
        rankList['date/time'] = dt_string
        levelList['date/time'] = dt_string
        expList['date/time'] = dt_string
    
    
        with open('csv/{}/rank-values.csv'.format(p.name), 'a', newline='') as csvFile:
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            csvWriter.writerow(rankList)
        with open('csv/{}/level-values.csv'.format(p.name), 'a', newline='') as csvFile:
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            csvWriter.writerow(levelList)
        with open('csv/{}/exp-values.csv'.format(p.name), 'a', newline='') as csvFile:
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            csvWriter.writerow(expList)