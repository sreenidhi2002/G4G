import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("G4G Bot is ready to start.")

#TO DO
client.run('NzQzMDU5ODkzNzA3MDc5NzIw.XzPKdA.hEcTqwnxHhNRHjmu7aw6hI0MEWQ')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')
