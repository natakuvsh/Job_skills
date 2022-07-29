from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from stop_words import get_stop_words


def clean_text(word_tokens, nlp):
    stop_words = set(stopwords.words('english'))
    stop_words_russian = get_stop_words('russian')
    text_without_stopwords = [w for w in word_tokens if not w.text.lower() in stop_words and not w.text.lower() in stop_words_russian]
    text_without_symbols = [w.text.lower() for w in text_without_stopwords if not w.text in r"""  \n!"#$%&()*+,./:;<=>?@[\]^_`{|}~"""]
    oov_text = [w for w in text_without_symbols if not w in nlp.vocab]
    return oov_text


def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]