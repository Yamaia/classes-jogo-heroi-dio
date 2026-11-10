# 🗡️ Classes de um Jogo: Herói

Projeto do desafio da **DIO** que modela um herói de aventura com **Programação Orientada a Objetos**: uma classe genérica `Heroi` com nome, idade e tipo, e um método `atacar` que muda a descrição do ataque conforme o tipo.

Desenvolvido por Yamaia, desenvolvedor Python, como parte do meu portfólio no GitHub.

## 🎯 Objetivo

Criar uma classe genérica que represente um herói com as propriedades **nome**, **idade** e **tipo** (guerreiro, mago, monge, ninja) e um método `atacar` que exibe:

```
o {tipo} atacou usando {ataque}
```

| Tipo | Ataque |
|---|---|
| mago | magia |
| guerreiro | espada |
| monge | artes marciais |
| ninja | shuriken |

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **Variáveis** | `nome`, `idade`, `tipo`, `herois`, constantes `ATAQUES` e `ATAQUE_PADRAO` |
| **Operadores** | comparação (`==`, `<`), lógicos (`not`), f-strings |
| **Estruturas de decisão** | `if / elif / else` em `descricao_ataque` e nas validações |
| **Laços de repetição** | `while` (menu e validação de entrada) e `for` (batalha final) |
| **Funções** | `ler_inteiro`, `main` |
| **Classes e objetos** | classe `Heroi` (construtor, métodos, `__str__` e `__repr__`) e objetos criados a cada herói |

## ⚖️ Decisões de projeto

1. **Texto do ataque.** A tabela do enunciado mostra "(usou magia)", mas a mensagem final é "atacou usando magia". Por isso o `{ataque}` guarda só o nome do golpe (`magia`, `espada`...), evitando um "usando usou".
2. **Prefixo "o".** O modelo da mensagem é `o {tipo} atacou usando {ataque}`, então a saída começa com "o" (ex.: `o mago atacou usando magia`). Os exemplos do enunciado omitem o artigo, mas segui o modelo.
3. **Tipo padronizado.** O tipo é guardado em minúsculas e sem espaços extras, então `"  NINJA "` vira `"ninja"`.
4. **Tipo desconhecido.** Como a classe é *genérica*, um tipo fora da tabela (ex.: arqueiro) não gera erro: ataca com `um ataque básico`.
5. **Duas formas de decidir.** `descricao_ataque` usa `if/elif/else` (o conteúdo pedido no desafio) e `descricao_ataque_por_tabela` usa um dicionário, mais fácil de ampliar com novos tipos.
6. **`atacar` exibe e retorna.** O método imprime a mensagem (como o desafio pede) e também a devolve, o que facilita testar.

## 🗂️ Estrutura

```
classes-jogo-heroi-dio/
├── src/
│   └── heroi.py          # classe Heroi + menu interativo
├── tests/
│   └── test_heroi.py     # testes automatizados
├── .gitignore
└── README.md
```

## ▶️ Como executar

Requisito: Python 3.8+ (sem dependências externas).

```bash
git clone https://github.com/<seu-usuario>/classes-jogo-heroi-dio.git
cd classes-jogo-heroi-dio
python src/heroi.py
```

### Exemplo de uso

```
==================================================
   🗡️  CLASSES DE UM JOGO: HERÓIS  🗡️
==================================================
Tipos com ataque especial: mago, guerreiro, monge, ninja

Nome do herói: Gandalf
Idade: 300
Tipo (guerreiro, mago, monge, ninja): mago

Gandalf (mago, 300 anos) entrou na aventura!
o mago atacou usando magia

Criar outro herói? (s/n): n

--- Batalha final: todos atacam! ---
1. Gandalf: o mago atacou usando magia
```

### Usando a classe em outro código

```python
from heroi import Heroi

aragorn = Heroi("Aragorn", 87, "guerreiro")
aragorn.atacar()
# o guerreiro atacou usando espada
```

## ✅ Testes

```bash
python -m unittest discover -s tests -v
```

Cobrem os 4 tipos, a mensagem impressa, o tipo desconhecido, a padronização do tipo, as duas formas de decidir o ataque (devem dar o mesmo resultado), entradas inválidas e `__str__`/`__repr__`.

## 🔍 Como funciona

1. **`Heroi.__init__`** – valida nome e idade e guarda as propriedades (`nome`, `idade`, `tipo`).
2. **`descricao_ataque`** – `if/elif/else` que devolve o ataque do tipo.
3. **`descricao_ataque_por_tabela`** – consulta o dicionário `ATAQUES`, com `ATAQUE_PADRAO` como valor padrão.
4. **`atacar`** – monta a mensagem `o {tipo} atacou usando {ataque}`, imprime e retorna.
5. **`main`** – menu em `while` que cria vários heróis (objetos) e, no final, faz todos atacarem com um `for`.

## 🚀 Ideias de evolução

- Subclasses (`Mago`, `Guerreiro`, `Monge`, `Ninja`) com **herança e polimorfismo**
- Pontos de vida, dano e sistema de turnos
- Salvar e carregar heróis em JSON
- API com FastAPI e interface em React

## 📚 Aprendizados

- Diferença entre **classe** (molde) e **objeto** (instância)
- Encapsular dados e comportamento (`atacar`) no mesmo lugar
- Validar dados no construtor e testar com `unittest`

## 🔗 Referências

- [Desafio DIO](https://www.dio.me/)
- [Classes em Python](https://docs.python.org/3/tutorial/classes.html)
