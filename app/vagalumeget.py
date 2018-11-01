# - coding: utf-8 --
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import requests
import pdb
import os


from selenium.webdriver.chrome.options import Options as ChromeOptions


options = ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"
driver = webdriver.Chrome(chrome_options=options)


from bs4 import BeautifulSoup

def openartista(artista):
	link = 'https://www.vagalume.com.br/'
	#try:
	#	browser = webdriver.Chrome()
	#except:
	browser = webdriver.Chrome(chrome_options=options)
	#browser = webdriver.Chrome()
	browser.get(link)
	openpopustat =browser.find_element_by_xpath("//*[@class='icon-busca']")
	openpopustat.click()
	time.sleep(3)
	#pdb.set_trace()
	openpopustat =browser.find_element_by_xpath("//*[@class='searchField']")
	openpopustat.send_keys(str(artista))
	time.sleep(3)

	try:
		openpopustat =browser.find_element_by_xpath("//*[@class='boxResults blockCenter']")
	except:
		pass
	if openpopustat.text == 'Nenhum resultado :(':
		browser.close()
		return '400'
	else:
		try:
			openpopustat =browser.find_element_by_xpath("//*[@class='itemArtist match']")
		except:
			openpopustat =browser.find_element_by_xpath("//*[@class='itemArtist']")

		openpopustat.click()
		time.sleep(5)
		url = browser.current_url
		browser.close()
		return url


def gettop15(artista):
	link = openartista(artista)
	link = '{}popularidade/'.format(link)
	#try:
	#	browser = webdriver.Chrome()
	#except:
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(link)
	openpopustat =browser.find_element_by_xpath("//*[@class='icon-busca']")
	xx = browser.find_element_by_tag_name('tbody')
	xx =xx.text.split('\n')
	dicio={}
	for i in xx:
	    kk = i.split(' ')
	    key = kk[0]
	    value = ' '.join(kk[1:-2])
	    if key =='16':
	    	print(dicio)
	    	return dicio
	    dicio[key]=value
	browser.close()
	print(dicio)
	return dicio

def getmusics(artista,limit):

	link = openartista(artista)
	limit = str(int(limit)+1)

	if link=='400':
		return {'erro':'Nenhum resultado :('}
	page = requests.get(link)
	soup = BeautifulSoup(page.text, 'html.parser')
	x = soup.find_all('span', {'class' : 'numMusic'})
	y = soup.find_all('a', {'class' : 'nameMusic'})

	diciomusic ={}
	for num,music in zip(x,y):
		if num.text == "{}.".format(limit):
			return diciomusic
		diciomusic[num.text]=music.text

	return diciomusic


def getletra(artista, musica):
	link = openartista(artista)
	if link=='400':
		return {'erro':'Nenhum resultado :('}
	#try:
	#	browser = webdriver.Chrome()
	#except:
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(link)
	x=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Jumento Celestino')))
	x.click()

	if str(browser.current_url) == str(link):
		return {'erro':'Nenhum resultado :('}

	time.sleep(5)
	openpopustat =browser.find_element_by_id('lyrics')

	dicio ={'letra':openpopustat.text}
	browser.close()
	return dicio
