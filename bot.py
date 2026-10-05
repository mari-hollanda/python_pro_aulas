import os
import discord
from dotenv import load_dotenv
from bot_logic import gen_pass
from discord.ext import commands

# Carrega as variáveis do arquivo .env
load_dotenv()

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá eu sou um bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send("Oi! Você falou comigo?")

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))