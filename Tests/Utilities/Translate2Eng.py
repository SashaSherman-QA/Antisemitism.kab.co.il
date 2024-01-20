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


def transliterate_hebrew_to_latin_mapping(hebrew_text):
    # Define a mapping of Hebrew to Latin characters
    char_mapping = {
        'א': 'a', 'ב': 'b', 'ג': 'g', 'ד': 'd', 'ה': 'h',
        'ו': 'v', 'ז': 'z', 'ח': 'ch', 'ט': 't', 'י': 'y',
        'כ': 'k', 'ך': 'kh',  # Final Kaf
        'ל': 'l', 'מ': 'm', 'ם': 'm',  # Final Mem
        'נ': 'n', 'ן': 'n',  # Final Nun
        'ס': 's', 'ע': 'a',
        'פ': 'p', 'ף': 'f',  # Final Pe
        'צ': 'ts', 'ץ': 'tz',  # Final Tsadi
        'ק': 'k', 'ר': 'r',
        'ש': 'sh', 'ת': 't'
    }

    # Replace each Hebrew character with its Latin equivalent
    latin_text = ''.join(char_mapping.get(char, char) for char in hebrew_text)

    return latin_text
