# - coding: utf-8 --
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

import bs4
from bs4 import BeautifulSoup
import requests
import pdb

def openartista(artista):
	link = 'https://www.vagalume.com.br/'
	browser = webdriver.Chrome()
	browser.get(link)
	openpopustat =browser.find_element_by_xpath("//*[@class='icon-busca']")
	openpopustat.click()
	time.sleep(3)
	openpopustat =browser.find_element_by_xpath("//*[@class='searchField']")
	#openpopustat.clear()
	openpopustat.send_keys(str(artista))
	time.sleep(3)
	#openpopustat.click()

	#pdb.set_trace()

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
	
	

	if link=='400':
		#print('erro')
		return {'erro':'Nenhum resultado :('}


	page = requests.get(link)
	soup = BeautifulSoup(page.text, 'html.parser')
	x = soup.find_all('span', {'class' : 'numMusic'})
	y = soup.find_all('a', {'class' : 'nameMusic'})

	diciomusic ={}
	for num,music in zip(x,y):
		if num.text == "16.":
			return diciomusic
		diciomusic[num.text]=music.text

	#print(diciomusic)
	return diciomusic


#gettop15('mamonas')
#gettop15('ramones')
#gettop15('easde')
#gettop15('guns')