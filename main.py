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
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$russell"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

client.run(TOKEN)