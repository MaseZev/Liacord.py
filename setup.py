from setuptools import setup

readme = ''
with open('README.md') as f:
    readme = f.read()

setup(name='Liacord',
      author="Masezev",
      url="https://github.com/masezev/Liacord.py",
      project_urls={
          'Discord': 'https://discord.gg/H7FQFGEPz5',
      },
      repository='https://github.com/masezev/Liacord.py',
      version='0.1.6',
      description='A Python wrapper for the Discord API',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      python_requires='>=3.8.0',
      keywords='A Python wrapper for the Discord API',
      install_requires=[
            'aiohttp'
      ],
      packages=['Liacord'],
      license='MIT',
      author_email='csgomanagement1@gmail.com',
      zip_safe=False)
