# 🌡️ VibeCheck API (Bizu do Boto)  
**Seu termômetro de sentimentos para textos em português, com uma pitada de IA direto da Amazônia.**

---

## 🎯 Sobre o Projeto

O **VibeCheck API** é um microsserviço esperto, construído com **FastAPI**, que analisa o sentimento de qualquer texto em português — do meme ao manifesto.  
Chega de IA gringa que trava no "açaí pai d’égua"! Aqui a vibe é tropical, com IA multilíngue da Hugging Face na jugular.

Use para analisar feedback de clientes, comentários em redes sociais ou descobrir se aquela mensagem no grupo foi carinho ou caos passivo-agressivo.

---

## ✨ Funcionalidades

- ✅ Análise de sentimento com alta precisão em **português** (e outras línguas!).
- ✅ Classificação em: `"positivo"`, `"negativo"` ou `"neutro"`.
- ✅ Retorno da **pontuação de polaridade/confiança** do modelo.
- ✅ Arquitetura moderna, assíncrona e escalável com **FastAPI**.
- ✅ **Validação de dados** com Pydantic.
- ✅ Documentação automática via **Swagger UI** (`/docs`) e **ReDoc** (`/redoc`).

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta        | Função                                             |
|-------------------|----------------------------------------------------|
| 🐍 Python 3.13     | Linguagem base                                     |
| ⚡ FastAPI + Uvicorn | Web framework assíncrono & servidor leve         |
| 🤗 Transformers   | Modelos de IA multilíngue (Hugging Face)           |
| 🔥 PyTorch        | Backbone matemático da IA                          |
| 📦 Poetry         | Gerenciamento de dependências & ambiente virtual   |
| 🧪 Pytest         | Testes para dormir tranquilo 😌                    |

---

## 🚀 Como Rodar o Projeto

### ⚙️ Pré-requisitos

- Python **3.13+**
- [Poetry](https://python-poetry.org/docs/#installation)

### 📥 Instalação

```bash
git clone https://github.com/briellll/vibecheck-api.git
cd vibecheck-api
poetry install
```

### ▶️ Rodando o Servidor

```bash
poetry run uvicorn vibecheck_api.main:app --reload
```

> ⚠️ **IMPORTANTE:**  
Na primeira execução, será feito o download (~500MB) do modelo `nlptown/bert-base-multilingual-uncased-sentiment`.  
Então relaxa, pega um açaí e deixa que o boto cuida.

---

## 📚 Documentação Interativa

- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🕹️ Exemplo de Uso via `curl`

```bash
curl -X 'POST'   'http://127.0.0.1:8000/analisar-sentimento'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{
    "texto": "Esse açaí com peixe frito tava pai d'''égua demais!"
}'
```

### 🔄 Resposta da API

```json
{
  "sentimento": "positivo",
  "polaridade": 0.9825,
}
```

---

## 🧪 Rodando os Testes

```bash
poetry run pytest
```

---

### 🎶 Rodado nas madrugadas amazônicas,  
com café, código e o som dos grilos de Santarém-PA. 🇧🇷
