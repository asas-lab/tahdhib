import re

def normalize_arabic(text):
    # Arabic unicode block range
    arabic_range = '\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF'

    # 1. Normalize Arabic diacritics (Tashkeel)
    tashkeel_pattern = re.compile(r'[\u0617-\u061A\u064B-\u0652\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED]')
    text = re.sub(tashkeel_pattern, '', text)

    # 2. Standardize Arabic characters
        
    # Reason: there are variation of the same letetr 
    # though they might held importance in dectation, their importance in meaning 
    # -such as changing the meaning of the word when we return them to their original form-
    # has less to no significance importance
        
    # Replace Alif variants with bare Alif (ٱ،إ،أ،آ)
    text = re.sub(r'[\u0622\u0623\u0625\u0671\u0672\u0673\u0675]', '\u0627', text)
    # Replace Yaa variants with bare Yaa (ي،ى)
    text = re.sub(r'[\u0649]', '\u064A', text)
    # Replace Taa Marbuta to Ha (ة،ه)
    text = re.sub(r'ة\b', 'ه', text)

    # 3. Remove Tatweel (Kashida)
    text = re.sub(r'\u0640', '', text)

    # 4. Remove empty lines 
    text = re.sub(r'\n+', '\n', text)  # Replace multiple newlines with a single one
    text = re.sub(r'^\s*$', '', text, flags=re.MULTILINE)  # Remove empty lines
    
    # 5.Normalize whitespace
    text = ' '.join(text.split())

    return text


#%%
# For file content read with '.read()'
with open('scraped_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
normalized_content = normalize_arabic(content)


