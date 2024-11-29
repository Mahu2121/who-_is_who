import reflex as rx
import pytest
from diccionario_caracteristicas import diccionario
import random


def randomizer(diccionario):

    return random.choice(list(diccionario.keys()))

info_perso=diccionario()
print(randomizer(info_perso))