import reflex as rx
import pytest
from who__is_who.diccionario_caracteristicas import diccionario
import random


def randomizer(diccionario):
    info_perso=diccionario()
    return random.choice(list(info_perso.keys()))


