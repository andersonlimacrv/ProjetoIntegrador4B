# ProjetoIntegrador4B - PLANO DE EXECUÇÃO

## TEMA
Desenvolvimento de Sistema WEB utilizando REST

## OBJETIVOS
Realizar a implementação de uma API REST utilizando uma linguagem de programação para web.

## DESCRIÇÃO DAS ETAPAS DO PROJETO

### 1. PESQUISA
Tendo por base os conceitos explorados nas disciplinas de “Arquitetura de Sistemas” e “Integração de Aplicações”, os alunos irão sistematizar os conhecimentos e implementar uma API REST individualmente.

### 2. DESENVOLVIMENTO
Os alunos, em conjunto com o professor, desenvolverão uma API REST com rotas GET, POST, PUT, DELETE, interagindo com o CRUD utilizando a linguagem escolhida. A API será simulada através de um arquivo .json.

### 3. ENTREGA PARCIAL
Entrega parcial online (Plataforma A): De 13/11 até 20/11 às 23:59h
- Arquivo clientes.json (padrão json) com informações de 5 clientes:
  - cliente_id
  - nome
  - endereço
  - cep
  - data de nascimento
  - telefone
- Código devidamente comentado.

### 4. ENTREGA FINAL
Entrega final online (Plataforma A): De 04/12 até 09/12 às 23:59h
- Implementação da API REST.
- Arquivo clientes.json.
- Configuração das rotas.
- Apresentação oral e slides das atividades desenvolvidas.

## CRITÉRIO DE AVALIAÇÃO: ENTREGA PARCIAL

| Critérios                                 | Peso | Nota | 
|-------------------------------------------|------|------|
| Descrição correta dos campos do Json       | 2    |      |
| Qualidade na documentação                 | 3    |      |
| Formato correto do Json                   | 5    |      | 

## CRITÉRIO DE AVALIAÇÃO - ENTREGA FINAL:

| Critérios                                 | Peso | Nota |
|-------------------------------------------|------|------|
| Implementação das rotas                   | 2    |      | 
| Qualidade de código                       | 3    |      | 
| Arquivo json corretamente estruturado     | 2    |      | 
| Apresentação oral e qualidade do relatório| 3    |      |

Obs: `Entrega apenas via Plataforma A.`

## REFERÊNCIAS
- MILETTO, E.M.; BERTAGNOLLI, S.C. Desenvolvimento de Software II: Introdução ao desenvolvimento web com HTML, CSS, JavaScript e PHP. Porto Alegre: Bookman, 2014.
- ROBSON, E.; FREEMAN, E. Use a cabeça! HTML e CSS. Alta Books, 2ª edição, 2015.
- HERRINGTON, J.D. PHP Hacks: Dicas e ferramentas para criação de web sites dinâmicos. Porto Alegre: Bookman, 2007.
- ADAMS, C.; BOLTON, J.; JOHNSON, D.; SMITH, S.; SNOOK, J. A arte e a ciência da CSS: crie web designs inspiradores baseados em padrões. Porto Alegre: Bookman, 2009.
- FLANAGAN, David. Javascript: o guia definitivo. Porto Alegre: Bookman, 6ª edição, 2013.

# EXEMPLO DE JSON:

```
[
  {
    "cliente_id": 1,
    "nome": "Cliente 1",
    "endereço": "Rua A, 123",
    "cep": "12345-678",
    "data_de_nascimento": "1990-01-01",
    "telefone": "(00) 1234-5678"
  },
  {
    "cliente_id": 2,
    "nome": "Cliente 2",
    "endereço": "Rua B, 456",
    "cep": "98765-432",
    "data_de_nascimento": "1985-05-15",
    "telefone": "(00) 9876-5432"
  },
  {
    "cliente_id": 3,
    "nome": "Cliente 3",
    "endereço": "Rua C, 789",
    "cep": "54321-876",
    "data_de_nascimento": "1988-10-20",
    "telefone": "(00) 5432-1876"
  },
  {
    "cliente_id": 4,
    "nome": "Cliente 4",
    "endereço": "Rua D, 101",
    "cep": "67890-123",
    "data_de_nascimento": "1992-03-30",
    "telefone": "(00) 6789-0123"
  },
  {
    "cliente_id": 5,
    "nome": "Cliente 5",
    "endereço": "Rua E, 202",
    "cep": "23456-789",
    "data_de_nascimento": "1982-12-05",
    "telefone": "(00) 2345-6789"
  }
]
```

JSON melhor tratado. Sugestão:

```
[
  {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "name": "Cliente Anônimo",
    "address": {
      "street": "Rua Anônima",
      "number": 0,
      "city": "Cidade Anônima",
      "cep": "00000-000",
      "state": "XX",
      "country": "AN"
    },
    "birthdate": "01/01/2000",
    "phone_number": "00000000000"
  }
]
```

JSON com mais campos e exemplo de utilização:
```
[
  {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "name": "Cliente Anônimo",
    "contact": {
      "email": "cliente.anonimo@example.com",
      "phone_number": "+00 (0)123 456 7890"
    },
    "address": {
      "street": "Rua Anônima",
      "number": 0,
      "city": "Cidade Anônima",
      "cep": "00000-000",
      "state": "XX",
      "country": "AN"
    },
    "birthdate": "01/01/2000",
    "registration_date": "01/01/2022",
    "last_access": {
      "date": "01/01/2023",
      "location": "Página Inicial",
      "device": "Computador"
    },
    "products_purchased": [
      {
        "product_id": "p1",
        "product_name": "Produto 1",
        "price": 19.99
      },
      {
        "product_id": "p2",
        "product_name": "Produto 2",
        "price": 29.99
      }
    ]
  }
]


```


