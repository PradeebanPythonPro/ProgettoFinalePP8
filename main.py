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
    await ctx.send(f"Ciao {ctx.author.name}! Sono un bot che ti aiuterà nell'informarti riguardo al cambiamento climatico!")

@bot.command()
async def articolo(ctx):
    await ctx.send(random_article())

@bot.command()
async def video(ctx):   
    await ctx.send(random_video()) 

@bot.command()
async def fatto(ctx):
    fatti = [
        "La temperatura media globale è aumentata di circa 1,1°C dal 1880.",
        "I 10 anni più caldi mai registrati sono tutti successivi al 2010.",
        "Lo scioglimento dei ghiacciai contribuisce all'innalzamento del livello del mare.",
        "Ogni anno vengono distrutti circa 10 milioni di ettari di foreste.",
        "La CO₂ resta nell'atmosfera per centinaia di anni."
    ]
    await ctx.send(random.choice(fatti))

@bot.command()
async def consiglio(ctx):
    consigli = [
        "Spegni le luci quando esci da una stanza.",
        "Preferisci la bici o i mezzi pubblici all'auto.",
        "Riduci l'uso della plastica monouso.",
        "Mangia meno carne e più vegetali.",
        "Compra prodotti locali e di stagione.",
        "Installa lampadine a basso consumo."
    ]
    await ctx.send(f"🌱 Consiglio per te: {random.choice(consigli)}")

@bot.command()
async def co2(ctx):
    azioni = [
        ("usare i mezzi pubblici per un mese", 120),
        ("piantare un albero", 22),
        ("evitare carne per una settimana", 30),
        ("spegnere i dispositivi in stand-by", 10),
    ]
    scelta = random.choice(azioni)
    await ctx.send(f"🌍 {ctx.author.name}, facendo **{scelta[0]}**, puoi risparmiare circa **{scelta[1]} kg** di CO₂!")


@bot.command()
async def statistica(ctx):
    statistiche = [
        "Nel 2023, le emissioni globali di CO₂ hanno raggiunto i 36,8 miliardi di tonnellate.",
        "Il livello del mare è aumentato di 8 cm dal 1993.",
        "Il 2023 è stato l'anno più caldo mai registrato.",
        "Ogni minuto si distruggono foreste equivalenti a 27 campi da calcio."
    ]
    await ctx.send(f"📊 Statistica: {random.choice(statistiche)}")

quizzes = [
    {
        "domanda": "Qual è la principale causa del cambiamento climatico?",
        "opzioni": ["A) I vulcani", "B) Le attività solari", "C) L'attività umana", "D) I cicli naturali"],
        "corretta": "C"
    },
    {
        "domanda": "Quale gas serra è più abbondante nell'atmosfera?",
        "opzioni": ["A) Ossigeno", "B) CO₂", "C) Metano", "D) Azoto"],
        "corretta": "B"
    },
    {
        "domanda": "Quale settore produce più emissioni di gas serra a livello globale?",
        "opzioni": ["A) Agricoltura", "B) Trasporti", "C) Industria", "D) Produzione di energia"],
        "corretta": "D"
    },
]
current_quiz = {}

@bot.command()
async def quiz(ctx):
    global current_quiz
    domanda = random.choice(quizzes)
    current_quiz[ctx.author.id] = domanda["corretta"]
    testo = f"🧠 **Quiz:** {domanda['domanda']}\n"
    for opzione in domanda["opzioni"]:
        testo += f"{opzione}\n"
    testo += "\nRispondi con `$rispondi <lettera>` (es. `$rispondi C`)"
    await ctx.send(testo)

@bot.command()
async def rispondi(ctx, risposta: str):
    globale = current_quiz.get(ctx.author.id, None)
    if not globale:
        await ctx.send("❌ Non hai ancora ricevuto una domanda. Usa `$quiz` per iniziare.")
        return
    if risposta.upper() == globale:
        await ctx.send("✅ Esatto! Ottimo lavoro.")
    else:
        await ctx.send(f"❌ Sbagliato. La risposta corretta era **{globale}**.")
    current_quiz.pop(ctx.author.id)


bot.run("TOKEN")
#usate responsabilmente ciao ragazzi come state spero tutto bene
