#Automatic Dependency install
import discord
import os
import requests
from bs4 import BeautifulSoup

#Intializes the Discord Bot
client = discord.Client(intents=discord.Intents.default())


#Function to store variables
def get_player(player):
  """
  player: player name
  returns: 
  """
  player = player.split('#')
  tag = player[1]
  name = player[0]
  player = name + '%23' + tag
  response = requests.get(
      f"https://tracker.gg/valorant/profile/riot/{player}/overview")
  soup = BeautifulSoup(response.content, 'html.parser') 
  return soup


print(get_player("BaubbleTea#Boba"))


#Readying Bot
@client.event
async def on_ready():
  """
  This function is called when the bot is ready to start working.
  returns: None
  """
  print(f"Logged in as {client.user}")


#Recieving Message
@client.event
async def on_message(message):
  """
  message: message to be recieved
  returns: None
  """
  if message.author == client.user:
    return

  message = message.lower()
  if message.startswith("%"):
    await message.channel.send("Hello!")


client.run(os.environ['TOKEN'])
