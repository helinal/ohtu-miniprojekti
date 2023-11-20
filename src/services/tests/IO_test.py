import unittest
from unittest.mock import patch
from IO import KonsoliIO
from IO import UI


class TestKonsoliIO(unittest.TestCase):
    def setUp(self):
        self.konsoli_io = KonsoliIO()
        self.ui = UI()
