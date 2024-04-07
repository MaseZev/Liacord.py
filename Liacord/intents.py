class Intents:
    def __init__(self):
        self.bits = 0

    def guilds(self):
        self.bits |= 1 << 0
        return self

    def guild_members(self):
        self.bits |= 1 << 1
        return self

    def guild_moderation(self):
        self.bits |= 1 << 2
        return self

    def guild_emojis_and_stickers(self):
        self.bits |= 1 << 3
        return self

    def guild_integrations(self):
        self.bits |= 1 << 4
        return self

    def guild_webhooks(self):
        self.bits |= 1 << 5
        return self

    def guild_invites(self):
        self.bits |= 1 << 6
        return self

    def guild_voice_states(self):
        self.bits |= 1 << 7
        return self

    def guild_presences(self):
        self.bits |= 1 << 8
        return self

    def guild_messages(self):
        self.bits |= 1 << 9
        return self

    def guild_message_reactions(self):
        self.bits |= 1 << 10
        return self

    def guild_message_typing(self):
        self.bits |= 1 << 11
        return self

    def direct_messages(self):
        self.bits |= 1 << 12
        return self

    def direct_message_reactions(self):
        self.bits |= 1 << 13
        return self

    def direct_message_typing(self):
        self.bits |= 1 << 14
        return self

    def message_content(self):
        self.bits |= 1 << 15
        return self

    def guild_scheduled_events(self):
        self.bits |= 1 << 16
        return self

    def auto_moderation_configuration(self):
        self.bits |= 1 << 20
        return self

    def auto_moderation_execution(self):
        self.bits |= 1 << 21
        return self

    def all(self):
        self.bits = 2 ** 22 - 1
        return self

    def raw(self):
        return self.bits
