import os, re, time, requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from urllib.parse import quote, urlparse, parse_qs

# Class 호출.
from app.data_logging import logging

class DataCrawling:
    def __init__(self, uri):
        # 기록을 위한 logger 생성.
        self._logger = logging._get_log()

        # 크롤링에 필요한 기본 값 정의.
        self._craw_uri = uri

        # Chrome을 실행하기 위한 설정.
        chrome_options = Options()
        chrome_service = Service(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        # 초기 URI로 이동.
        self._driver.get(self._craw_uri)