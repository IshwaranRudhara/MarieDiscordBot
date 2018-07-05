import discord
import asyncio
from discord.ext import commands


"""TOKEN = "For Token Contact icode""""
 
client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print(client.user.name)
    print('Is Ready!')

client.run(TOKEN)