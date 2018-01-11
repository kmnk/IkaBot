import random
from logging import basicConfig, getLogger, DEBUG, INFO
from typing import List

from discord.ext import commands

import data
import env
import model.weapons
from type.language import Language
from type.weapon import Weapon

env = env.Env()

logger = getLogger(__name__)
basicConfig(level=DEBUG if env.debug else INFO)

bot = commands.Bot(command_prefix=env.prefix, description='Bot for enjoying Splatoon2')
data = data.Data(env)

@bot.event
async def on_ready():
    logger.info('Logged in as')
    logger.info('- name: ' + bot.user.name)
    logger.info('- id: ' + bot.user.id)

@bot.group(pass_context=True)
async def rand(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('rand sub-commands are [weapon]')

@rand.command()
async def weapon(count:int=1, *, arg:str='all'):
    weapons = []

    types = arg.split(' ')
    if 'all' in types:
        weapons = data.all_weapons
    else:
        wtypes = Weapon.from_str_arr(types)
        for ws in data.weapons:
            if ws.type in wtypes:
                weapons.extend(ws.list)

    if len(weapons) <= 0:
        await bot.say('No weapon candidates')
    else:
        for i in range(min(count, 8)):
            await bot.say('{0}: {1}'.format(str(i+1), random.choice(weapons).localized_name))

@bot.event
async def on_message(message):
    logger.debug('{0}: {1}'.format(message.author, message.content))

    if bot.user == message.author:
        return await bot.process_commands(message)

    await bot.process_commands(message)

def main():
    logger.info('Starting IkaBot')
    bot.run(data.token)

if __name__ == '__main__': main()
