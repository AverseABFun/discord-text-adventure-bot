"""
Copyright © AverseABFun/sdft 2023 - https://github.com/AverseABFun
Description:
A discord text adventure bot

Version: 0.0.1
"""

from discord.ext import commands


class UserBlacklisted(commands.CheckFailure):
    """
    Thrown when a user is attempting something, but is blacklisted.
    """

    def __init__(self, message="User is blacklisted!"):
        self.message = message
        super().__init__(self.message)


class UserNotOwner(commands.CheckFailure):
    """
    Thrown when a user is attempting something, but is not an owner of the bot.
    """

    def __init__(self, message="User is not an owner of the bot!"):
        self.message = message
        super().__init__(self.message)

class UserExecutingInDMs(commands.CheckFailure):
    """
    Thrown when a user is attempting something, but is not executing it in a guild.
    """

    def __init__(self, message="User cannot execute command in DMs!"):
        self.message = message
        super().__init__(self.message)

class IncorrectChannel(commands.CheckFailure):
    """
    Thrown when a user is attempting something, but is not executing it in the correct channel.
    """

    def __init__(self, message="User cannot execute command in channel!"):
        self.message = message
        super().__init__(self.message)
        