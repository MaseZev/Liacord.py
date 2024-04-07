class Context:
    def __init__(self, message, client):
        self.message = message
        self.channel = self.Channel(message['channel_id'])
        self.author = self.User(message['author'])
        self.guild = client.guild
        self.client = client

    async def send(self, content=None, *, tts=False, embed=None, delete_after=None,
                   nonce=None, allowed_mentions=None):
        return await self.client.send(content=content,ctx=self, tts=tts, embed=embed,
                                      delete_after=delete_after, nonce=nonce,
                                      allowed_mentions=allowed_mentions)

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
