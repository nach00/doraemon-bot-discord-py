import discord
import argparse
import logging as log
import sys
import asyncio
import urllib
import json
import random
import os
import pickle
from discord.ext import commands

#DORAEMON
#TOKEN = 'MzkxMDcyMTAxNDI5MTQ5Njk3.DRTfGA.f3KBfj0Nm_1wZghnpKBGEQRRbDY'


#T4C0-BoT
TOKEN = 'Mzg5NjA1Mjc1MjU1OTYzNjQ5.DRTn8Q.-YHIoiX4AkQm8fB7e2uCIRhLrHM'

description = '''T4C0-Bot in Python'''
bot = commands.Bot(command_prefix='!', description=description)

######################################################################

# parser = argparse.ArgumentParser(description="Handle the #on_hand_volunteers channel.")
# parser.add_argument("-v", "--verbose", dest="verbose", action="store_const",
#                     const=True, default=False,
#                     help="verbose output")
# parser.add_argument("-q", "--quiet", dest="quiet", action="store_const",
#                     const=True, default=False,
#                     help="only output warnings and errors")
# parser.add_argument("token", metavar="token", action="store",
#                     help="discord auth token for the bot")
# args = parser.parse_args()

# if args.verbose:
#     log.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=log.DEBUG, stream=sys.stdout)
#     log.debug("Verbose output enabled")
# elif args.quiet:
#     log.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=log.WARNING, stream=sys.stdout)
# else:
#     log.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s", level=log.INFO, stream=sys.stdout)

# log.info("Started")

#bot = discord.Client()

def get_channel(requested_channel):
    for channel in server.channels:
        if channel.name == requested_channel:
            return(channel)
    else:
        log.error("The #{0} channel does not exist".format(requested_channel))
        return False

def get_role(requested_role):
    for role in server.roles:
        if role.name == requested_role:
            return(role)
    else:
        log.error("The {0} role does not exist".format(requested_role))
        return False

def get_members_by_role(role):
    members = []
    for member in server.members:
        for member_role in member.roles:
            if member_role.name == role:
                members.append(member)
                break
    return(members)

@bot.event
async def on_ready():
    global server
    global channels
    global roles

    log.info("Connected to discord")
    log.debug("Logged in as:")
    log.debug("User: {0}".format(bot.user.name))
    log.debug("ID: {0}".format(bot.user.id))

    # Hardcoded server ID for Scrubs
    server = bot.get_server("374742615100489730")
    channels = dict()
    roles = dict()

    log.info("Connected to server: {0}".format(server.name))

######################################################################







@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def eightball():
    phrases = [
        "As I see it, yes",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don’t count on it",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "My reply is no",
        "My sources say no",
        "Outlook good",
        "Outlook not so good",
        "Reply hazy, try again",
        "Signs point to yes",
        "Very doubtful",
        "Without a doubt",
        "Yes",
        "Yes, definitely",
        "You may rely on it.",
        "Blame Mark"
    ]
    #await bot.send_message(message.channel, "{user}: {phrase}".format(user=member.mention, phrase=random.choice(phrases)))
    await bot.say(random.choice(phrases))

@bot.command()
async def catfact():
    cat_facts = open(sys.path[0] + '/cat_facts.txt').read().splitlines()
    await bot.say(random.choice(cat_facts))

@bot.command()
async def dadjoke():
    cat_facts = open(sys.path[0] + '/dadjokes.txt').read().splitlines()
    await bot.say(random.choice(cat_facts))

@bot.command()
async def offjoke():
    cat_facts = open(sys.path[0] + '/offjokes.txt').read().splitlines()
    await bot.say(random.choice(cat_facts))

@bot.command()
async def deadbaby():
    deadbaby = open(sys.path[0] + '/deadbaby.txt').read().splitlines()
    await bot.say(random.choice(deadbaby))

@bot.command()
async def google(query : str):
    # message_parts = message.content.split(' ', 1)

    # if len(message_parts) == 1:
    #     return

    # help_msg = "{user}, here's the info: http://lmgtfy.com/?q={query}".format(
    #     user=member.mention,
    #     query=urllib.parse.quote(message_parts[1])
    # )
    # await bot.say(message.channel, help_msg)
    await bot.say("Hey scrub, let me Google that for you: http://lmgtfy.com/?q="+query)

@bot.command()
async def wtf():
    msg = "Fuck you, my name is DORAEMON and I'm a robotic cat\n\n" \
          "I understand the following commands:\n\n" \
          "`!wtf` - what the fuck, man? do it again and see what happens.\n" \
          "`!eightball` - Ask the magic 8 ball a question.\n" \
          "`!roll` - Request a random number, chosen by fair dice roll.\n" \
          "`!catfact` - Edumacates you in the vast world of meow-meows\n" \
          "`!dadjoke` - U laff @ dad jokes\n" \
          "`!offjoke` - U cry @ sad joke\n" \
          "`!deadbaby` - Tells really horrible jokes\n" \
          "`!google` - Stupid way to find out out shit about shit you don't know\n" \
          "`!fliptable` - Fixes table\n" \
          "`!yeah` - YEAH!!!\n" \
          "`!shrug` - I dunno\n" \
          "\nIf I'm not working correctly, go fuck yourself, you aren't my boss."
    await bot.say(msg)

@bot.command()
async def fliptable():
    await bot.say("┬──┬ ﾉ(° -°ﾉ) That wasn't nice.")

@bot.command()
async def yeah():
    # #yeah
    await bot.say(" \n( •\_•)\n( •\_•)>⌐■-■\n(⌐■\_■)")

@bot.command()
async def shrug():
    # ¯\_(ツ)_/¯
    await bot.say("¯\\_(ツ)_/¯")

@bot.command()
async def roll():
    await bot.say("4")


bot.run(TOKEN)