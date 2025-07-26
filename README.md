# 🌡️ VibeCheck API (Bizu do Boto)

Seu termômetro de sentimentos direto da Amazônia — agora ainda mais afinado com estrelas, emoções e confiança.

---

## 🎯 Sobre o Projeto

A **VibeCheck API** é um microsserviço desenvolvido com **FastAPI** que realiza análise de sentimento em textos em português. Utilizamos um modelo de linguagem robusto para mapear o texto para emoções humanas como "positivo", "neutro" e "negativo", e ainda oferecemos uma **polaridade numérica** e um **grau de confiança**.

---

## 🧠 Como Funciona

A API usa o modelo `nlptown/bert-base-multilingual-uncased-sentiment`, que atribui uma nota de 1 a 5 estrelas para o texto. Traduzimos essa nota para:

| Estrelas | Emoção    | Polaridade |
|----------|-----------|------------|
| 5        | positivo  | +1.0       |
| 4        | positivo  | +0.5       |
| 3        | neutro    |  0.0       |
| 2        | negativo  | -0.5       |
| 1        | negativo  | -1.0       |

---

## 🚀 Como usar

### ▶️ Rota principal

`POST /analisar-sentimento`

### 📤 Requisição (JSON)

```json
{
  "text": "Eu amei este produto! É incrível e perfeito."
}
```

### 📥 Resposta

```json
{
  "emotion": "positivo",
  "polarity": 1.0,
  "confidence": 0.9876
}
```

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/briellll/VibeCheck_API.git
cd VibeCheck_API
```

2. Crie o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Instale as dependências com [Poetry](https://python-poetry.org/):

```bash
poetry install
```

---

## 🧪 Testes

Os testes cobrem todos os cenários de análise de sentimento, incluindo casos positivos, negativos, neutros e erros de schema:

```bash
poetry run pytest
```

---

## 🧰 Tech Stack

- 🔥 FastAPI
- 🤗 Transformers (`nlptown/bert-base-multilingual-uncased-sentiment`)
- 🧪 Pytest
- 📦 Poetry

---

## 🐍 Exemplo de código para chamada com `requests`

```python
import requests

response = requests.post(
    "http://localhost:8000/analisar-sentimento",
    json={"text": "Esse serviço foi excelente!"},
)
print(response.json())
```

---

## ✨ Resultado esperado

Você terá como resposta:
- `emotion`: a emoção extraída do texto (`positivo`, `neutro`, `negativo`)
- `polarity`: um valor entre -1.0 e 1.0 indicando a força do sentimento
- `confidence`: o quão confiante o modelo está nessa classificação

---

## 📬 Contato

Criado por [@briellll](https://github.com/briellll) — o boto dev 🐬

---
