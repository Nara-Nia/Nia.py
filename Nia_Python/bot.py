import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurações do bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Carregar módulos de comandos
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online!')
    await bot.change_presence(activity=discord.Game(name="!comandos"))

# Função para carregar as extensões (comandos)
async def load_extensions():
    await bot.load_extension('commands.admin')
    await bot.load_extension('commands.moderation')
    await bot.load_extension('commands.general')
    await bot.load_extension('commands.lock')

# Setup do bot, carregando as extensões
@bot.event
async def setup_hook():
    await load_extensions()

bot.run(TOKEN)
