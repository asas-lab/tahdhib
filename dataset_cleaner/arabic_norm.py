
import re

def normalize(
     text,
    remove_special_char=False,
    remove_tatweel=False,
    remove_harkat=False,
    remove_html=False,
    remove_javascript=False,
    remove_citation=False,
    unified_alf=False,
    unified_yaa=False,
    freq_word_removel=False,
    repetetion_removel=False,
    remove_diacritics=False,
    remove_extrawhitespace=False,
    special_characters = None,):


    # Arabic unicode block range
    arabic_range = '\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF'

    if remove_harkat == True:
        # 1. Normalize Arabic diacritics (Tashkeel)
        tashkeel_pattern = re.compile(r'[\u0617-\u061A\u064B-\u0652\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED]')
        text = re.sub(tashkeel_pattern, '', text)

    if unified_alf== True:
        # 2. Standardize Arabic characters
        # Replace Alif variants with bare Alif
        text = re.sub(r'[\u0622\u0623\u0625\u0671\u0672\u0673\u0675]', '\u0627', text)

    if unified_yaa == True:
        # Replace Yaa variants with bare Yaa
        text = re.sub(r'[\u0649]', '\u064A', text)

    if remove_tatweel == True:
        # 3. Remove Tatweel (Kashida)
        text = re.sub(r'\u0640', '', text)

    if remove_extrawhitespace:
        # Normalize whitespace
        text = ' '.join(text.split())

    # Remove non-Arabic characters - Replaced with special_characters
    #text = re.sub(r'[^\s' + arabic_range + ']', '', text)
    if special_characters != None:
        # Remove special characters like "!.*()?"#
        pattern = '[' + re.escape(special_characters) + ']'
        re.sub(pattern, '', text)

    return text
