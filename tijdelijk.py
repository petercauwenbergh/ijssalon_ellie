prijzen={
    'aardbei'   :'3',
    'vanille'   :'4',
    'chocolade' :'5'
}
aanbieding=(int(prijzen['aardbei'])*0.8)
print (aanbieding)

'''
ik heb dit met 'int' opgelost, want anders kreeg ik steeds onderstaande foutmelding:
        aanbieding=((prijzen['aardbei'])*0.8)
                ~~~~~~~~~~~~~~~~~~~~^~~~
        TypeError: can't multiply sequence by non-int of type 'float' 
'''

reclame_tekst =  (f'Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}')
reclame_tekst2 = reclame_tekst[:61]
reclame_tekst3 = (reclame_tekst2).upper()
reclame_tekst4 = reclame_tekst3.split ()

print ()
for el in reclame_tekst4:
    if len(el) > 5:
        print (el.lower())
