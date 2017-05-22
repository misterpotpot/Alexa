# -*- coding: utf8 -*-

import urllib2

def querry(nom_domaine):
	url = "http://www.alexa.com/siteinfo/" + nom_domaine
	try:
		req = urllib2.urlopen(url)
		body = req.read()
		position_debut = body.find("""strong class="metrics-data align-vmiddle">""", 0) + 134
		position_fin = position_debut + 10
		output = body[position_debut:position_fin]
		if output == "<span styl":
			output = "NA"
		output = output.replace(',','') 
		output = output.replace(' ','')
	except:
		output = '#Erreur'
	return output

def querry_pays(nom_domaine):
    url = "http://www.alexa.com/siteinfo/" + nom_domaine
    try:
        req = urllib2.urlopen(url)
        body = req.read()
        position_debut = body.find("""<a href='/topsites/countries/""", 0) + 29
        position_fin = position_debut + 2
        output = body[position_debut:position_fin]
    except:
        output = '#Erreur'
    return output



while 1:
	print "\n\n************************"
	print "* Crawling - Alexa *"
	print "************************"
	print "\nChoisissez un mode :\n'ranking'\n'pays'\n'quit'       => Quitter le programme"
	mode = raw_input()

	if mode == "ranking":
		fichier = open("input.txt", "r")
		contenu = fichier.read()
		fichier.close()
		nom_domaine = contenu.split("\n")
		for i in nom_domaine:
			output = querry(i)
			print i + " " + output
                
	elif mode == "pays":
		fichier = open("input.txt", "r")
		contenu = fichier.read()
		fichier.close()
		nom_domaine = contenu.split("\n")
		print "Fichier chargé\n"
		for i in nom_domaine:
			output = querry_pays(i)
			print i + " " + output

	elif mode == "quit":
		break

	else:
		print "\n\nErreur, ce mode n'est pas reconnu. Reessayez !"
