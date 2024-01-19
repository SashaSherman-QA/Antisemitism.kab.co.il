from googletrans import Translator

# def transliterate_hebrew_to_latin(hebrew_text):
#     translator = Translator()
#     # Detect the source language (Hebrew)
#     detected_lang = translator.detect(hebrew_text).lang
#     # Translate to English
#     english_text = translator.translate(hebrew_text, src=detected_lang, dest='en').text
#     return english_text

def transliterate_hebrew_to_latin(hebrew_text):
    # mimic user and not automation tool
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    translator = Translator(user_agent=user_agent)
    return translator.translate(hebrew_text, src='he', dest='en').text
