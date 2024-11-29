import reflex as rx
import pytest
from who__is_who.diccionario_caracteristicas import diccionario 
import random


def randomizer(personas):

    return random.choice(list(personas.keys()))


