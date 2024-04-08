class EmbedBuilder:
    def __init__(self):
        self.embed = {}

    def set_title(self, title):
        self.embed['title'] = title
        return self

    def set_description(self, description):
        self.embed['description'] = description
        return self

    def set_color(self, color):
        self.embed['color'] = color
        return self

    def set_author(self, name, icon_url=None):
        self.embed['author'] = {'name': name}
        if icon_url:
            self.embed['author']['icon_url'] = icon_url
        return self

    def add_field(self, name, value, inline=False):
        if 'fields' not in self.embed:
            self.embed['fields'] = []
        self.embed['fields'].append({'name': name, 'value': value, 'inline': inline})
        return self

    def set_footer(self, text, icon_url=None):
        self.embed['footer'] = {'text': text}
        if icon_url:
            self.embed['footer']['icon_url'] = icon_url
        return self

    def set_url(self, url):
        self.embed['url'] = url
        return self

    def set_timestamp(self, timestamp):
        self.embed['timestamp'] = timestamp
        return self

    def set_image(self, url):
        self.embed['image'] = {'url': url}
        return self

    def set_thumbnail(self, url):
        self.embed['thumbnail'] = {'url': url}
        return self

    def set_video(self, url):
        self.embed['video'] = {'url': url}
        return self

    def set_provider(self, name, url=None):
        self.embed['provider'] = {'name': name}
        if url:
            self.embed['provider']['url'] = url
        return self

    def to_dict(self):
        return self.embed

    @staticmethod
    def embed(title=None, description=None, color=None):
        builder = EmbedBuilder()
        if title:
            builder.set_title(title)
        if description:
            builder.set_description(description)
        if color:
            builder.set_color(color)
        return builder