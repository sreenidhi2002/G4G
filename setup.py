import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("G4G Bot is ready to start.")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

#takes in context as param
@client.command()
async def schedule(ctx, *, time, ta_name):
    await ctx.send(f'Schedule request received.\n Time: {time}\n TA/CA name: {ta_name} \n Position in queue: ')

@client.command()
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)} ms')

#TO DO
client.run('NzQzMDU5ODkzNzA3MDc5NzIw.XzPKdA.rLmHRjoPY5BWxZ25yNAA5PyZ1zY')
