import discord
import asyncio
from config import link
from discord.ext import commands

class invite:
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def invite(self):
        '''A Link To Invite This Bot To Server!'''
        await self.client.say("Check Your Dms! :wink:")
        await self.client.whisper(link)

def setup(client):
    client.add_cog(invite(client))