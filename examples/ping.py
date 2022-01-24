import nextcord
from nextcord.ext import commands
import time

bot = commands.Bot(command_prefix='t!')
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
    print('tut_bot is up and ready to serve!')


@bot.command()
async def ping(ctx): 
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic()-before) * 1000
    await message.edit(content = f"Pong! `{int(ping)}ms`")


bot.run("token")
