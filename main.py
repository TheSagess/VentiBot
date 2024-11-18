import os
import discord
import datetime
from discord.ext.commands import ExtensionNotFound, ExtensionFailed
from dotenv import load_dotenv
from discord.ext import commands
from checks import is_owner

#Import Cogs
from coffe import coffe

# Load Dotenvs
load_dotenv()

# Set Intents
intents = discord.Intents.default()  # Sets the default bot intents
intents.guilds = True
intents.members = True  # Allows the bot to see members in a guild
intents.message_content = True  # Allows the bot to see message content

# Set Some Other Varibles
TOKEN = os.getenv("token")
COMMAND_PREFIX = "?"  # Sets the bots command prefix for non app commands
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)  # Defines bot

# Load Cogs
async def load_cogs(bot): # Taken out of Vaje Bot [Closed Project of mine]
    cogs = [coffe]  # Ensure these are properly imported
    for cog in cogs:
        if not bot.get_cog(cog.__name__):
            try:
                await bot.load_extension(cog.__name__)
                print(f"Successfully loaded cog: {cog.__name__}")
            except ExtensionNotFound:
                print(f"Cog {cog.__name__} not found. Please check the module name and path.")
            except ExtensionFailed as e:
                print(f"Cog {cog.__name__} failed to load: {e}")
            except Exception as e:
                print(f"Unexpected error occurred while loading cog {cog.__name__}: {e}")


# Bot ready event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("Ready!")

# Sync command to reload the app commands
@bot.command(pass_context=True, hidden=True)
@commands.is_owner()
async def sync(ctx):
    await ctx.bot.tree.sync()
    await ctx.send("Commands synced, you will need to reload Discord to see them")
    await ctx.message.delete()


bot.run(TOKEN)