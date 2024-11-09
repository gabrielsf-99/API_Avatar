import requests
import json
from googletrans import Translator

def personagens():
    url_api = f'https://last-airbender-api.fly.dev/api/v1/characters'

    r = requests.get(url_api)
    personagens = r.json()

    print(personagens)
    tradutor = Translator()

    for personagem in personagens:
        afiliacao = personagem.get("affiliation","N/A")
        nome = personagem.get("name","Sem Nome")
        afiliacao_pt = tradutor.translate(afiliacao, dest="pt").text
        nome_pt = tradutor.translate(nome,dest="pt").text
        print(f'{nome_pt}: {afiliacao_pt}')

personagens ()
