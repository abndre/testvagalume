# - coding: utf-8 --
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

import time
import requests

import os

#options = ChromeOptions()
#options.binary_location = "/app/.apt/usr/bin/google-chrome-stable"


from bs4 import BeautifulSoup


'''
este metodo apenas abre a pagina do artista para
ser feito obtido as musicas e letras

todas as outras funcoes a chamam
'''
def openartista(artista):
	link = 'https://www.vagalume.com.br/'
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(link)

	#clica no icone de busca
	openpopustat =browser.find_element_by_xpath("//*[@class='icon-busca']")
	openpopustat.click()
	time.sleep(3)

	#no campo de busca imputa o nome do artista
	openpopustat =browser.find_element_by_xpath("//*[@class='searchField']")
	openpopustat.send_keys(str(artista))
	time.sleep(3)


	# TODO organizar estas excecoes
	try:
		#Procurando se o artista foi encontrado
		openpopustat =browser.find_element_by_xpath("//*[@class='boxResults blockCenter']")
	except:
		pass
	if openpopustat.text == 'Nenhum resultado :(':
		browser.close()
		return '400', browser
	else:
		#ao se digitar na caixa de texto, sempre se e escolhido o primeiro artista
		try:
			#em alguns casos aparece este match
			openpopustat =browser.find_element_by_xpath("//*[@class='itemArtist match']")
		except:
			#procurando o primeiro artista da lista apresentada
			openpopustat =browser.find_element_by_xpath("//*[@class='itemArtist']")


		openpopustat.click()
		time.sleep(5)

		#aqui se obtem a url do artista selecionado
		url = browser.current_url
		#browser.close()
		# retorna a url para outros testes
		return url, browser

	# se chegar aqui deu algum erro
	return '400'

def gettop15(artista):
	#obtem a url do artista
	link, browser = openartista(artista)

	if link=='400':
		browser.quit()
		return {'erro':'Nenhum resultado :('}

	#abre a url da popularidade
	link = '{}popularidade/'.format(link)
	#browser = webdriver.Chrome(chrome_options=options)
	browser.get(link)
	time.sleep(5)


	# seleciona as top15
	openpopustat =browser.find_element_by_xpath("//*[@class='icon-busca']")
	xx = browser.find_element_by_tag_name('tbody')
	xx =xx.text.split('\n')
	dicio={}
	for i in xx:
		kk = i.split(' ')
		key = kk[0]
		value = ' '.join(kk[1:-2])
		# este if limita o numero para 15 musicas
		if key =='16':
			browser.quit()
			return dicio
		dicio[key]=value
	browser.quit()
	return dicio


def getmusics(artista,limit):

	link, browser = openartista(artista)
	limit = str(int(limit)+1)
	browser.quit()
	if link=='400':
		return {'erro':'Nenhum resultado :('}

	page = requests.get(link)
	soup = BeautifulSoup(page.text, 'html.parser')

	#seleciona da tabela de musica o numero e o texto da musica
	x = soup.find_all('span', {'class' : 'numMusic'})
	y = soup.find_all('a', {'class' : 'nameMusic'})

	#o valor limit parametro da classe limita a quantidade de musicas
	diciomusic ={}
	for num,music in zip(x,y):
		if num.text == "{}.".format(limit):
			return diciomusic
		diciomusic[num.text]=music.text

	return diciomusic


def getletra(artista, musica):
	link, browser = openartista(artista)

	if link=='400':
		browser.close()
		return {'erro':'Nenhum resultado :('}

	browser.get(link)

	#abre o lind onde se encontra a musica
	x=WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Jumento Celestino')))
	x.click()

	# esta selecao ocorre para o caso da musica nao ser encontrada
	if str(browser.current_url) == str(link):
		return {'erro':'Nenhum resultado :('}

	time.sleep(5)

	#encontra a tag da musica e retorna
	openpopustat =browser.find_element_by_id('lyrics')
	dicio ={'letra':openpopustat.text}
	browser.quit()
	return dicio
