from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def start_driver():
    """
    Starting the web driver
    """
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager(version='104.0.5112.20').install(), options=options)
    return driver


