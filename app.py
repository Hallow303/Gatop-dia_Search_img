import time
from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os, requests
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)

# Contador global
search_quota = 50
last_search_time = 0  # inicializamos com 0

@app.route("/", methods=["GET", "POST"])
def index():
    global search_quota, last_search_time
    image_url = None
    query = None
    name_input = None
    message = None  # mensagem para pop-up


    if request.method == "POST":
        current_time = time.time()
        query = request.form.get("query")
        query.lower()

        # calcula delay baseado na quota restante
        delay = max(0, (50 - search_quota) * 2)  # cada pesquisa faltando adiciona 2s

        if current_time - last_search_time < delay:
            # ainda dentro do tempo de espera → retorna gato404
            image_url = "/static/img/gato404.png"
            remaining = int(delay - (current_time - last_search_time))
            message = f"🕒 Aguarde {remaining} segundos antes de pesquisar novamente!"
        else:
            last_search_time = current_time
            if search_quota > 0:
                search_quota -= 1
                # busca real no Unsplash
                if query in ['gato', 'cat', 'felino', 'kitty', 'gatinho', 'mia', 'miauu']:
                    image_url = f'https://cataas.com/cat/says/Meow!'
                elif query in ['dog', 'cachorro', 'puppy', 'cao', 'doguinho', 'canino', 'latido']:
                    image_url = 'https://placedog.net/500?r'
                elif query in ['raposa', 'fox', 'raposinha', 'foxy', 'vulpes']:
                    resposta = requests.get('https://randomfox.ca/floof/')
                    data = resposta.json()  # retorna algo tipo {"image": "https://randomfox.ca/images/123.jpg", "link": "..."}
                    image_url = data['image']  # aqui sim pega a URL da imagem
                elif query in ['pato', 'duck', 'patinho', 'quack', 'anatidae']:
                    resposta = requests.get('https://random-d.uk/api/random')
                    data = resposta.json()  # {"url": "...", ...}
                    image_url = data['url']
                elif query in ['pessoa', 'rosto', 'face', 'humano', 'ser humano', 'portrait', 'human', 'cara']:
                    image_url = 'https://thispersondoesnotexist.com/'
                elif query in ['paisagem', 'natureza', 'landscape', 'cenário', 'montanha', 'praia', 'floresta', 'nature', 'vista']:
                    image_url = 'https://picsum.photos/800/600'
                else:
                    image_url = unsplash_search(query)
            else:
                # acabou a quota → retorna gato404
                image_url = "/static/img/gato404.png"
                message = "❌ Sua cota acabou! Aguarde para pesquisar novamente."

    return render_template("index.html", image_url=image_url, query=query, message=message)

def unsplash_search(query):
    key = os.environ.get("UNSPLASH_ACCESS_KEY")
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={key}&per_page=1"
    try:
        r = requests.get(url)
        data = r.json()
        if data.get("results"):
            return data["results"][0]["urls"]["regular"]
    except:
        pass
    return "/static/img/gato404.png"  # fallback se falhar

if __name__ == "__main__":
    app.run(debug=True)
