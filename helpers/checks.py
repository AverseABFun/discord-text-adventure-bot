""""
Copyright © AverseABFun/sdft 2023 - https://github.com/AverseABFun
Description:
A discord text adventure bot

Version: 0.0.1
"""

import json
import os
from typing import Callable, TypeVar

from discord.ext import commands

from exceptions import *
from helpers import db_manager

T = TypeVar("T")


def is_owner() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is an owner of the bot.
    """

    async def predicate(context: commands.Context) -> bool:
        with open(
            f"{os.path.realpath(os.path.dirname(__file__))}/../config.json"
        ) as file:
            data = json.load(file)
        if context.author.id not in data["owners"]:
            raise UserNotOwner
        return True

    return commands.check(predicate)


def not_blacklisted() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is blacklisted.
    """

    async def predicate(context: commands.Context) -> bool:
        if await db_manager.is_blacklisted(context.author.id):
            raise UserBlacklisted
        return True

    return commands.check(predicate)

def not_dms() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is executing it in the DMs.
    """

    async def predicate(context: commands.Context) -> bool:
        if not context.guild:
            raise UserExecutingInDMs
        return True

    return commands.check(predicate)

def in_channel(channel: str) -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is executing it in the DMs.
    """

    async def predicate(context: commands.Context) -> bool:
        if context.channel.name != channel:
            raise IncorrectChannel
        return True

    return commands.check(predicate)
