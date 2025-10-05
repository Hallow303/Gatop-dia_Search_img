# 🐱 **Gatopedia**

> "Porque toda busca merece um miado."

Gatopedia é um mini projeto divertido feito com **Flask**, inspirado na interface do **Google**, mas com um toque felino 🐈.
O usuário digita um termo e o site retorna uma imagem relacionada vinda da **Unsplash API**. Caso algo dê errado, um adorável **Gato 500** aparece para animar o erro.
🌐 **Teste online:** [gatopedia.hallowp.xyz](https://gatopedia.hallowp.xyz/)
---

## 🚀 **Tecnologias Utilizadas**

* 🐍 [Flask](https://flask.palletsprojects.com/) – Framework web em Python
* 🧱 [HTML5](https://developer.mozilla.org/docs/Web/HTML)
* 🎨 [CSS3](https://developer.mozilla.org/docs/Web/CSS)
* ⚡ [JavaScript](https://developer.mozilla.org/docs/Web/JavaScript)
* 🖼️ [Unsplash API](https://unsplash.com/developers) – Busca de imagens dinâmicas
* 🔒 [python-dotenv](https://pypi.org/project/python-dotenv/) – Gerenciamento de variáveis de ambiente

---

## 🗂️ **Estrutura do Projeto**

```bash
Gatopedia/
│
├── static/
│   ├── img/
│   │   ├── logo.png
│   │   ├── gato500.png
│   │   └── favicon.ico
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── .env
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ **Instalação e Execução**

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/gatopedia.git
cd gatopedia
```

### 2️⃣ Crie e ative o ambiente virtual

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure sua chave da API Unsplash

Crie um arquivo `.env` e adicione sua chave:

```bash
UNSPLASH_ACCESS_KEY=suachaveaqui
```

### 5️⃣ Execute o servidor

```bash
python app.py
```

### 6️⃣ Acesse o projeto

Abra no navegador:

```
http://127.0.0.1:5000
```

---

## 🧠 **Funcionalidades**

* 🔍 Interface inspirada no Google
* 🐾 Busca dinâmica de imagens
* ✨ Efeito “flástico” (vidro fosco translúcido)
* ⏳ Loader circular animado
* 🕒 Limite de buscas com tempo de espera
* 💬 Mensagens interativas de aviso
* 😹 Gato 500 personalizado para erros

---

## 🛡️ **Proteção da API Key**

A chave do Unsplash é armazenada em variáveis de ambiente, dentro do `.env`.
Lembre-se de **não subir esse arquivo** para o GitHub.
Adicione ao `.gitignore`:

```
.env
venv/
__pycache__/
```

---

## 💡 **Melhorias Futuras**

* 🌙 Alternar entre modo noturno e diurno automaticamente
* 💾 Implementar cache local para resultados
* 🐍 Adicionar suporte a outras APIs de imagem
* ☁️ Hospedar no Render, Railway ou Vercel

---

## 👨‍💻 **Autor**

Desenvolvido com ❤️ e 😺 por **Hallow**

---

<p align="center">
  <b>🐈‍⬛ Gatopedia — simples, elegante e cheio de miados!</b>
</p>

