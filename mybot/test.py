import discord
import os
import requests
import json
import random



client = discord.Client()

#sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

#starter_encouragements = [
 # "Cheer up!",
  #"Hang in there.",
 # "You are a great person / bot!"
#]



def get_quote():
  response = requests.get("https://zenquotes.io/api/quotes")
  print(response.text)
  json_data = json.loads(response.text)
  print(json_data)
  quote = json_data[0]['q'] + " -" + json_data[0]['h']
  return(quote)

client.run('Nzk4MTcyNTUwNDMyODE3MjEz.X_xKHQ.NVh8SXUVIco3q9iQh33vOTyDuEY')