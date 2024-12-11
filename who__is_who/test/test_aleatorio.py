import reflex as rx
import unittest
from who__is_who.estado import state
import pytest

class TestAdivinar(unittest.TestCase):

    def setUp(self):
        
        self.state = state()

    def aleatorio(self):
        self.state.randomizer()
        self.assertIn(
            self.state.final,
            self.state.name_diccionarioo.keys(),
        )