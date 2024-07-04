import csv
from helper import *
from presentatie import *

totaal_inkomsten=0

inkomsten = {
    'Aarbeien-ijs-totaal':1000,
    'Vanille-ijs-totaal':2000,
    'Chocolade-ijs-totaal':1500,
    "Waterijsjes-totaal":750
    }

totaal_inkomsten=(som(inkomsten))

uit=presenteer(inkomsten,totaal_inkomsten)
for el in uit:
    print (el)

with open('boekhouding.csv', 'w',newline='') as csvfile:
     for key, value in inkomsten.items():
        writer = csv.writer(csvfile,delimiter=';')
     writer.writerow([key,value])
