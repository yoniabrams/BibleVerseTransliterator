import requests

base_url = 'http://localhost:5000/verse_transliteration/'


if __name__ == "__main__":
    book_index = int(input('Enter the book index: '))
    chapter = int(input('Enter the chapter: '))
    verse = int(input('Enter the verse: '))

    url = f"{base_url}{book_index}/{chapter}/{verse}"
    response = requests.get(url)

    if response.status_code == 200:
        # Get and Print results
        result = response.json()
        verse_text = result['verse']
        transliteration = result['transliteration']
        print(f'Verse:\n{verse_text}')
        print(f'Transliteration:\n{transliteration}')
    else:
        print('Failed to fetch verse and inference.')
