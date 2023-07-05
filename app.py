from flask import Flask, jsonify
from fetch_verse_transliteration import fetch_a_verse, get_transliteration

app = Flask(__name__)


@app.route('/verse_transliteration/<int:book_index>/<int:chapter>/<int:verse>', methods=['GET'])
def get_verse_and_inference(book_index, chapter, verse):
    # get verse citation information from command line interface
    verse_text = fetch_a_verse(book_index, chapter, verse)

    # Make inference using the machine learning model
    inference = get_transliteration(verse_text)

    return jsonify({
        'verse': verse_text,
        'transliteration': inference
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
