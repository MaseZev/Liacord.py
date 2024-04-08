Liacord
==========

<p align="center">
    <a href="https://discord.gg/H7FQFGEPz5"><img src="https://img.shields.io/discord/930415100718878750?style=flat-square&color=5865f2&logo=discord&logoColor=ffffff&label=discord" alt="Discord server invite" /></a>
    <a href="https://pypi.org/project/Liacord"><img src="https://img.shields.io/pypi/v/Liacord.svg?style=flat-square" alt="PyPI version info" /></a>
    <a href="https://pypi.org/project/Liacord/"><img src="https://img.shields.io/pypi/pyversions/Liacord.svg?style=flat-square" alt="PyPI supported Python versions" /></a>
    <a href="https://github.com/masezev/Liacord.py/commits"><img src="https://img.shields.io/github/commit-activity/w/masezev/Liacord.py.svg?style=flat-square" alt="Commit activity" /></a>
</p>

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- Optimised in both speed and memory.

Installing
----------

**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

    # Linux/macOS
    python3 -m pip install -U Liacord

    # Windows
    py -3 -m pip install -U Liacord

Bot Example
~~~~~~~~~~~~~
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
~~~~~~~~~~~~~
You can find more examples in the examples directory [There](https://github.com/MaseZev/Liacord.py/tree/main/examples).


Links


<br>
<p align="center">
    <a href="https://discord.gg/H7FQFGEPz5">Discord Server</a>
    ⁕
    <a href="https://discord.gg/discord-developers">Discord Developers</a>
</p>
<br>

