
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

        # remove_tatweel part need more testing coz the result was deleting the words that has it! 
    if remove_tatweel == True:
        # 3. Remove Tatweel (Kashida)
        text = re.sub(r'\u0640', '', text)

    # Remove non-Arabic characters - Replaced with special_characters
    #text = re.sub(r'[^\s' + arabic_range + ']', '', text)
    # I think we should have another function deals with non-Arabic char where we have all or part(specified what parts...)
    # then we have all the functions in one class
    
    if special_characters != None:
        # Remove special characters like "!.*()?"#
        pattern = '[' + re.escape(special_characters) + ']'
        # added 'text=' to save all the changes to text and return it at the end
        text = re.sub(pattern, '', text)
        
        # The part of normalizing white spaces must be the last step before the final output
    if remove_extrawhitespace:
        # Normalize whitespace
        text = ' '.join(text.split())

    return text
