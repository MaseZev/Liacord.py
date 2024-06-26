import asyncio

import aiohttp

from .context import Context
from .embed import EmbedBuilder


class Client:
    class Guild:
        def __init__(self, guild_info):
            self.id = guild_info['id']
            self.name = guild_info['name']
            self.icon = guild_info['icon']
            self.owner_id = guild_info['owner_id']
            self.region = guild_info['region']
            self.afk_timeout = guild_info['afk_timeout']
            self.afk_channel_id = guild_info['afk_channel_id']
            self.verification_level = guild_info['verification_level']
            self.default_message_notifications = guild_info['default_message_notifications']
            self.mfa_level = guild_info['mfa_level']
            self.explicit_content_filter = guild_info['explicit_content_filter']
            self.premium_tier = guild_info['premium_tier']
            self.premium_subscription_count = guild_info['premium_subscription_count']
            self.system_channel_id = guild_info['system_channel_id']
            self.system_channel_flags = guild_info['system_channel_flags']
            self.rules_channel_id = guild_info['rules_channel_id']
            self.public_updates_channel_id = guild_info['public_updates_channel_id']
            self.preferred_locale = guild_info['preferred_locale']
            self.features = guild_info['features']
            self.description = guild_info['description']
            self.banner = guild_info['banner']
            self.max_presences = guild_info['max_presences']
            self.max_members = guild_info['max_members']
            self.max_video_channel_users = guild_info['max_video_channel_users']

    STATUS_TYPES = ['online', 'idle', 'dnd', 'invisible']
    ACTIVITY_TYPES = ['playing', 'streaming', 'listening', 'watching']

    def __init__(self, token, prefix="!", intents=0):
        self.prefix = prefix
        self.token = token
        self.intents = intents
        self.base_url = 'https://discord.com/api/v10'
        self.session = aiohttp.ClientSession()
        self.commands = []
        self.latency = None
        self.guild = None

    async def get_payload(self, op, text=None):
        payload = {
            'op': op,
            'd': {
                'token': self.token,
                'properties': {
                    '$os': 'windows',
                    '$browser': 'chrome',
                    '$device': 'pc'
                }
            }
        }
        return payload
    async def close(self):
        await self.session.close()

    async def fetch_user(self, user_id):
        url = f'{self.base_url}/users/{user_id}'
        headers = {'Authorization': f'Bot {self.token}'}
        try:
            async with self.session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f'Error fetching user: {e}')
            return None

    async def fetch_channel(self, channel_id):
        url = f'{self.base_url}/channels/{channel_id}'
        headers = {'Authorization': f'Bot {self.token}'}
        try:
            async with self.session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f'Error fetching channel: {e}')
            return None

    async def fetch_channel_context(self, channel_id):
        url = f'{self.client.base_url}/channels/{channel_id}'
        headers = {'Authorization': f'Bot {self.client.token}'}
        try:
            async with self.client.session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f'Error fetching channel: {e}')
            return None

    async def fetch_guild(self, guild_id):
        url = f'{self.base_url}/guilds/{guild_id}'
        headers = {'Authorization': f'Bot {self.token}'}
        try:
            async with self.session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f'Error fetching guild: {e}')
            return None

    async def send(self, ctx, content=None, *, tts=False, embed=None, delete_after=None,
                   nonce=None, allowed_mentions=None):
        url = f'{self.base_url}/channels/{ctx.channel.id}/messages'
        headers = {'Authorization': f'Bot {self.token}', 'Content-Type': 'application/json'}

        payload = {
            'content': content,
            'tts': tts,
            'nonce': nonce,
            'allowed_mentions': allowed_mentions
        }

        if embed:
            if isinstance(embed, EmbedBuilder):
                payload['embeds'] = [embed.to_dict()]
            else:
                raise ValueError("Embed must be an instance of EmbedBuilder")

        try:
            async with self.session.post(url, headers=headers, json=payload) as response:
                response.raise_for_status()
                message_data = await response.json()

                if delete_after:
                    await asyncio.sleep(delete_after)
                    delete_url = f"{self.base_url}/channels/{ctx.channel.id}/messages/{message_data['id']}"
                    async with self.session.delete(delete_url, headers=headers) as delete_response:
                        delete_response.raise_for_status()

                return message_data
        except aiohttp.ClientResponseError as e:
            print(f'Error sending message: {e}')
            return None

    async def delete_message(self, ctx, message_id):
        if not isinstance(ctx, Context):
            raise ValueError("ctx must be an instance of Context")
        if not isinstance(message_id, str):
            raise ValueError("message_id must be a string")

        url = f'{self.base_url}/channels/{ctx.channel.id}/messages/{message_id}'
        headers = {'Authorization': f'Bot {self.token}'}

        try:
            async with self.session.delete(url, headers=headers) as response:
                response.raise_for_status()
        except aiohttp.ClientResponseError as e:
            print(f'Error deleting message: {e}')

    async def edit_message(self, ctx, message_id, content=None, embed=None):
        if not isinstance(ctx, Context):
            raise ValueError("ctx must be an instance of Context")
        if not isinstance(message_id, str):
            raise ValueError("message_id must be a string")

        url = f'{self.base_url}/channels/{ctx.channel.id}/messages/{message_id}'
        headers = {'Authorization': f'Bot {self.token}', 'Content-Type': 'application/json'}

        payload = {}
        if content:
            if not isinstance(content, str):
                raise ValueError("content must be a string")
            payload['content'] = content
        if embed:
            if not isinstance(embed, EmbedBuilder):
                raise ValueError("embed must be an instance of EmbedBuilder")
            payload['embed'] = embed.to_dict()

        try:
            async with self.session.patch(url, headers=headers, json=payload) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f'Error editing message: {e}')

    async def on_message(self, message):
        if 'guild_id' in message:
            guild_id = message['guild_id']
            guild_info = await self.fetch_guild(guild_id)
            self.guild = self.Guild(guild_info)
        await self.process_commands(message)

    async def start(self):
        try:
            headers = {'Authorization': f'Bot {self.token}'}
            async with self.session.ws_connect('wss://gateway.discord.gg') as ws:
                payload = await self.get_payload(op=2)
                await ws.send_json(payload)
                async for msg in ws:
                    data = msg.json()
                    if data['op'] == 10:
                        self.latency = data['d']['heartbeat_interval'] / 1000
                        payload = await self.get_payload(op=1)
                        await ws.send_json(payload)
                    elif data['op'] == 0:
                        await self.on_message(data['d'])
        except Exception as e:
            print(f'An error occurred: {e} | Line 82')
        finally:
            while True:
                await self.start()

    async def run(self):
        await self.start()

    def command(self, name=None, *, brief=None):
        def decorator(func):
            self.commands.append((name, brief, func))
            return func

        return decorator

    async def process_commands(self, message):
        if 'content' in message:
            content = message['content']
            if content.startswith(self.prefix):
                words = content.split()
                command_name = words[0][len(self.prefix):]
                for name, brief, func in self.commands:
                    if command_name == name:
                        ctx = Context(message, self)
                        await func(ctx)
        elif 'type' in message and message['type'] == 7:
            pass
