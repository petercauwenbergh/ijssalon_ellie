from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    kortingprijs=prijs*korting
    uitvoer=(f"Vandaag in de aanbieding: emmertje ijs  (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingprijs} euro.")
    return uitvoer
def inkomsten_totaal(inkomsten,btw):
    uitvoer = 0
    for i in inkomsten:
        uitvoer +=i
    btwbedrag=round(uitvoer*btw,2)
    return (f'Het totaal van de inkomsten van deze week is {uitvoer} euro, waarover {btwbedrag} euro BTW betaald dient te worden.')

def laag_en_hoog(mijn_lijst):
    uitvoer = (min(mijn_lijst),max(mijn_lijst))
    return(uitvoer)

def gemiddelde(mijn_lijst):
    uitvoer=round(sum(mijn_lijst)/len(mijn_lijst))
    return(f'De gemiddelde inkomsten van deze week zijn {uitvoer} euro.')

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst =  laag_en_hoog(invoer_lijst_2)
    return(mijn_functie_2(korte_lijst[0],korte_lijst[1]))

