""""
Copyright © AverseABFun/sdft 2023 - https://github.com/AverseABFun-Windows
Description:
A discord text adventure bot

Version: 0.0.1
"""

from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks, db_manager


class TextAdventure(commands.Cog, name="textadv"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="start",
        description="Start your adventure!",
    )
    @checks.not_blacklisted()
    async def testcommand(self, context: Context):
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        pass


async def setup(bot):
    await bot.add_cog(TextAdventure(bot))
