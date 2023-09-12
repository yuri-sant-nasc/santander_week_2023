sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app' #link da APi

import pandas as pd
df = pd.read_csv('SDW2023.csv')
user_ids = df ['UserID'].tolist()





import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))


openai_api_key = 'TODO' #chave ficticia

import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "santander-dev-week-2023-api",
      "description": news
  })



  def upadate_user(user):
    response = requests.put(f"{swd2023_api_url}/users/{user['id'], }"json=user)
    return True if response. status_code ==200 else False
  for user in users:
    sucess = upadate_user(user)
    print(f"user{user['name']}updated?{sucess}!")
