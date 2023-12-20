import re

def normalize_arabic(text):
    # Arabic unicode block range
    arabic_range = '\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF'


    # Function to apply normalization rules to a single text block or line
    def normalize_text_block(text):
        # 1. Normalize Arabic diacritics (Tashkeel)
        tashkeel_pattern = re.compile(r'[\u0617-\u061A\u064B-\u0652\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED]')
        text = re.sub(tashkeel_pattern, '', text)

        # 2. Standardize Arabic characters
        # Replace Alif variants with bare Alif
        text = re.sub(r'[\u0622\u0623\u0625\u0671\u0672\u0673\u0675]', '\u0627', text)
        # Replace Yaa variants with bare Yaa
        text = re.sub(r'[\u0649]', '\u064A', text)

        # 3. Remove Tatweel (Kashida)
        text = re.sub(r'\u0640', '', text)
                
        # 4.Normalize whitespace
        text = ' '.join(text.split())

        return text

    # 5. Remove empty lines 
    # if it is a text block
    if isinstance(text, str):
        text = normalize_text_block(text)
        text = re.sub(r'\n+', '\n', text)  # Replace multiple newlines with a single one
        text = re.sub(r'^\s*$', '', text, flags=re.MULTILINE)  # Remove empty lines

    # if it is line in a list
    elif isinstance(text, list):
        text = [normalize_text_block(line) for line in text]
        text = [line for line in text if line.strip()]  # Remove empty or whitespace-only lines

    return text


#%%
# For file content read with '.read()'
with open('scraped_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
normalized_content = normalize_arabic(content)

# For file content read with '.readlines()'
with open('scraped_data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
normalized_lines = normalize_arabic(lines)

