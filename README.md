# Bible Verse Transliterator

## Introduction
***Why transliteration?***

Many people I have come across in both religious and non-religious communities outside of Israel (mostly New York and London) want to study Bible, and they want to do so in the original Hebrew!
There is no end to the number of Translations of the Bible, but a robust transliteration is hard to come by.

This Flask application allows users to enter a biblical book, chapter, and verse number and retrieve the corresponding text from the Bolls.life Bible API. Additionally, it utilizes the TaatikNet inference model, trained by Morris Alper, to provide a transliteration of the selected verse from Hebrew to Latin letters.

<div align="center">
    <img src="https://joelmhoffman.files.wordpress.com/2009/12/hebrew-transliteration.png" alt="Image" height="175">
</div>

## Functionality
The application has the following two features:

### 1. Retrieve Biblical Text
Users can input a Biblical book, chapter, and verse number of their choice. The application then queries the Bolls.life Bible API and fetches the corresponding text for the specified verse.
* Note: Each Biblical book is retrieved by its index, not its name. (E.g. Genesis is 1, Joshua is 6, etc.)

### 2. Hebrew-to-Latin Transliteration
To enhance the user experience, the application incorporates the **TaatikNet** inference model which was trained by **Morris Alper** as a demonstration of seq2seq training. It sends a request to the inference API, which utilizes TaatikNet to generate a transliteration of the selected verse from Hebrew to Latin letters.
This facilitates readers to study texts by first reading it in the original pronunciation (albeit in Latin letters).
* To learn about the training of this model, see Alper's crystal-clear Jupyter notebook in [this GitHub repo](https://github.com/morrisalp/taatiknet).
## Usage
To use this application locally, follow these steps:

(You know most of these steps, but just for completeness...)
* **Note:** the command-line prompts are based on Windows, and may need to be adapted for OS or Linux.

1. Clone the repository:
```
git clone https://github.com/your-repo
```
2. Install the required dependencies:
```commandline
pip install -r requirements.txt
```

3. Run the Flask application:
```commandline
python app.py
```

4. Make sure your configurations are right:
* A configuration template has been provided in this repo (`config_template.json`), but you must edit it to include your personal `API_TOKEN` with Hugging Face.
* After your edit, change the name of the config file using the following code in the command line:
```commandline
ren "config_template.json" "config.json"
```

5. Open another command line, and run the client file:
```commandline
python client.py
```
6. Choose your desired Biblical Book, Chapter and Verse:
   (This is what the command line interface will look like when you've inputted an integer for all three prompts.)
```commandline
python client.py
Enter the book index: 1
Enter the chapter: 1
Enter the verse: 1
```

7. Your output will (hopefully!) look something like this:
```commandline
Verse:
בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ

Transliteration:
boreshít baráf elohím et hashamáyim veét haaréts.
```
* **Note:** You'll notice that the transliteration has some oddities and mistakes. More can be done to preprocess the verses than has been done here.

## Dependencies
The following dependencies are required to run the application:

- Flask: Web framework for building the application.
- requests: Library for making HTTP requests to the Bolls.life Bible API and the Hugging Face inference API.

## Credits
- The Bolls.life Bible API (https://bolls.life) for providing the biblical text data.
- Morris Alper for training the TaatikNet inference model used for transliteration.
  - [Alper's GitHub Profile](https://github.com/morrisalp)
  - [His 'Towards Data Science' Article on the topic](https://towardsdatascience.com/taatiknet-sequence-to-sequence-learning-for-hebrew-transliteration-4c9175a90c23)
- Hugging Face (https://huggingface.co) for hosting the inference API.

***Thank you for stopping by this repo - I hope you enjoyed!***


Be in touch anytime:<br> 
[LinkedIn Profile](www.linkedin.com/in/yabrams)
<br><br>
הכל בס"ד
