import discord, random
from discord.ext import commands

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
   await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="Sparky"))
   print('Bot is online')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a member')
        return
    await member.ban()
    await ctx.send(f'{member.display_name} was banned from the server')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send('Please mention a member')
        return
    await member.kick()
    await ctx.send(f'{member.display_name} was kicked from the server')

@client.command()
async def embed(ctx):
    embed=discord.Embed()
    embed.title='Answer'
    embed.description='custom command (by sparky)'
    await ctx.send(embed=embed)

@client.command()
async def normal(ctx):
    await ctx.send('What do you want')

client.run('NjkwNTAyOTAwNjIyODE5MzU4.XnTVwQ.WGqm2UAMh0qywD07MhgQWGDyl3o')
