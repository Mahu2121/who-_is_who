import reflex as rx

import pytest

import unittest
from who__is_who.estado import state


class TestAdivinar(unittest.TestCase):

    def setUp(self):
        
        self.state = state()

    def test_aleatorio(self):
        self.state.randomizer()
        self.assertIn(
            self.state.final,
            self.state.name_diccionarioo.keys(),
        )


