import discord
#from discord.ext import commands

TOKEN = 'MTExNDQ1MDc4NjkwMzEzODQyNQ.GBlRq2.IOTI_BMQjkIClMPXKf8nNbOdDBzkFvTHVnloP4'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in: {0.user}'.format(client))
client.run(TOKEN)