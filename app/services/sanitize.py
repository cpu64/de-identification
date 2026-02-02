# app/services/sanitize.py
"""
Mock NER prediction for testing the validation tool UI.

Returns entity predictions as [start, end, entity_type] for every other word.
"""
import random
import re
import asyncio


ENTITY_TYPES = [
    'PER', 'ID_PER', 'ID_MISC', 'NUM_CAR', 'NUM_PHONE',
    'LOC', 'ORG', 'NAT', 'OCC', 'EDU', 'AGE', 'TIME',
    'DATE', 'DURATION', 'VALUE', 'MISC',
    'REL', 'POL', 'SEX', 'GENDER', 'MAR', 'FAM', 'ETH', 'HEALTH'
]

def predict(text):
    """Return mock NER predictions for every other word."""
    entities = []
    words = list(re.finditer(r'\b\w+\b', text))

    for i, match in enumerate(words):
        if i % 2 == 0:
            entities.append([match.start(), match.end(), random.choice(ENTITY_TYPES)])

    return entities

async def sanitize(text: str) -> str:
    """
    Replace predicted entities in text with their entity type in brackets.
    Preserves non-entity text unchanged.
    """
    predictions = predict(text)
    sanitized_text = ""
    last_index = 0

    for start, end, entity_type in predictions:
        sanitized_text += text[last_index:start]
        sanitized_text += f"[{entity_type}]"
        last_index = end

    sanitized_text += text[last_index:]

    await asyncio.sleep(1) # simulate a call to our server
    return sanitized_text

