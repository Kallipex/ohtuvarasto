import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus_nollataan(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_nolla_tilavuus(self):
        varasto = Varasto(0, 5)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_negatiivinen_alku_saldo(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0.0)

    def test_suurempi_alku_saldo_kuin_tilavuus(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_taysi_varasto(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.lisaa_varastoon(1)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_enemman_kuin_saldo(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijono_tyhja(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_merkkijono_taynna(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")