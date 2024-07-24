import os

import pandas as pd
import requests
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()


def translate_word(word):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": word,
        "source": "tl",
        "target": "en",
        "format": "text",
        "key": os.getenv("GOOGLE_TRANSLATE_API_KEY"),
    }
    response = requests.get(url, params=params)
    result = response.json()
    return result["data"]["translations"][0]["translatedText"]


# Access the API key
api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
# Just to demonstrate, remove or secure this line in production
FILE = "tl_full.txt"
df = pd.read_csv(FILE, sep=" ")
tagalog_words = df.iloc[:, 0].tolist()
# print(tagalog_words)

# Example of translating the first word and printing it
english_word = translate_word(tagalog_words[200])
print(f"Tagalog: {tagalog_words[200]}, English: {english_word}")
