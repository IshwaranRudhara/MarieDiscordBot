import discord
import asyncio
from discord.ext import commands

class purge:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await self.client.delete_messages(messages)
        await self.client.say("Purge Complete.")


def setup(client):
    client.add_cog(purge(client))