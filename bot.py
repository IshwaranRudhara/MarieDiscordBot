import discord
import asyncio
import time
from config import TOKEN, link
from discord.ext import commands


 
client = commands.Bot(command_prefix = '/')

VERSION = "0.1"


@client.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")


@client.command(name="shutdown")
async def bot_quit():
    await client.say("Shutting down...\n\U0001f44b")
    await client.logout()

  
@client.command()
async def ping():
    '''See if The Bot is Working'''
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, ":ping_pong:  time is `%.01f seconds`" % ping)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += " "
    await client.say(output)

@client.command(name="info")
async def bot_info():
    """Display information about the bot."""
    await client.say("Marie " +VERSION+" "+"(https://github.com/Mithusmenon/MarieDiscordBot)")

@client.command()
async def invite():
    '''A Link To Invite This Bot To Server!'''
    await client.say("Check Your Dm's :wink:")
    await client.whisper(link)



client.run(TOKEN)
