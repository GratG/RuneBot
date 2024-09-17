import os, sys, discord
#sys.path.append('C:/Dev/RuneBot/lib')

from lib.player import player


def resourcePath(relativePath):
    try:
        basePath = sys._MEIPASS
    except:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

def ensure_dir():
    directory = os.path.dirname('csv')
    print(directory)
    if not os.path.exists('csv'):
        os.makedirs('csv')
        

ensure_dir()

p1 = player("VarroMalleus")
print(type(p1))
print(p1.data)

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord!')

client.run(TOKEN)
