import asyncio
from Liacord import Client, Intents

intents = Intents().all()
client = Client("your_token_here", prefix="#", intents=intents)

@client.command(name="name")
async def hello(ctx):
    await ctx.send(f"{ctx.author.name}")

@client.command(name="ping")
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency)}ms.")

@client.command(name='server_id', brief='get the server id')
async def server_id_command(ctx):
    server_id = ctx.guild.id
    await ctx.send(f"server id: {server_id}")

loop = asyncio.get_event_loop()
loop.run_until_complete(client.run())
