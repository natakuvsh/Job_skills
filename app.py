import spacy
from utils import selenium_driver, utils, text_utils
from utils import url_generator


def run():
    """
    Taking job title from the user, scraping work.ua website for job descriptions,
    :return: 'django' : 10
    """

    # Asks the user to enter job title
    search_job = input('What is the job title you are searching for?(Please use english name) ')
    driver = selenium_driver.start_driver()

    # Saves job links in a list
    job_links = []
    for page in range(1, 5):
        url = url_generator.generate_url(search_job, page)
        driver.get(url)
        print('Waiting for page to load...')
        job_cards = (utils.collect_job_cards_from_page(driver))
        job_link = utils.collect_job_links(job_cards)
        print(f'Collected job links from page {page}...')
        job_links.extend(job_link)

    # Saves job descriptions
    job_descriptions = utils.get_job_descriptions(driver, job_links)
    print('Collected job descriptions.')

    driver.quit()

    # Downloads nlp and makes tokenization
    nlp = spacy.load("en_core_web_sm")
    content = ''.join(job_descriptions)
    word_tokens = nlp(content)

    # Cleans the text from stopwords, punctuation marks
    print('Cleaning the text to find most frequently appearing words...')
    clean_job_description_words = text_utils.clean_text(word_tokens, nlp)

    # Selects top 15 words(skills) for job title
    top_words = text_utils.get_top_n_words(clean_job_description_words, 15)

    print('\n\n\n')
    print('The most frequently appearing skills are:')
    for i in top_words:
        print(str(i[0]) + ':' + str(i[1]))


if __name__ == "__main__":
    run()