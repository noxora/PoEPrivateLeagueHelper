import discord
from privateleaguehelper.config import (
    bot_token,
    command_center,
    new_user_channel,
    help_channel,
    audit_channel,
)
from privateleaguehelper.schpeal import (
    schpeal_intro,
    schpeal_crowdfund,
    schpeal_unknown,
    schpeal_faq,
    error_no_username,
    error_no_image,
    error_not_image,
    error_typo,
    confirmation_registered,
    confirmation_admitted,
    confirmation_help,
    confirmation_proof,
    example_proof,
)
from discord.ext import commands
import os

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
    # I'm probably doing all of this the hard way, since there's probably a way to get bot commands in dms. This works for now though
    if message.author.id == bot.user.id:
        return
    if message.guild:
        # This is a command being run in a server, pass it on
        await bot.process_commands(message)
        return

    # Check these first, since they don't require any processing
    if "!help" in message.content:
        await handle_help(message)
        return

    if "!intro" in message.content:
        await handle_intro(message)
        return

    if "!example" in message.content:
        await handle_example(message)
        return

    if "!crowdfund" in message.content:
        await handle_crowdfund(message)
        return

    if "!faq" in message.content:
        await handle_faq(message)
        return

    m = message.content
    message_has_account_name = False
    accountname = None
    if ("<" in m) and (">" in m):
        message_has_account_name = True
        accountname = m.split("<")[1].split(">")[0]

    # These two are grouped because of common validation steps
    if "!register" in m or "!proof" in m:
        # Validate account name
        if not message_has_account_name or not accountname:
            await message.author.send(error_no_username)
            return
        # Handle Register
        if "!register" in m:
            await handle_register(message, accountname)
            return
        # Handle Proof
        if "!proof" in m:
            # Validate attachments
            if not message.attachments:
                await message.author.send(error_no_image)
                return
            for att in message.attachments:
                if not att.content_type or not "image" in att.content_type:
                    await message.author.send(error_not_image)
            await handle_proof(message, accountname)
            return

    if m.startswith("!"):
        await message.author.send(error_typo)
        return

    # We got here because we don't know what they said
    await message.author.send(schpeal_unknown)


async def handle_register(message, accountname):
    """handle_register assumes that the message has been validated to be of the form:
    !register <account-name>"""
    await bot.get_guild(command_center).get_channel(new_user_channel).send(
        f"Discord user {message.author.name}#{message.author.discriminator}: <{message.author.id}>\nAccount name ```{accountname}```would like to be added to the league"
    )
    await bot.get_guild(command_center).get_channel(audit_channel).send(
        f"Discord user {message.author.name}#{message.author.discriminator} with uid {message.author.id} and PoE account name ```{accountname}```has started the registration process"
    )
    await message.author.send(confirmation_registered)


async def handle_proof(message, accountname):
    """handle_proof assumes that the message has been validated to contain at least one image and is of the form:
    !proof <account-name>"""
    ifiles = []
    for attach in message.attachments:
        ifiles.append(await attach.to_file())
    await bot.get_guild(command_center).get_channel(audit_channel).send(
        f"Discord user {message.author.name}#{message.author.discriminator} with uid {message.author.id} and PoE account name ```{accountname}``` has submitted a proof image",
        files=ifiles,
    )
    await message.author.send(confirmation_proof)


async def handle_help(message):
    await bot.get_guild(command_center).get_channel(help_channel).send(
        f"Discord user {message.author.name}#{message.author.discriminator} is requesting help!"
    )
    await message.author.send(confirmation_help)


async def handle_example(message):
    image_file = open(f"PrivateLeagueHelper{os.path.sep}example_image.PNG", "rb")
    discord_file = discord.File(image_file)
    await message.author.send(
        example_proof,
        file=discord_file,
    )
    # Discord.py should override this method, but call it anyway
    image_file.close()


async def handle_intro(message):
    await message.author.send(schpeal_intro)


async def handle_crowdfund(message):
    await message.author.send(schpeal_crowdfund)


async def handle_faq(message):
    await message.author.send(schpeal_faq)


# TODO: Change this to on_raw_reaction_add
@bot.event
async def on_reaction_add(reaction, user):
    # Only care about reactions to our messages
    if reaction.message.author.id != bot.user.id:
        return
    emoj = reaction.emoji
    if not isinstance(emoj, str):
        emoj = emoj.name
    # emoj should now be a string of the name
    if reaction.message.channel.id == new_user_channel:
        if emoj == "????":
            discord_id = reaction.message.content.split("<")[1].split(">")[0]
            await bot.get_user(int(discord_id)).send(confirmation_admitted)
            reactors = await reaction.users().flatten()
            if len(reactors) < 1:  # This shouldn't happen
                await bot.get_guild(command_center).get_channel(audit_channel).send(
                    f"A moderator has indicated that they've added user {discord_id}, but the moderator could not be found"
                )
            await bot.get_guild(command_center).get_channel(audit_channel).send(
                f"Moderator {reactors[0]} has indicated that they've added user {discord_id} to the league"
            )


@bot.command()
async def join(ctx):
    """Allows a user to start the process of joining the league"""
    await ctx.message.author.send(schpeal_intro)


def start():
    bot.run(bot_token)
