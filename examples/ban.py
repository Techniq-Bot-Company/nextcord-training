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
@commands.has_permissions(kick_members=True)
async def ban(ctx,user:nextcord.Member = None,*,reason=None):
    if user == None:
        await ctx.message.reply("Plz enter a user")

    if reason == None:
        reason = ""
    await user.ban(reason=reason)


    if reason == None:
        await ctx.send(f"Banned {user}")
    else:
        await ctx.send(f"Banned {user} for {reason}")

        
bot.run("token")
