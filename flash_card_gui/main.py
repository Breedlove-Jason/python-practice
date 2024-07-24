import os

import pandas as pd
import requests
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")


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


def create_translation_dict(tagalog_words):
    translation_dict = {}
    for word in tagalog_words:
        english_translation = translate_word(word)
        translation_dict[word] = english_translation
        print(
            f"Translated {word} to {english_translation}"
        )  # Optional: for monitoring progress
    return translation_dict


FILE = "tl_full.txt"
df = pd.read_csv(FILE, sep=" ")
tagalog_words = df.iloc[:, 0].tolist()
# print(tagalog_words)

# Example of translating the first word and printing it
english_word = translate_word(tagalog_words[200])
print(f"Tagalog: {tagalog_words[200]}, English: {english_word}")


def save_translations_to_csv(translation_dict, file_path):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(list(translation_dict.items()), columns=["Tagalog", "English"])
    # Save DataFrame to CSV
    df.to_csv(file_path, index=False)


# Assuming tagalog_words is already loaded and available
translation_dict = create_translation_dict(tagalog_words)
save_translations_to_csv(translation_dict, "translations.csv")
