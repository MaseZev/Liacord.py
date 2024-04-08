import aiohttp

class Context:
    def __init__(self, message, client):
        self.message = message
        self.channel = self.Channel(message['channel_id'])
        self.author = self.User(message['author'])
        self.guild = client.guild
        self.client = client

    async def fetch_channel_context(self, channel_id, client):
        url = f'{client.base_url}/channels/{channel_id}'
        headers = {'Authorization': f'Bot {client.token}'}
        try:
            async with client.session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f'Error fetching channel: {e}')
            return None

    async def send(self, content=None, *, tts=False, embed=None, delete_after=None,
                   nonce=None, allowed_mentions=None):
        return await self.client.send(ctx=self, content=content, tts=tts, embed=embed,
                                      delete_after=delete_after, nonce=nonce,
                                      allowed_mentions=allowed_mentions)

    async def delete_message(self, message_id=None):
        if message_id is None:
            message_id = self.message['id']
        return await self.client.delete_message(ctx=self, message_id=message_id)

    async def edit_message(self, message_id=None, content=None, embed=None):
        if message_id is None:
            message_id = self.message['id']
        return await self.client.edit_message(ctx=self, message_id=message_id, content=content, embed=embed)

    class Channel:
        def __init__(self, id):
            self.id = id

    class User:
        def __init__(self, user_info):
            self.id = user_info.get('id', None)
            self.name = user_info.get('username', None)
            self.discriminator = user_info.get('discriminator', None)
            self.bot = user_info.get('bot', False)
            self.avatar = user_info.get('avatar', None)
            self.system = user_info.get('system', False)
            self.public_flags = user_info.get('public_flags', 0)
            self.flags = user_info.get('flags', 0)
            self.locale = user_info.get('locale', None)
            self.mfa_enabled = user_info.get('mfa_enabled', False)
            self.verified = user_info.get('verified', False)
            self.email = user_info.get('email', None)