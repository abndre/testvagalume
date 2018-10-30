# - coding: utf-8 --
import bs4
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


link = 'https://www.vagalume.com.br/'