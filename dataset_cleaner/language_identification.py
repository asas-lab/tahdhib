import fasttext

from huggingface_hub import hf_hub_download


def fast_text(text):
    model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
    model = fasttext.load_model(model_path)
    result = model.predict(text,k=219)
    return {'label': result[0][0],
          'score': result[1][0]}


def cld3_pred(text):
    result = cld3.get_language("هلا")

    return {'label': result[0],
          'score': result[1]}
