from discord.ext import commands
import discord

from random import *

class _events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = None

    @commands.Cog.listener()
    async def on_message(self, msg):  
            # if not msg.author.id == 657064257552384044: # If author is not puang
            if msg.channel.id == 1156593944663183452: # if channel is not general
                if not isinstance(msg.channel, discord.channel.DMChannel): # if the channel is not Dm channel
                    if not msg.content.startswith(self.bot.command_prefix): #checking if msg is a commands 
                        if not msg.attachments:
                            await msg.delete() 

async def setup(bot):
    await bot.add_cog(_events(bot))
