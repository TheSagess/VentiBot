import discord

from discord import app_commands
from discord.ext import commands
from datetime import datetime, timezone, timedelta


class coffe(GroupCog, group_name="coffe", group_description="Commands in relation to coffe and what sorrounds it"):
    def __init__(self, bot):
        self.bot = bot
        



async def setup(bot):
    await bot.add_cog(coffe(bot))