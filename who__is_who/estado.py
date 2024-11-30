import reflex as rx
import pytest
from who__is_who.diccionario_caracteristicas import diccionario
from who__is_who.randomizer import randomizer
import random


class State(rx.State):
    


    def randomizer(self):
        info_perso=diccionario()
        random.choice(list(info_perso.keys()))
