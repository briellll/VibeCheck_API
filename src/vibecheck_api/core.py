from transformers import pipeline # type: ignore

sentiment_analyzer = pipeline(
    'sentiment-analysis',  # type: ignore
    model='nlptown/bert-base-multilingual-uncased-sentiment',
)


def analyze(text: str) -> dict:
    result = sentiment_analyzer(text)
    main_result = result[0]
    label = main_result['label']
    score = main_result['score']

    if label in {'5 stars', '4 stars'}:
        sentiment = 'positivo'
    elif label in {'1 star', '2 stars'}:
        sentiment = 'negativo'
    else:
        sentiment = 'neutro'

    return {'emotion': sentiment, 'polarity': score}
