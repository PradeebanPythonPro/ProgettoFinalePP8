import discord
from discord.ext import commands
import os
import random
from archive import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def aiuto(ctx):
    await ctx.send(f"Ciao {bot.user}! Sono un bot che ti aiuterà nell'informarti riguardo al cambiamento climatico!")

@bot.command()
async def articolo(ctx):
    await ctx.send(random_article)

bot.run("INSERISCI TOKEN")
#usate responsabilmente ciao ragazzi come state spero tutto bene
#ciao sono fede e sto provando