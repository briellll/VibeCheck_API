from pydantic import BaseModel


class TextForAnalysis(BaseModel):
    text: str


class ResultAnalysis(BaseModel):
    emotion: str
    polarity: float
    confidence: float
