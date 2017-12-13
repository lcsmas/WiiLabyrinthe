#!/usr/bin/env python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import cwiid
import nunchuk
import servo
from grovepi import *
#from grovepi_rgb_lcd import *

#Initialisation de l'écran

#setText("WiiLabyrinthe")


def main() :
	wm = connexionWii()
	wm.rpt_mode = cwiid.RPT_NUNCHUK
	moteurs = servo.init()
	moteur_x = moteurs[0]
	moteur_y = moteurs[1]
	
	i = 0
	while i == 0:
		x = float(nunchuk.get_x(wm))
		y = float(nunchuk.get_y(wm))
		servo.coordonne_to_position_moteur_x(moteur_x,x)
		servo.coordonne_to_position_moteur_y(moteur_y,y)	
		#time.sleep(0.1)
	servo.stop()

def connexionWii():
	#setText("Appuyez sur les boutons 1 et 2")
	#time.sleep(6)
	#setText("de votre Wiimote")
	wm=cwiid.Wiimote()
	#setText("Wiimote         connectée !")
	wm.rumble=1
	time.sleep(3)
	wm.rumble=0
	#setText("Arrêt partie :  appuyez sur + ")
	return wm
	

main()

	

#def partie():
	#setText("Placez la bille en bas a gauche")
	#time.sleep(10)
	#setText("Pret ?")
	#time.sleep(3)
	#setText("Pour lancer la  partie :")
	#time.sleep(3)
	#setText("Appuyez sur le  bouton A !")
	#while wm.state['buttons']!=8: #on presse le bouton A
		#setText("Appuyez sur le bouton A !")
	#t0=time.time()
	#setText("Partie en cours !")
	#while wm.state['buttons']!=4096 and #condition d'arrêt du capteur de luminosité :

		##expliquez les différents situations du nunchuk par rapport aux moteurs




	#t=time.time()-t0
	#setText("Temps"+t)
	#if t<25:
		#setText("GAGNE !")
	#else:
		#setText("PERDU !")
	##le labyrinthe se remet en place
	#setText("Nouvelle partie ?")
	#time.sleep(4)
	#setText("Appuyez sur A")
	#time.sleep(4)
	#setText("Sinon, appuyez  sur +")
	#if wm.state['buttons']!=8:
		#partie()
	#else:
		#setText("WiiLabyrinthe")
