import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print("RussellBot332 running...")

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game(name="rs help", type=3))
    print("Status is set!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "rs help":
        await message.channel.send("**Help!**\nType \"rs <sentence>\" to start chatting!\nExample: rs Hello, how are you?")
    elif message.content.startswith("rs"):
        response = chatbot.request(message.content[3:])
        await message.channel.send(response)

client.run(TOKEN)