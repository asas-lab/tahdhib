import re

def remove_diacritics(text):
    tashkeel_pattern = re.compile(r'[\u0617-\u061A\u064B-\u0652\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED]')
    return re.sub(tashkeel_pattern, '', text)

def remove_non_useful_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'http[s]?://\S+', '', text)
    return text

def remove_repeated_characters(text):
    return re.sub(r'(.)\1+', r'\1\1', text)

def standardize_arabic_characters(text):
    text = re.sub(r'[\u0622\u0623\u0625\u0671\u0672\u0673\u0675]', '\u0627', text)
    text = re.sub(r'[\u0649]', '\u064A', text)
    text = re.sub(r'ة\b', 'ه', text)
    text = re.sub(r'ؤ', 'و', text)
    text = re.sub(r'ئ', 'ي', text)
    text = re.sub(r'ء', '', text)
    # there is an issue here coz if (ال) after (و) == and, it doesn't delete it coz it just delete (ال) if it exists at the beginning
    text = re.sub(r'\bال', '', text)
    return text

def remove_tatweel(text):
    return re.sub(r'\u0640', '', text)

def standardize_numbers(text):
    western_to_arabic_numerals = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
    return text.translate(western_to_arabic_numerals)

def remove_empty_lines(text):
    text = re.sub(r'\n+', '\n', text)
    return re.sub(r'^\s*$', '', text, flags=re.MULTILINE)

def normalize_whitespace(text):
    return ' '.join(text.split())

def normalize_arabic(text):
    text = remove_diacritics(text)
    text = remove_non_useful_text(text)
    text = remove_repeated_characters(text)
    text = standardize_arabic_characters(text)
    text = remove_tatweel(text)
    text = standardize_numbers(text)
    text = remove_empty_lines(text)
    text = normalize_whitespace(text)
    return text

#%%
# For file content read with '.read()'
with open('scraped_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
normalized_content = normalize_arabic(content)


