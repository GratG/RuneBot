import os, sys, discord
import json

from datetime import datetime

from discord import app_commands
from lib.player import player
from lib.csv_manager import csv_manager
from dotenv import load_dotenv

CONST_STATS = ['Overall', 'attack', 'defence', 'strength', 'constitution', 
              'ranged', 'magic', 'cooking', 'woodcutting', 'fletching', 
              'fishing', 'firemaking', 'crafting', 'smithing', 'mining',
              'herblore', 'agility', 'thieving', 'slayer', 'farming',
              'runecrafting', 'hunter', 'construction', 'summoning',
              'dungeoneering', 'divination', 'invention', 'archaeology',
              'necromancy']


    
        
try:
    p1 = player("VarroMalleus")
except:
    print("failed to create player")
mngr = csv_manager()
mngr.ensure_dir()
mngr.save_csv(p1)


class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.csv_mngr = csv_manager()

    async def setup_hook(self):
        # Sync commands to Discord
        await self.tree.sync()



load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
bot = MyBot()

@bot.tree.command(name="hello", description="Says hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello there!")

bot.run(TOKEN)
