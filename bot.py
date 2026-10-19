import os
import discord
import random
import requests
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

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    # Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('woof')
async def woof(ctx):
    # Uma vez que chamamos o comando woof, o programa chama a função get_dog_image_url
    image_url = get_dog_image_url()
    await ctx.send(image_url)



bot.run(os.getenv("DISCORD_TOKEN"))