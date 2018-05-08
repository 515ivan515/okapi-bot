import discord
from discord.ext import commands
from os import listdir
from os.path import isfile, join
import sys, traceback

def decode(inp):
    return "".join(map(lambda x: chr(ord(x) - 7), inp))

okapiicon = """https://orig02.deviantart.net/d6e5/f/2013/184/5/6/56c80607908d203f4b516480701586af-d6bsxy5.png"""

def get_prefix(bot, message):
    prefix = '..'
    if not message.guild:
        return ''
    return commands.when_mentioned_or(prefix)(bot, message)

cogs_dir = "cogs"
bot = commands.Bot(command_prefix=get_prefix, description='Okapi Bot By @Just An Okapi#8112')

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')


bot.run(decode("""UKX\x7fT[j\x80T[T;V[\\<V[`\x80T[L\x805KjzaN~5Y}Y~\\rz4{V`ju?7]79\\@8qfIQ]P"""), bot=True, reconnect=True)
