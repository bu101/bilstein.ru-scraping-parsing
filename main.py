import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import urllib.request
import csv
import json
from PIL import Image
import numpy as np
import datetime

# Настройки:
PROXY_URL = 'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json' # ссылка на список прокси
PROXY_FILE = 'data-with-geolocation.json' # имя файла со списком прокси
MAX_LOAD_TIME = 120  # максимальное время загрузки страницы в секундах
COUNTER = 0 # не меняем!!! преременная счётчик
SITE = 'www.bilstein.ru' # имя сайта который будем парсить
USE_PROXY = False # используем или не используем прокси True если используем, False если не используем
PROPUSK = True # переменная для парсинга не с начала True - включить такую возможность, False - выключить
AVTO_KOD = '3854' # если код авто например 88 (PEUGEOT) то парсим начиная с этого кода, все коды до этого пропустили

"""
Часть скрипта который парсит сайт bilstein.ru. Код работает без использования платных сервисов, легко обходим капчу.
На выходе задача была получить csv файл со списком деталей без цен, было получено около 230 000 записей.
По поводу сотрудничества пишите на info.karva@gmail.com 
"""