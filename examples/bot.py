import asyncio
from Liacord import Client, Intents, EmbedBuilder

intents = Intents().all()
client = Client("your_bot_token", prefix="#", intents=intents)

@client.command(name="info")
async def hello(ctx):
    await ctx.send(f"Channel id: {ctx.channel.id}, Author id: {ctx.author.id}, Author name: {ctx.author.name}, Guild id: {ctx.guild.id}")

@client.command(name="help")
async def help(ctx):
    await ctx.send(f"Hi {ctx.author.name}, I'm Liacord!")
    channel = await client.fetch_channel(ctx.channel.id)
    await ctx.send(f"{channel['name']}")

@client.command(name="get_info_channel")
async def get_info_channel(ctx):
    channel = await client.fetch_channel(ctx.channel.id)
    await ctx.send(f"{channel}")

@client.command(name="embed-test")
async def embed_test(ctx):
    message = await ctx.send('hello')
    await ctx.edit_message(message_id=message['id'], content="HELLO2")

@client.command(name="embed-test2")
async def embed_test2(ctx):
    message = await ctx.send('hello')
    await asyncio.sleep(5)
    await ctx.delete_message(message_id=message['id'])

@client.command(name="ping")
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency)}ms.")

@client.command(name='server_id', brief='get the server id')
async def server_id_command(ctx):
    server_id = ctx.guild.id
    await ctx.send(f"server id: {server_id}")

loop = asyncio.get_event_loop()
loop.run_until_complete(client.run())
