import json
import os
import time
from selenium import webdriver
from google.cloud import storage

def main(request):

    # chrome_options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.binary_location = os.getcwd() + "/headless-chromium"

    driver = webdriver.Chrome(
        os.getcwd() + "/chromedriver", chrome_options=chrome_options)

    # set url
    url = 'https://www.yahoo.co.jp/'
    driver.get(url)

    # file name
    file_name = "screenshot.png"

    # save screenshot
    time.sleep(5)
    driver.save_screenshot("/tmp/{}".format(file_name))

    # upload google cloud storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('YOUR_BUCKET_NAME')
    blob = bucket.blob("img/{}".format(file_name))
    blob.upload_from_filename("/tmp/{}".format(file_name))

    driver.quit()
    return "screenshot upload finished"
