import fasttext

from huggingface_hub import hf_hub_download


import fasttext
import numpy as np

from huggingface_hub import hf_hub_download


def fast_text(text):
    model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
    model = fasttext.load_model(model_path)
    preds, scores = model.predict(text,k=219)

    if isinstance(scores, np.ndarray):
        scores = scores.tolist()

    for label, score in zip(preds, scores):
        if label == '__label__arb_Arab':
            return {'label': label, 'score': score}

    return {'label': result[0][0],
          'score': result[1][0]}


def cld3_pred(text):
    result = cld3.get_language("هلا")

    return {'label': result[0],
          'score': result[1]}
