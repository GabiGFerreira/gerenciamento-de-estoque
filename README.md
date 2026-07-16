# Sistema de Controle de Estoque

Este projeto consiste em um sistema simples de controle de estoque desenvolvido em Python. O programa é executado no terminal e permite visualizar os produtos cadastrados, registrar entradas e saídas de mercadorias e atualizar automaticamente a quantidade disponível em estoque.

## Sobre o projeto

Os produtos são armazenados em um **dicionário de dicionários**, onde cada produto possui informações sobre preço e quantidade. Essa estrutura foi escolhida por facilitar a organização dos dados e permitir acesso rápido às informações de cada item.

O sistema possui um menu interativo que permanece em execução até que o usuário escolha encerrar o programa.

## Funcionalidades

- Visualizar todos os produtos cadastrados.
- Registrar entrada de produtos no estoque.
- Registrar saída de produtos.
- Atualizar automaticamente a quantidade disponível.
- Impedir retirada de quantidade superior ao estoque.
- Informar quando um produto não é encontrado.
- Encerrar o programa mediante confirmação do usuário.

## Tecnologias utilizadas

- Python 3

## Estrutura do projeto

```
controle-estoque/
│
├── estoque.py
└── README.md
```

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/controle-estoque.git
```

2. Acesse a pasta do projeto:

```bash
cd controle-estoque
```

3. Execute o programa:

```bash
python estoque.py
```

## Exemplo de uso

```
Controle de Estoque

1 - Visualizar Estoque atual
2 - Registrar Entrada de Produto
3 - Registrar Saída de Produto
4 - Sair do Sistema

Escolha uma opção numérica: 1

Produto: celular
Preço: R$5000.00
Quantidade: 5

Produto: detergente
Preço: R$13.00
Quantidade: 50

Produto: brinco
Preço: R$100.00
Quantidade: 20
```

## Estrutura dos dados

O estoque é armazenado utilizando um dicionário de dicionários:

```python
estoque = {
    "celular": {
        "preco": 5000.00,
        "quantidade": 5
    },
    "detergente": {
        "preco": 13.00,
        "quantidade": 50
    }
}
```

Essa estrutura permite acessar facilmente as informações de cada produto, por exemplo:

```python
estoque["celular"]["quantidade"]
```

## Conceitos praticados

Este projeto foi desenvolvido para praticar conceitos fundamentais da linguagem Python, como:

- Dicionários e dicionários aninhados.
- Estruturas de repetição (`while`).
- Estruturas condicionais (`if`, `elif` e `else`).
- Entrada e saída de dados (`input()` e `print()`).
- Manipulação de valores armazenados em estruturas de dados.
- Validação básica de entradas do usuário.
