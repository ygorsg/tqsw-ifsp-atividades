import unittest
import numeroromano as nr

class TestConversorRomano(unittest.TestCase):

    def test_converte_I(self):
        self.assertEqual(nr.converte('I'), 1, "Erro ao converter I")

    def test_converte_V(self):
        self.assertEqual(nr.converte('V'), 5, "Erro ao converter V")

    def test_converte_II(self):
        self.assertEqual(nr.converte('II'), 2, "Erro ao converter II")

    def test_converte_XXII(self):
        self.assertEqual(nr.converte('XXII'), 22, "Erro ao converter XXII")

    def test_converte_IX(self):
        self.assertEqual(nr.converte('IX'), 9, "Erro ao converter IX")

    def test_converte_XXIV(self):
        self.assertEqual(nr.converte('XXIV'), 24, "Erro ao converter XXIV")

if __name__ == '__main__':
    unittest.main()