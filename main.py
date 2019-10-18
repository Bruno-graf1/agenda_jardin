#coding:utf-8
import os
import sys

def menu():
	os.system("cls")
	print("\t\t*********************************************")
	print("\t\t***************AGENDA JARDIN*****************")
	print("\t\t*********************************************")
	print("\n")
	print("\n")
	print("\n")
	print("\t\tLa prochaine Tache devra se réaliser le **/**/** ")
	print("\t\tEt cela devra etre : *****")
	print("\n")
	print("\n")
	print("\n")
	print("\t\tQue voulez faire ?")
	print("\t\tVoir toutes les taches : taper 1")
	print("\t\tQuitter : taper :2")

def voirTaches():
	print("vous avez tapr 1 ")
	print("voici toutes les taches")
	input("aller on revient au menu ?")
	

def choixDuMenu():
	choixMenu = int(input("votre choix :  "))
	if choixMenu == 1:
		voirTaches()
		return  1

	elif choixMenu == 2:
		quitter()
				

def quitter():
	print("Vous avez taper 2 ")
	input("salut")
	sys.exit()
	


choixMenu = 1
while choixMenu == 1 :
	menu()
	choixDuMenu()
	




