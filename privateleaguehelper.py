import discord
from config import (
    bot_token,
    command_center,
    new_user_channel,
    help_channel,
    audit_channel,
    intro_schpeal,
)
from discord.ext import commands

description = """
A bot to help in the management of path of exile private leagues"""

intents = discord.Intents.default()
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if message.guild:
        # This is a command being run in a server, pass it on
        await bot.process_commands(message)
        return
    if "!register" in message.content:
        m = message.content
        if (not "<" in m) or (not ">" in m):
            await message.author.send("I didn't quite get that, please try again")
            return
        accountname = m.split("<")[1].split(">")[0]
        if not accountname:
            await message.author.send("I didn't quite get that, please try again")
            return
        await bot.get_guild(command_center).get_channel(new_user_channel).send(
            f"Discord user {message.author.mention}#{message.author.discriminator}: <{message.author.id}>\nAccount name ```{accountname}```would like to be added to the league"
        )
        await bot.get_guild(command_center).get_channel(audit_channel).send(
            f"Discord user {message.author.name}#{message.author.discriminator} with uid {message.author.id} and PoE account name ```{accountname}```has started the registration process"
        )
    if "!help" in message.content:
        await bot.get_guild(command_center).get_channel(help_channel).send(
            f"Discord user {message.author.name}#{message.author.discriminator} is requesting help!"
        )


@bot.event
async def on_reaction_add(reaction, user):
    emoj = reaction.emoji
    if not isinstance(emoj, str):
        emoj = emoj.name
    # emoj should now be a string of the name
    if emoj == "👍":
        discord_id = reaction.message.content.split("<")[1].split(">")[0]
        # Either need a member intent, or to use fetch_user, which is an API call
        await bot.get_user(int(discord_id)).send(
            "A Moderator has indicated that they've added you to the league!\nGood luck and have fun!"
        )


@bot.command()
async def join(ctx):
    """Allows a user to start the process of joining the league"""
    await ctx.message.author.send(intro_schpeal)


bot.run(bot_token)
