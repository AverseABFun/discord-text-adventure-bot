""""
Copyright © AverseABFun/sdft 2023 - https://github.com/AverseABFun
Description:
A discord text adventure bot

Version: 0.0.1
"""

from discord.ext import commands
from discord.ext.commands import Context
import discord
import json
import random

from helpers import checks, db_manager, data

async def get_state(context: Context):
    state = await db_manager.get_state(context.author.id)
    if len(state)>1:
        raise ValueError(f"User {context.author.name} has multiple states!")
    if len(state)==0:
        return state
    return state[0]

class TextAdventure(commands.Cog, name="textadv"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="start",
        description="Start your adventure!",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    @checks.in_channel("level-1")
    async def start(self, context: Context):
        """
        This is the command that starts your adventure yaaay

        :param context: The application command context.
        """
        if len(await get_state(context))>0:
            embed = discord.Embed(
                description="You've already started!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        await db_manager.create_state(context.author.id, "start", '{"attack":0.5,"defense":0.5,"reload":0,"fighting":"","enemy_data":"","health":20,"old_attack_room":"","cleared_rooms":[],"start_room":"start"}')
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow started in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        data.mark_player_in_room(context.author.id, state[1])
        embed = discord.Embed(
            title=room["name"],
            description=room["description"],
            color=int(room["color"], base=16)
        )
        await context.send(embed=embed)
    
    @commands.hybrid_command(
        name="look",
        description="Look around at your surroundings",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def look(self, context: Context):
        """
        This is a command that allows you to look around at your surroundings

        :param context: The application command context.
        """
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        data.mark_player_in_room(context.author.id, state[1])
        embed = discord.Embed(
            title=room["name"],
            description=room["description"],
            color=int(room["color"], base=16)
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="north",
        description="Go north",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def north(self, context: Context):
        """
        This is a command that allows you to go north

        :param context: The application command context.
        """
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            room = room["exits"]["north"]
        except KeyError:
            embed = discord.Embed(
                description="You can't go that way!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        await db_manager.update_state(context.author.id, room, state[2])
        data.mark_player_in_room(context.author.id, room)
        data.mark_player_not_in_room(context.author.id, state[1])

        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=room["name"],
            description=room["description"],
            color=int(room["color"], base=16)
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="south",
        description="Go south",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def south(self, context: Context):
        """
        This is a command that allows you to go south

        :param context: The application command context.
        """
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            room = room["exits"]["south"]
        except KeyError:
            embed = discord.Embed(
                description="You can't go that way!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        await db_manager.update_state(context.author.id, room, state[2])
        data.mark_player_in_room(context.author.id, room)
        data.mark_player_not_in_room(context.author.id, state[1])

        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=room["name"],
            description=room["description"],
            color=int(room["color"], base=16)
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="east",
        description="Go east",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def east(self, context: Context):
        """
        This is a command that allows you to go east

        :param context: The application command context.
        """
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            room = room["exits"]["east"]
        except KeyError:
            embed = discord.Embed(
                description="You can't go that way!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        await db_manager.update_state(context.author.id, room, state[2])
        data.mark_player_in_room(context.author.id, room)
        data.mark_player_not_in_room(context.author.id, state[1])

        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=room["name"],
            description=room["description"],
            color=int(room["color"], base=16)
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="west",
        description="Go west",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def west(self, context: Context):
        """
        This is a command that allows you to go west

        :param context: The application command context.
        """
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            room = room["exits"]["west"]
        except KeyError:
            embed = discord.Embed(
                description="You can't go that way!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        await db_manager.update_state(context.author.id, room, state[2])
        data.mark_player_in_room(context.author.id, room)
        data.mark_player_not_in_room(context.author.id, state[1])
        
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        embed = discord.Embed(
            title=room["name"],
            description=room["description"],
            color=int(room["color"], base=16)
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="get",
        description="Get an item",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def get(self, context: Context, item: str):
        """
        This is a command that allows you to get an item.

        :param context: The application command context.
        """
        state = await get_state(context)
        try:
            room = data.get_room_data(state[1])
        except ValueError:
            embed = discord.Embed(
                title="Error!",
                description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            items = room["items"]
        except KeyError:
            embed = discord.Embed(
                title="Error!",
                description="There are no items in this room!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            item = items[item]
        except KeyError:
            embed = discord.Embed(
                title="Error!",
                description="That item isn't in the room!",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        try:
            item = json.load(open(f"items/{item}.json",'r'))
        except:
            embed = discord.Embed(
                title="Error!",
                description="That item is referenced but doesn't exist...? Please report this to @AverseABFun.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        if item["type"] == "weapon":
            print(state)
            inventory = state[2]
            inventory = json.loads(inventory)
            print(inventory)
            if item["attack"]>=inventory["attack"]:
                inventory["attack"] = item["attack"]
                inventory["defense"] = item["defense"]
                inventory["reload"] = item["reload"]
                await db_manager.update_state(context.author.id, state[1], json.dumps(inventory))
                embed = discord.Embed(
                    description="You get the weapon and equip it. You feel stronger now.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
                return
            else:
                embed = discord.Embed(
                    description="You have a better weapon.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
                return

    @commands.hybrid_command(
        name="attack",
        description="Attack an enemy when in an arena",
    )
    @checks.not_blacklisted()
    @checks.not_dms()
    async def attack(self, context: Context):
        state = await get_state(context)
        room = data.get_room_data(state[1])
        inv = json.loads(state[2])
        if inv["fighting"] != "":
            state = list(state)
            enemy = json.loads(inv["enemy_data"])
            text = dict(**enemy["text"])
            print(text)
            text['defend'] = random.choice(text['defend'])
            text['attack'] = random.choice(text['attack'])
            text['die'] = random.choice(text['die'])
            show_text = f"You attack {enemy['name']}.\n{text['defend']}"
            enemy['health'] -= inv['attack']/enemy['defense']
            inv["enemy_data"] = json.dumps(enemy)
            if enemy['health'] <= 0:
                show_text += f"\n\n{text['die']}"
                print(show_text)
                inv["enemy_data"] = ""
                inv["fighting"] = ""
                inv["health"] = 20
                if data.get_room_data(state[1])["return"] != "":
                    state[1] = data.get_room_data(state[1])["return"]
                else:
                    state[1] =  inv["old_attack_room"]
                #if data.get_room_data(state[1]):
                    
                inv["old_attack_room"] = ""
                inv["cleared_rooms"].append(state[1])
                try:
                    item = random.choice(enemy['loot'])
                except: item = ""
                try:
                    item = json.load(open(f"items/{item}.json",'r'))
                except:
                    if item != "":
                        embed = discord.Embed(
                            title="Error!",
                            description="A loot item is referenced but doesn't exist...? Please report this to @AverseABFun.",
                            color=0xE02B2B
                        )
                        await context.send(embed=embed)
                        return
                if item == "":
                    embed = discord.Embed(
                        description=show_text,
                        color=0xE02B2B
                    )
                    await context.send(embed=embed)
                    await db_manager.update_state(context.author.id, state[1], json.dumps(inv))
                    return
                if item["type"] == "weapon":
                    inventory = inv
                    if item["attack"]>=inventory["attack"]:
                        inventory["attack"] = item["attack"]
                        inventory["defense"] = item["defense"]
                        inventory["reload"] = item["reload"]
                        await db_manager.update_state(context.author.id, state[1], json.dumps(inventory))
                        embed = discord.Embed(
                            description=f"{show_text}\n\nYou get the loot weapon and equip it. You feel stronger now.",
                            color=0xE02B2B
                        )
                        await context.send(embed=embed)
                        return
                    else:
                        embed = discord.Embed(
                            description=f"{show_text}\n\nYou already have a better loot weapon.",
                            color=0xE02B2B
                        )
                        await context.send(embed=embed)
                        return
            else:
                show_text += f"\n\n{text['attack']}"
                inv['health'] -= enemy['attack']-inv['defense']
            if inv['health']<=0:
                show_text += "\n\nYou died. You will restart at the start of your current level, but with all of your stuff. See you later!"
                state[1] = inv['start_room']
            embed = discord.Embed(
                description=show_text,
                color=0xE02B2B
            )
            await context.send(embed=embed)
            await db_manager.update_state(context.author.id, state[1], json.dumps(inv))
            return
                
        else:
            try:
                if len(room["enemies"])>0 and state[1] not in inv["cleared_rooms"]:
                    enemy = json.load(open(f"enemies/{room['enemies'][0]}.json",'r'))
                    arena = enemy["arena"]
                    inv = json.loads(state[2])
                    inv["fighting"] = room['enemies'][0]
                    inv["enemy_data"] = json.dumps(enemy)
                    inv["old_attack_room"] = state[1]
                    room = data.get_room_data(arena)
                    await db_manager.update_state(context.author.id, arena, json.dumps(inv))
                    data.mark_player_in_room(context.author.id, arena)
                    data.mark_player_not_in_room(context.author.id, state[1])
                    embed1 = discord.Embed(
                        description="You attacked. The enemy dodged the attack but noticed you and forced you into the arena.",
                        color=0xE02B2B
                    )
                    state = await get_state(context)
                    try:
                        room = data.get_room_data(state[1])
                    except ValueError:
                        embed = discord.Embed(
                            title="Error!",
                            description="You have somehow landed in an invalid location. Please report this to @AverseABFun.",
                            color=0xE02B2B
                        )
                        await context.send(embed=embed)
                        return
                    embed2 = discord.Embed(
                        title=room["name"],
                        description=room["description"],
                        color=int(room["color"], base=16)
                    )
                    await context.send(embeds=[embed1,embed2])
                    return
            except: pass


async def setup(bot):
    await bot.add_cog(TextAdventure(bot))
