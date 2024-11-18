import discord

from discord import app_commands
from discord.ext import commands
from datetime import datetime, timezone, timedelta


class coffe(GroupCog, group_name="coffe", group_description="Commands in relation to coffe and what sorrounds it"):
    def __init__(self, bot):
        self.bot = bot
        
    @command(name="tierlist", description="This is a tier list of different coffe flavours")
    async def tierlist(self, inter: discord.Interaction):
        await inter.response.send_message("This is a test feature RN and more to be implemented later")

async def setup(bot):
    await bot.add_cog(coffe(bot))