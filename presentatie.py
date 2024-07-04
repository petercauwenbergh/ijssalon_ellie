
def presenteer(dictionary_input,totaal):
    uitvoer=[]
    for k,v in dictionary_input.items():
       uitvoer.append (f'{k} : {v} euro')
    uitvoer.append("="*30  )
    uitvoer.append(f'Totaal : {totaal} euro')
    return uitvoer


        

