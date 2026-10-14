import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills/informes-mantenimiento/scripts/comparar_metricas.py"
spec = importlib.util.spec_from_file_location("comparar_metricas", SCRIPT)
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)


class ComparacionesTest(unittest.TestCase):
    def comparar(self, actual, anterior, comparable=True):
        return modulo.comparar({"indicador": "Sesiones", "actual": actual, "anterior": anterior,
                                "comparable": comparable})

    def test_crecimiento_y_caida(self):
        self.assertEqual(self.comparar(1200, 1000)["variacion_porcentual"], "20.00")
        self.assertEqual(self.comparar(0, 1000)["variacion_porcentual"], "-100.00")

    def test_no_copiar_porcentaje_del_ejemplo(self):
        self.assertEqual(self.comparar(4021, 12733)["variacion_porcentual"], "-68.42")

    def test_cero_no_es_base_porcentual(self):
        for actual in (0, 3):
            resultado = self.comparar(actual, 0)
            self.assertEqual(resultado["estado"], "sin_base_porcentual")
            self.assertIsNone(resultado["variacion_porcentual"])
            self.assertEqual(resultado["diferencia"], str(actual))

    def test_faltante_no_es_cero(self):
        for actual, anterior in ((None, 5), (5, None), (None, None)):
            resultado = self.comparar(actual, anterior)
            self.assertEqual(resultado["estado"], "sin_datos")
            self.assertIsNone(resultado["diferencia"])
            self.assertIsNone(resultado["variacion_porcentual"])

    def test_bases_incompatibles_no_producen_variacion(self):
        resultado = self.comparar(4021, 12733, False)
        self.assertEqual(resultado["estado"], "no_comparable")
        self.assertIsNone(resultado["diferencia"])
        self.assertIsNone(resultado["variacion_porcentual"])

    def test_precision_decimal(self):
        self.assertEqual(self.comparar("0.3", "0.1")["diferencia"], "0.2")
        self.assertEqual(self.comparar("0.3", "0.1")["variacion_porcentual"], "200.00")

    def test_rechaza_numeros_ambiguos_y_no_validos(self):
        for actual in (True, -1, "1.234,56", "NaN", "Infinity", [], {}):
            with self.subTest(actual=actual), self.assertRaises(ValueError):
                self.comparar(actual, 1)

    def test_comparabilidad_debe_ser_explicita(self):
        for valor in (None, "true", 1):
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                self.comparar(3, 2, valor)


if __name__ == "__main__":
    unittest.main()
