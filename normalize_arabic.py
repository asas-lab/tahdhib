import re

def normalize_arabic(text):
    # Arabic unicode block range
    arabic_range = '\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF'

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
    
    # 4. Remove non-Arabic characters
    # text = re.sub(r'[^\s' + arabic_range + ']', '', text)
    
    # 5. Normalize whitespace
    text = ' '.join(text.split())
    
    return text

# usage
# Read the scraped data from the file
with open('scraped_data.txt', 'r', encoding='utf-8') as file:
    scraped_data = file.readlines()

# Apply normalization to each piece of text
normalized_data = [normalize_arabic(text) for text in scraped_data]

# print 
for page_text in normalized_data:
    print(page_text)

