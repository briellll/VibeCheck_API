from http import HTTPStatus

from fastapi import FastAPI

from vibecheck_api import core

from .schemas import ResultAnalysis, TextForAnalysis

app = FastAPI()


@app.post(
    '/analisar-sentimento',
    status_code=HTTPStatus.OK,
    response_model=ResultAnalysis,
)
def analyze_sentiment(text: TextForAnalysis):
    sentiment_text = text.text

    sentiment = core.analyze(sentiment_text)

    return sentiment
