import requests
import json

# load configs file
with open("config.json", "r") as config_file:
    configs = json.load(config_file)

# configurations
BASE_BOLLS_URL = configs["base_bolls_url"]
DEFAULT_TRANSLATION = configs["default_translation"]
API_TOKEN = configs["hugging_face_api_configs"]["api_token"]
API_URL = configs["hugging_face_api_configs"]["api_url"]
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# # Uncomment if you want to load the model locally instead of requesting from Hugging Face API
# MODEL_TYPE = configs["hugging_face_api_configs"]["model_type"]
# TAATIKNET_MODEL = configs["hugging_face_api_configs"]["taatiknet_model_label"]


def fetch_a_verse(bible_book_index, chapter, verse):
    """
    Make request from 'bolls.life' Bible API from a book_index, chapter and verse
    :param bible_book_index: (int) Book of the bible [1-24]
    :param chapter: (int) Chapter of book.
    :param verse: (int) Verse #
    :return (list): list of words from the verse requested
    """
    # construct URL using base-url and reference variables
    api_request_url = f"{BASE_BOLLS_URL}/{DEFAULT_TRANSLATION}/{bible_book_index}/{chapter}/{verse}/"
    response = requests.get(api_request_url)  # returns a string in the form of a dict

    # parse response to extract verse
    if response.status_code == 200:
        text_dict = response.json()
        return text_dict["text"]
    else:
        return "Couldn't complete request."


def get_inference(verse):
    """
    :param verse: ([str, str, etc.]) The words of a Hebrew verse/sentence
    :return: inference (i.e. transliteration) from the taatiknet model on HuggingFace
    """
    while True:
        response = requests.post(API_URL, headers=headers, json=verse)
        if response is not None and response.status_code == 200:
          break
    return response.json()


def get_transliteration(verse):
    """
    This function makes an inference for what the proper transliteration from Hebrew
    to English would be, using Taatik Net (created by Morris Alper 2023)
    :param verse : (list or string) the Hebrew verse which the user wants to transliterate
    :return: a string of the transliterated verse
    """
    if not isinstance(verse, list):
        if isinstance(verse, str):
            # preprocess verse by removing common Biblical punctuation; split into a list
            verse = verse.replace("|", "")
            verse = verse[:-1]
            verse = verse.split()  # verse is now a list
        else:
            return "Error transliterating. Check input format."

    # # Uncomment if you want to load TaatikNet locally:
    # taatiknet_pipe = pipeline(MODEL_TYPE, model=TAATIKNET_MODEL)
    # transliterated_words = taatiknet_pipe(verse, num_beams=10, num_return_sequences=1, max_length=100)

    transliterated_words = get_inference(verse)

    # concatenate into a single string
    transliterated_verse = " ".join([d["generated_text"] for d in transliterated_words]) + "."

    return transliterated_verse
