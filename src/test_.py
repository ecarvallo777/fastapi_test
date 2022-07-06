import unittest

from main import get_patent, get_id

class TestID(unittest.TestCase):
    def test_not_int(self):
        #Ingresa id y devuelve la patente.
        id = 10.5
        
        with self.assertRaises(ValueError) as exc:
            get_patent(id)
        self.assertEqual(str(exc.exception), 'El identificador debe ser un número entero.')
        
        #self.assertIs(type(id), int)
    def test_not_domain(self):
        id = get_patent(28886999)
        assert(id <= 28886999)
        assert(id >= 0)
    