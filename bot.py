import discord
import asyncio
import time
from config import TOKEN, link
from discord.ext import commands


 
client = commands.Bot(command_prefix = '/')

__version__ = '1.0'


@client.event
async def on_ready():
   
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print(f'Discord Version: {discord.__version__}')
    print(f'Bot Version: {__version__}')
    print("----------------------")
    print("Bot started successfully.")
    print("Ctrl+C To Quit")


@client.command(name="shutdown")
async def bot_quit():
    await client.say("Shutting down...\n\U0001f44b")
    await client.logout()

  
@client.command()
async def ping():
    pingtime = time.time()
    pingms = await client.say("*Pinging...*")
    ping = (time.time() - pingtime) * 1000
    await client.edit_message(pingms, "**Pong!** :ping_pong:  The ping time is `%dms`" % ping)
    print("Pinged bot with a response time of %dms." % ping)


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
    await client.say("Marie " +__version__+" "+"(https://github.com/Mithusmenon/MarieDiscordBot)")

@client.command()
async def invite():
    '''A Link To Invite This Bot To Server!'''
    await client.say("Check Your Dm's :wink:")
    await client.whisper(link)

@client.command(pass_context=True)
async def purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Purge Complete.")




client.run(TOKEN)
