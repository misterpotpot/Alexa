# -*- coding: utf8 -*-

import urllib2
import time

def load(file):
	fichier = open(file, "r")
	contenu = fichier.read()
	fichier.close()
	output = contenu.split("\n")
	print "Fichier chargé\n"
	return output

def querry(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request, timeout=5)
	body = response.read()
	return body

def scrap(body, to_find, debut, fin):
	position_debut = body.find(to_find, 0) + debut
	position_fin = position_debut + fin
	output = body[position_debut:position_fin]
	output = output.replace('\n','#')
	output = output.replace('"','#')
	return output

def is_ecommerce(body):
	if body.find("panier", 0) > 1:
		return 'oui'
	return 'non'


while 1:
	print "\n\n************************"
	print "* Crawling - Alexa *"
	print "************************"
	print "\nChoisissez un mode :\n'alexa'		=> Crawl le rank alexa et le pays principal\n'direct'	=> Crawl la langue et si le site est marchand\n'quit'		=> Quitter le programme"
	mode = raw_input()

	if mode == "alexa":
		nom_domaine = load("input.txt")
		for i in nom_domaine:
			url = "http://www.alexa.com/siteinfo/" + i
			try:
				body = querry(url)
				try:
					rank = scrap(body, """strong class="metrics-data align-vmiddle">""", 134, 10)
					rank = rank.replace(',','') 
					rank = rank.replace(' ','')
					if rank == "<spanstyl":
						rank = "NA"
					pays = scrap(body, """<a href='/topsites/countries/""", 29, 2)
				except:
					print i + " #Erreur=2"
				print i + " " + rank + " " + pays
			except:
				print i + " #Erreur=1"

	elif mode == "direct":
		nom_domaine = load("input.txt")
		for i in nom_domaine:
			url = "http://" + i
			try:
				body = querry(url)
				try:
					pays = scrap(body, "lang=", 6, 2)
				except:
					pays = "NA"
				ecommerce = is_ecommerce(body)
				print i + " " + pays + " " + ecommerce
			except:
				print i + " #Erreur=1"

	elif mode == "quit":
		break

	else:
		print "\n\nErreur, ce mode n'est pas reconnu. Reessayez !"
