import pytest
from who__is_who.randomizer import diccionario
def hacer_random():
    personas={"Susan":0,"Claire":0,"David":0,"Anne":0,"Robert":0,"Anita":0,"Joe":0,"George":0,"Bill":0,"Alfred":0,"Max":0,"Tom":0,"Alex":0,"Sam":0,"Richard":0,"Paul":0,"Maria":0,"Frans":0,"Herman":0,"Bernard":0,"Phillip":0,"Eric":0,"Charles":0,"Peter":0,}
    contador=0
    while i < 30:

        resultado=random.choice(list(personas.keys()))
        personas[resultado] +=1
        contador+=1
    return print(resultado)

