"""
NOTE: DO NOT DIRECTLY PASTE YOUR BOT'S TOKEN WHILE USING REPL.IT. ALWAYS CREATE A SECRET AND PASTE IT THERE
"""

#import the required packages
import nextcord
from nextcord.ext import commands
#Following two packages are required only for hosting on repl.it. If you are using self hosting need not use it
from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def index():
	return "<h1>Bot is Running</h1>"

Thread(target=app.run, args=("0.0.0.0", 8080)).start()

bot = commands.Bot(command_prefix='<preffered prefix>') # replace <preffered prefix> for the prefix you want to use or told by client
bot.remove_command('help')
client = nextcord.Client

@bot.event
async def on_ready():
    await bot.change_presence(
        status=nextcord.Status.idle, #idle can be replaced by online and dnd only
        activity=nextcord.Activity(
            type=nextcord.ActivityType.watching, #should only be changed (streaming,listening,playing) 
            name='Techniq Bot Company')
    )
    print('<bot_name> is up and ready to serve!')
		
@bot.command()
async def command_name(ctx,par2,par3): #set par2 , par3 .... according to the input that will go with the command
	#refer to examples for seeing sample code
	
my_secret = os.environ['DISCORD_TOKEN'] # use this line only when using repl.it
bot.run(my_secret)
