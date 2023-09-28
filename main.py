from discord.ext import commands
import discord
from random import *
import contextlib
import config

intents = discord.Intents.all()
intents.members = True
        
class kelabot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_extensions = [
            'cogs._events',
        ]

    global check_if_allowed
    def check_if_allowed(ctx):
        return ctx.author.id in config.admins

    async def setup_hook(self) -> None:
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        
    async def on_ready(self):
        print('started')

    async def on_error(self, event_method, *args, **kwargs):
        error_message = f"Error in event {event_method}:"
        error_message += f"\n{args}"
        error_message += f"\n{kwargs}"
        print(error_message)

bot = kelabot(
    command_prefix=".", 
    intents=intents,
    activity=discord.Activity(type=discord.ActivityType.listening, name="sucking on deez"), 
)

@bot.command()
@commands.check(check_if_allowed) 
async def cleanup(ctx, amount: int):
    '''
    Cleans message, do .cleanup <value>
    '''
    if amount <= 0:
        await ctx.send("Please provide a valid positive number of messages to delete.")
        return

    await ctx.message.delete()
    with contextlib.suppress(discord.HTTPException):
        deleted_messages = await ctx.channel.purge(limit=amount)

@cleanup.error
async def cleanup_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the number of messages to delete.")

bot.run(config.token)
