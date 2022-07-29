import time
from random import random
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def sleep_for_random_interval():
    time_in_seconds = random() * 2
    time.sleep(time_in_seconds)


def collect_job_cards_from_page(driver):
    """
    Finding all cards for a specific job title
    :param driver: driver-object
    :return: list of card objects
    """
    job_cards = []
    for i in range(2,100):
        try:
            value = f'//*[@id="pjax-job-list"]/div[{i}]'
            job_card = driver.find_element(by=By.XPATH, value=value)
            job_cards.append(job_card)
        except NoSuchElementException:
            break
    return job_cards


def collect_job_links(job_cards):
    """
    Collects all the link to a full job descriptions from main page
    :param job_cards: list of card objects
    :return: list of links
    """
    links = []
    for card in job_cards:
        try:
            link = card.find_element(by=By.XPATH, value='.//h2/a').get_attribute('href')
            links.append(link)
        except NoSuchElementException:
            pass
    return links


def get_job_descriptions(driver, job_links):
    """
    Gets job description from every link
    :param driver: driver-object
    :param job_links: list of urls
    :return: list of strings
    """
    job_descriptions = []
    for link in job_links:
        driver.get(link)
        description = driver.find_element(by=By.XPATH, value='//*[@id="job-description"]').text.strip()
        job_descriptions.append(description)
        #name = driver.find_element(by=By.XPATH, value='//*[@id="h1-name"]').text.strip()
        sleep_for_random_interval()
    return job_descriptions