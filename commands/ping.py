import discord
import asyncio
import time
from discord.ext import commands

class ping:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self):
        pingtime = time.time()
        pingms = await self.client.say("*Pinging...*")
        ping = (time.time() - pingtime) * 1000
        await self.client.edit_message(pingms, "**Pong!** :ping_pong:  The ping time is `%dms`" % ping)
        print("Pinged bot with a response time of %dms." % ping)

def setup(client):
    client.add_cog(ping(client))