from discord.ext import commands
from discord import Intents

from business import discord_business
from config import config

DISCORD_GUILD_ID = int(config.DISCORD_GUILD_ID)

intent = Intents(messages=True, members=True, guilds=True, reactions=True, message_content=True)
bot = commands.Bot(command_prefix='$', intents=intent)

@bot.command()
async def rewards(ctx):
    await discord_business.rewards(ctx)

@bot.command()
async def delete(ctx):
    await discord_business.delete(ctx)

@bot.command()
async def init(ctx):
    await discord_business.init(ctx)

@bot.command()
async def setfile(ctx, arg: str = "on"):
    await discord_business.setfile(ctx, arg)

@bot.command()
async def started(ctx, arg: str = "on"):
    await discord_business.started(ctx, arg)

@bot.command()
async def test(ctx):
    await discord_business.test(ctx)

@bot.command()
async def clear(ctx, nombre: int = 100):
    await discord_business.clear(ctx, nombre)

@bot.command()
async def cmd(ctx):
    await discord_business.cmd(ctx)

@bot.event
async def on_message(message):
    if message.guild.id != DISCORD_GUILD_ID:
        return
    if message.attachments:
        await discord_business.import_file(bot, message)
    if message.author == bot.user:
        return
    await bot.process_commands(message)

def main():
    bot.run(config.DISCORD_TOKEN)