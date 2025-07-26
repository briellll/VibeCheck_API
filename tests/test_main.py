from http import HTTPStatus

from fastapi.testclient import TestClient

from vibecheck_api.core import (
    NEGATIVE_POLARITY,
    NEUTRAL_POLARITY,
    POSITIVE_POLARITY,
    SUPER_NEGATIVE_POLARITY,
    SUPER_POSITIVE_POLARITY,
)
from vibecheck_api.main import app

client = TestClient(app)


def test_sentiment_super_positive_should_return_5_stars_logic():
    payload = {'text': 'Eu amei este produto! É incrível e perfeito.'}

    response = client.post('/analisar-sentimento', json=payload)

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['emotion'] == 'positivo'
    assert data['polarity'] == SUPER_POSITIVE_POLARITY


def test_sentiment_moderately_positive_should_return_4_stars_logic():
    payload = {'text': 'Gostei bastante do filme, foi uma boa diversão.'}

    response = client.post('/analisar-sentimento', json=payload)

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['emotion'] == 'positivo'
    assert data['polarity'] == POSITIVE_POLARITY


def test_sentiment_neutral_should_return_3_stars_logic(monkeypatch):
    mock_response_from_core = {
        'emotion': 'neutro',
        'polarity': 0.0,
        'confidence': 0.99,
    }
    # monkeypatch : utilizado devido dificuldade de testar com neutro
    monkeypatch.setattr(
        'vibecheck_api.core.analyze',
        lambda text: mock_response_from_core,
    )

    payload = {'text': 'mockado'}

    response = client.post('/analisar-sentimento', json=payload)

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['emotion'] == 'neutro'
    assert data['polarity'] == NEUTRAL_POLARITY
    assert 'confidence' in data


def test_sentiment_moderately_negative_should_return_2_stars_logic():
    payload = {'text': 'Não gostei muito do final, esperava mais do roteiro.'}

    response = client.post('/analisar-sentimento', json=payload)

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['emotion'] == 'negativo'
    assert data['polarity'] == NEGATIVE_POLARITY


def test_sentiment_super_negative_should_return_1_star_logic():
    payload = {
        'text': 'Este serviço foi péssimo e a qualidade é horrível. Odiei.'
    }

    response = client.post('/analisar-sentimento', json=payload)

    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data['emotion'] == 'negativo'
    assert data['polarity'] == SUPER_NEGATIVE_POLARITY


def test_invalid_payload_schema_should_return_422():
    payload = {'mensagem': 'Este payload está errado'}

    response = client.post('/analisar-sentimento', json=payload)

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
