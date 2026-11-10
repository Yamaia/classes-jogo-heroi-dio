import contextlib
import io
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from heroi import ATAQUES, Heroi  # noqa: E402

ESPERADOS = {
    "mago": "o mago atacou usando magia",
    "guerreiro": "o guerreiro atacou usando espada",
    "monge": "o monge atacou usando artes marciais",
    "ninja": "o ninja atacou usando shuriken",
}


class TestHeroi(unittest.TestCase):
    def test_propriedades(self):
        h = Heroi("Aragorn", 87, "Guerreiro")
        self.assertEqual(h.nome, "Aragorn")
        self.assertEqual(h.idade, 87)
        self.assertEqual(h.tipo, "guerreiro")

    def test_mensagem_de_ataque_por_tipo(self):
        for tipo, esperado in ESPERADOS.items():
            with self.subTest(tipo=tipo):
                self.assertEqual(self._atacar(Heroi("X", 20, tipo)), esperado)

    def _atacar(self, heroi):
        with contextlib.redirect_stdout(io.StringIO()):
            return heroi.atacar()

    def test_atacar_imprime_a_mensagem(self):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            Heroi("Gandalf", 300, "mago").atacar()
        self.assertEqual(saida.getvalue().strip(), "o mago atacou usando magia")

    def test_versao_por_tabela_igual_ao_if(self):
        for tipo in list(ATAQUES) + ["arqueiro"]:
            with self.subTest(tipo=tipo):
                h = Heroi("X", 20, tipo)
                self.assertEqual(h.descricao_ataque(), h.descricao_ataque_por_tabela())

    def test_tipo_desconhecido_usa_ataque_padrao(self):
        self.assertEqual(self._atacar(Heroi("Robin", 25, "arqueiro")),
                         "o arqueiro atacou usando um ataque básico")

    def test_tipo_ignora_maiusculas_e_espacos(self):
        self.assertEqual(self._atacar(Heroi("Hanzo", 30, "  NINJA ")),
                         "o ninja atacou usando shuriken")

    def test_entradas_invalidas(self):
        with self.assertRaises(ValueError):
            Heroi("", 20, "mago")
        with self.assertRaises(ValueError):
            Heroi("X", -1, "mago")

    def test_str_e_repr(self):
        h = Heroi("Lee", 22, "monge")
        self.assertEqual(str(h), "Lee (monge, 22 anos)")
        self.assertEqual(repr(h), "Heroi(nome='Lee', idade=22, tipo='monge')")


if __name__ == "__main__":
    unittest.main()
