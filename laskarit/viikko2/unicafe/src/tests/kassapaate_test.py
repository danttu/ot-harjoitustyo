import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_molemmilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260), 20)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(230), 230)

    def test_korttiosto_toimii_molemmilla(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamäärä_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

        self.assertIsNone(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1))
        