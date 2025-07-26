from transformers import pipeline  # type: ignore

SUPER_POSITIVE_POLARITY = 1.0
POSITIVE_POLARITY = 0.5
NEUTRAL_POLARITY = 0.0
NEGATIVE_POLARITY = -0.5
SUPER_NEGATIVE_POLARITY = -1.0


sentiment_analyzer = pipeline(
    'sentiment-analysis',  # type: ignore
    model='nlptown/bert-base-multilingual-uncased-sentiment',
)


def analyze(text: str) -> dict:
    result = sentiment_analyzer(text)
    main_result = result[0]
    label = main_result['label']
    score = main_result['score']

    if label == '5 stars':
        sentiment_label = 'positivo'
        polarity_score = SUPER_POSITIVE_POLARITY
    elif label == '4 stars':
        sentiment_label = 'positivo'
        polarity_score = POSITIVE_POLARITY
    elif label == '3 stars':
        sentiment_label = 'neutro'
        polarity_score = NEUTRAL_POLARITY
    elif label == '2 stars':
        sentiment_label = 'negativo'
        polarity_score = NEGATIVE_POLARITY
    else:  # 1 star
        sentiment_label = 'negativo'
        polarity_score = SUPER_NEGATIVE_POLARITY

    return {
        'emotion': sentiment_label,
        'polarity': polarity_score,
        'confidence': score,
    }
