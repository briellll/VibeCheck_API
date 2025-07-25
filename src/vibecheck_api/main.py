from http import HTTPStatus

from fastapi import FastAPI

from .core import analyze
from .schemas import ResultAnalysis, TextForAnalysis

app = FastAPI()


@app.post(
    '/analisar-sentimento',
    status_code=HTTPStatus.OK,
    response_model=ResultAnalysis,
)
def analyze_sentiment(text: TextForAnalysis):
    sentiment_text = text.text

    sentiment = analyze(sentiment_text)

    return sentiment
