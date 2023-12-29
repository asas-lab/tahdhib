import pandas as pd
import numpy as np
from collections import Counter

def word_count(text):
    return len(text.split(" "))

def char_count(text):
    return len(text)

def sentence_count(text):
    return len(text.split("."))

def basic_stats(text):
    word_count_stats = word_count(text).describe()
    char_count_stats = char_count(text).describe()
    return pd.concat([word_count_stats, char_count_stats], axis=1)

def vocab(text):
    all_words = text.split(" ")
    vocab = Counter(all_words)
    return vocab

def Most_Common_Words(text, n):
    vocab_dict = vocab(text)
    return vocab_dict.most_common(n)

def Least_Common_Words(text, n):
    vocab_dict = vocab(text)
    return vocab_dict.most_common()[:-n-1:-1]

def word_freq(text, word):
    vocab_dict = vocab(text)
    return vocab_dict[word] / len(text.split(" "))

def char_freq(text, char):
    return text.count(char) / len(text)

def avg_word_length(text):
    return char_count(text) / word_count(text)

def avg_sentence_length(text):
    return word_count(text) / sentence_count(text)
