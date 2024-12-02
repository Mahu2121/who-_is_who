import reflex as rx
import pytest
from diccionario_caracteristicas import diccionario
import random


def randomizer(diccionario):
    info_perso=diccionario()
    return random.choice(list(info_perso.keys()))


print(randomizer(diccionario))