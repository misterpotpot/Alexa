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

def is_ecommerce(body):
	if body.find("panier", 0) > 1:
		return 'oui'
	return 'non'

def querry(url, to_find, debut, fin, ecommerce):
	request = urllib2.Request(url)
	try:
		response = urllib2.urlopen(request, timeout=5)
		body = response.read()
	except:
		return '#Erreur=1'
	try:
		position_debut = body.find(to_find, 0) + debut
		position_fin = position_debut + fin
		output = body[position_debut:position_fin]
		output = output.replace('\n','#')
	except:
		output = '#Erreur=2'
	if ecommerce == 1:
		output = output + ' ' + is_ecommerce(body)
	return output


while 1:
	print "\n\n************************"
	print "* Crawling - Alexa *"
	print "************************"
	print "\nChoisissez un mode :\n'ranking'\n'pays'\n'direct'\n'quit'       => Quitter le programme"
	mode = raw_input()

	if mode == "ranking":
		nom_domaine = load("input.txt")
		for i in nom_domaine:
			url = "http://www.alexa.com/siteinfo/" + i
			output = querry(url, """strong class="metrics-data align-vmiddle">""", 134, 10, 0)
			if output == "<span styl":
				output = "NA"
			output = output.replace(',','') 
			output = output.replace(' ','')
			print i + " " + output
                
	elif mode == "pays":
		nom_domaine = load("input.txt")
		for i in nom_domaine:
			url = "http://www.alexa.com/siteinfo/" + i
			output = querry(url, """<a href='/topsites/countries/""", 29, 2, 0)
			print i + " " + output

	elif mode == "direct":
		nom_domaine = load("input.txt")
		for i in nom_domaine:
			url = "http://" + i
			url2 = "http://www." + i
			output = querry(url, "lang=", 6, 2, 1)
			print i + " " + output

	elif mode == "quit":
		break

	else:
		print "\n\nErreur, ce mode n'est pas reconnu. Reessayez !"
