import discord
from random import *
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant
from json import loads, dump
from urllib import request, parse

def read_dp():
	full_url = [DP_URL, '.body.json?lastUpdate=0']
	with request.urlopen(''.join(full_url)) as response:
		resp = response.read()

	return loads(resp.decode())['body']

load_dotenv()
TOKEN = os.getenv('TOKEN')
DP_URL = os.getenv('DP_URL')

try:
    with open("intents_dp.json", "w") as f:
        dump(loads(read_dp()), f)
        f.close()
    chatbot = GenericAssistant('intents_dp.json')
    game_name = "rs help"
except:
    chatbot = GenericAssistant('intents_lite.json')
    game_name = "rs help (DP down)"

chatbot.train_model()
chatbot.save_model()

print("RussellBot332 running...")

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = game_name, type = 3))
    print("Status is set!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "rs help":
        await message.channel.send("**HELP!**\nType \"rs <sentence>\" to start chatting with me!\nExample:\n```rs Hello, how are you?```")
    elif message.content == "rs xkcd":
        await message.channel.send(f"https://xkcd.com/{randint(1, 2515)}/")
    elif message.content.startswith("rs"):
        response = chatbot.request(message.content[3:])
        await message.channel.send(response)

client.run(TOKEN)