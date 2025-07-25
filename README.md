🌡️ VibeCheck API (Bizu do Boto)
Seu termômetro de sentimentos para textos em português, com uma pitada de IA direto da Amazônia.

🎯 Sobre o Projeto
O VibeCheck API é um microsserviço inteligente construído com FastAPI que analisa o sentimento de qualquer texto em português. Chega de usar modelos de IA "gringos" que não entendem o que significa um "açaí pai d'égua"!

Este projeto utiliza um poderoso modelo de linguagem multilíngue da Hugging Face para fornecer uma análise de sentimento precisa, classificando textos como positivo, negativo ou neutro. É a ferramenta perfeita para entender o feedback de clientes, analisar comentários em redes sociais ou simplesmente saber se aquela mensagem no grupo era um elogio ou puro sarcasmo.

✨ Funcionalidades
✅ Análise de sentimento de alta precisão em Português (e outras línguas!).

✅ Classificação clara em "positivo", "negativo" e "neutro".

✅ Retorna a pontuação de confiança (polaridade) do modelo de IA.

✅ Construído com uma arquitetura moderna e escalável usando FastAPI.

✅ Validação de dados de entrada e saída com Pydantic.

✅ Documentação interativa e automática com Swagger UI (/docs) e ReDoc (/redoc).

🛠️ Tecnologias Utilizadas
Esta API foi construída com as melhores ferramentas do ecossistema Python:

🐍 Python 3.13

✨ FastAPI & Uvicorn: Para a construção da API assíncrona de alta performance.

🤗 transformers (Hugging Face): A ponte para o universo dos modelos de IA de última geração.

🔥 PyTorch: O motor V12 que faz os cálculos pesados da nossa IA.

📦 Poetry: Para gerenciamento de dependências e do ambiente virtual.

🧪 Pytest: Para garantir que nossa API seja robusta e à prova de balas.

🚀 Como Rodar o Projeto
Para ter o VibeCheck API rodando na sua máquina local, siga estes simples passos.

Pré-requisitos
Ter o Python 3.13+ instalado.

Ter o Poetry instalado.

Instalação
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/vibecheck-api.git
Navegue até a pasta do projeto:

Bash

cd vibecheck-api
Instale as dependências com o Poetry:
(O Poetry criará um ambiente virtual e instalará tudo o que é necessário)

Bash

poetry install
Inicie o servidor da API:

Bash

poetry run uvicorn vibecheck_api.main:app --reload
⚠️ AVISO IMPORTANTE!
Na primeira vez que você iniciar o servidor, a biblioteca transformers irá baixar o modelo de IA (nlptown/bert-base-multilingual-uncased-sentiment), que tem cerca de 500MB. Isso pode demorar alguns minutos dependendo da sua conexão. Isso só acontece uma vez! Tenha um pouco de paciência e um açaí na mão.

Pronto! Sua API de IA já está no ar. Abra seu navegador e acesse:

Documentação Interativa (Swagger): http://127.0.0.1:8000/docs

🕹️ Como Usar a API
A maneira mais fácil de testar é usando a documentação interativa (/docs), onde você pode escrever o texto e ver a mágica acontecer.

Para usar via linha de comando (com curl):

Bash

curl -X 'POST' \
  'http://127.0.0.1:8000/analisar-sentimento' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "texto": "Esse açaí com peixe frito tava pai d'\''égua demais!"
}'
Estrutura da Resposta
A API retornará um JSON claro e direto com a análise:

JSON

{
  "sentimento": "positivo",
  "polaridade": 0.9825,
  "subjetividade": 0.0
}
🧪 Como Rodar os Testes
Para garantir que tudo está funcionando como deveria, execute a suíte de testes:

Bash

poetry run pytest
Feito nas madrugadas regadas a café e ao som dos grilos de Santarém-PA, Brasil. 🇧🇷