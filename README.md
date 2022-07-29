# Top job skills requred from work.ua

A console-app which uses Selenium library and NLP tools to find top required skill for a job position, provided by user.
* Asks for job position.
* Gather all job descriptions for this position.
* Clean the text from stopwords, punctuation
* Checks if the word is not in spacy english vocabulary
* Use Count Vectorizer to count the frequency of the specific word
* Return result in pair 'skill' : 'frequency'

## • How To Install and Use

Install required libraries:
```
pip install requirements.txt
```
To run the script:
```
python3 app.py
```
