import reflex as rx
import pytest

import random


def randomizer(diccionario):
    info_perso=diccionario()
    return random.choice(list(info_perso.keys()))


