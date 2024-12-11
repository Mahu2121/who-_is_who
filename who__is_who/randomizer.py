import reflex as rx
import pytest
import random
from diccionario_caracteristicas2 import diccionario

def randomizer():
    info_perso=diccionario()
    return random.choice(list(info_perso.keys()))

