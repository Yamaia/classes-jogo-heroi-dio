"""Classes de um jogo: o Herói.

Conceitos aplicados: variáveis, operadores, laços de repetição,
estruturas de decisão, funções, classes e objetos.
"""

# Tabela de ataques por tipo (usada na versão orientada a dados).
ATAQUES = {
    "mago": "magia",
    "guerreiro": "espada",
    "monge": "artes marciais",
    "ninja": "shuriken",
}
ATAQUE_PADRAO = "um ataque básico"


class Heroi:
    """Classe genérica que representa um herói de uma aventura."""

    def __init__(self, nome: str, idade: int, tipo: str):
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome não pode ficar vazio.")
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")

        self.nome = nome
        self.idade = idade
        self.tipo = tipo.strip().lower()  # "Mago " e "mago" viram o mesmo tipo

    def descricao_ataque(self) -> str:
        """Retorna o ataque do herói usando estruturas de decisão (if/elif/else)."""
        if self.tipo == "mago":
            return "magia"
        elif self.tipo == "guerreiro":
            return "espada"
        elif self.tipo == "monge":
            return "artes marciais"
        elif self.tipo == "ninja":
            return "shuriken"
        else:
            return ATAQUE_PADRAO

    def descricao_ataque_por_tabela(self) -> str:
        """Versão alternativa: consulta o dicionário ATAQUES."""
        return ATAQUES.get(self.tipo, ATAQUE_PADRAO)

    def atacar(self) -> str:
        """Exibe e retorna a mensagem de ataque: 'o {tipo} atacou usando {ataque}'."""
        mensagem = f"o {self.tipo} atacou usando {self.descricao_ataque()}"
        print(mensagem)
        return mensagem

    def __str__(self) -> str:
        return f"{self.nome} ({self.tipo}, {self.idade} anos)"

    def __repr__(self) -> str:
        return f"Heroi(nome={self.nome!r}, idade={self.idade}, tipo={self.tipo!r})"


def ler_inteiro(mensagem: str) -> int:
    """Laço while que repete até o usuário digitar um inteiro não negativo."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit():
            return int(entrada)
        print("  ⚠️  Digite apenas números inteiros não negativos.")


def main() -> None:
    print("=" * 50)
    print("   🗡️  CLASSES DE UM JOGO: HERÓIS  🗡️")
    print("=" * 50)
    print("Tipos com ataque especial:", ", ".join(ATAQUES))

    herois = []  # lista de objetos Heroi

    while True:
        nome = input("\nNome do herói: ").strip()
        if not nome:
            print("  ⚠️  O nome não pode ficar vazio.")
            continue

        idade = ler_inteiro("Idade: ")
        tipo = input("Tipo (guerreiro, mago, monge, ninja): ").strip()

        heroi = Heroi(nome, idade, tipo)
        herois.append(heroi)

        print(f"\n{heroi} entrou na aventura!")
        heroi.atacar()

        if input("\nCriar outro herói? (s/n): ").strip().lower() != "s":
            break

    print("\n--- Batalha final: todos atacam! ---")
    for i, h in enumerate(herois, start=1):
        print(f"{i}. {h.nome}: ", end="")
        h.atacar()


if __name__ == "__main__":
    main()
