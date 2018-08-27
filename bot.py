import discord
import asyncio
import time
from config import TOKEN, link
from discord.ext import commands

 
client = commands.Bot(command_prefix = '/')

__version__ = '1.0'

extensions = ['commands.ping','commands.purge','commands.invite','commands.echo']


@client.event
async def on_ready():
   
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    #print(f'Bot Version: __version__')
    print("----------------------")
    print("Bot started successfully.")
    print("Ctrl+C To Quit")


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} Cannot Be Loaded. [{}]'.format(extension, error))



@client.command(name="shutdown")
async def bot_quit():
    await client.say("Shutting down...\n\U0001f44b")
    await client.logout()

@client.command(name="info")
async def bot_info():
    """Display information about the bot."""
    await client.say("Marie " +__version__+" "+"(https://github.com/Mithusmenon/MarieDiscordBot)")

client.run(TOKEN)
