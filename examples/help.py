import nextcord
from nextcord.ext import commands
from flask import Flask
from threading import Thread
import os

app = Flask("")

@app.route("/")
def index():
	return "<h1>Bot is Running</h1>"

Thread(target=app.run, args=("0.0.0.0", 8080)).start()

bot = commands.Bot(command_prefix='!') 
bot.remove_command('help')
client = nextcord.Client

@bot.event
async def on_ready():
    await bot.change_presence(
        status=nextcord.Status.idle,
        activity=nextcord.Activity(
            type=nextcord.ActivityType.watching, 
            name='Techniq Bot Company')
    )
    print('test_bot is up and ready to serve!')
		
@bot.command()
async def help(ctx):
    embed = nextcord.Embed(title="Help",
                           description="This is the help command",
                          color = <hex_code>)
    embed.add_field(name="Command1", value="What it does")  # copy this line for each command
    await ctx.message.reply(embed=embed)
	
my_secret = os.environ['DISCORD_TOKEN'] # use this line only when using repl.it
bot.run(my_secret)
