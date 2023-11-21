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

# EXEMPLO DE JSON  `ENTREGA PARCIAL` :

```
[
  {
    "id": 1,
    "name": "Joao Silva",
    "email": "",
    "address": "Rua A, 123",
    "cep": "12345-678",
    "birthdate": "1990-01-01",
    "phone": "(53) 91234-5678"
  },
  {
    "id": 2,
    "name": "Maria Oliveira",
    "email": "",
    "address": "Rua B, 456",
    "cep": "98765-432",
    "birthdate": "1985-05-15",
    "phone": "(53) 99876-5432"
  },
  {
    "id": 3,
    "name": "Carlos Santos",
    "email": "",
    "address": "Rua C, 789",
    "cep": "54321-876",
    "birthdate": "1988-10-20",
    "phone": "(53) 91432-1876"
  },
  {
    "id": 4,
    "name": "Ana Souza",
    "email": "",
    "address": "Rua D, 101",
    "cep": "67890-123",
    "birthdate": "1992-03-30",
    "phone": "(53) 91789-0123"
  },
  {
    "id": 5,
    "name": "Luiz Pereira",
    "email": "",
    "address": "Rua E, 202",
    "cep": "23456-789",
    "birthdate": "1982-12-05",
    "phone": "(53) 92345-6789"
  }
]

```
# SOBRE A API `ENTREGA FINAL` :

**Requisitos:**

- Python 3.8 ou superior, `recomendado: Python 3.11.`)
- Ambiente Virtual (por exemplo, `venv` ou `virtualenv`)
- Poetry (para gerenciamento de dependências)

**Instruções de Execução:**

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/andersonlimacrv/ProjetoIntegrador4B
   cd ProjetoIntegrador4B
   ```

2. **Crie e Ative o Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Instale as Dependências usando Poetry:**
   ```bash
   poetry install
   ```

4. **Estrutura do projeto:**

O projeto teve ideia de modularização, tentando seguir os principios de SOLID, e usando a arquitetura MVC, que consiste em model view e controller, porém, como é uma aplicação apenas backend, ficou separado em MODEL, CONTROLLER e rotas.
Separado rotas de controller para facilidade na manutenção futura.

O projeto segue a seguinte estrutura de diretórios:

```
├───app
│   ├─── controller
│   │      └─── clients.py
│   ├─── model
│   │      └─── clients.py
│   ├─── repository
│   │      └─── clients.json
│   ├───router
│   │      └─── clients.py
│   │      └─── home.py
│   ├─── service
│   └─── main.py
├─── migrations
└─── public
```

- **`app`:** Contém os módulos principais da aplicação.
  - **`Diretório controller`:** Responsável pela lógica de controle das rotas.
  - **` Diretório model`:** Define os modelos de dados da aplicação (schemas).
  - **`Diretório repository`:** Armazena arquivos, como o `clients.json`.
  - **`Diretório router`:** Define apenas as rotas da api separados por `slug`.
  - **`Diretório service`:** Fornece serviços adicionais, se necessário.
  - **`arquivo main.py`**: onde roda de fato nossa aplicação. 

- **`migrations`:** Diretório para possíveis migrações de banco de dados, nesse caso não temos pois não temos banco de dados..

- **`public`:** Pode conter recursos públicos acessíveis pela aplicação.

**Configuração:**

O arquivo de configuração, `clients.json`, é armazenado no diretório `repository`. Este arquivo contém os dados dos clientes e é onde as informações são persistidas entre execuções da aplicação.

Certifique-se de verificar e, se necessário, modificar as configurações no arquivo `clients.json` conforme necessário para atender aos requisitos específicos do seu projeto.

5. **Execute a Aplicação:**
   ```bash
   poetry run start
   ```

6. **Acesse no Navegador:**
   - Abra o navegador e vá para [http://localhost:8888](http://localhost:8888)

**Documentação:**

- A documentação da API está disponível em [http://localhost:8888/docs](http://localhost:8888/docs).
- Para explorar a especificação OpenAPI, acesse [http://localhost:8888/openapi.json](http://localhost:8888/openapi.json).


# API, REST e RESTFUL

## O que é API? REST e RESTful?

**API (Application Programming Interface):**
Uma API é um conjunto de rotinas e padrões estabelecidos por uma aplicação para permitir que outras aplicações utilizem suas funcionalidades. Funciona como um intermediário que facilita a comunicação entre diferentes serviços e serve como um meio de campo entre tecnologias diversas.

- Estabelece a comunicação entre diferentes serviços.
- Funciona como intermediador na troca de informações entre aplicações.
- Age como meio de campo entre tecnologias diversas.

### REST

- **REST (Representational State Transfer):**
  - Acrônimo para Transferência de Estado Representativo.
  - Envolve a transferência simbólica, figurativa e didática de dados, geralmente usando o protocolo HTTP.

- **Resources:**
  - Representa uma entidade ou objeto manipulado através da API.
  - Em uma aplicação de blog, um recurso pode ser um artigo. Cada artigo é uma entidade manipulada pela API.

**6 NECESSIDADES (Constraints) para ser RESTful:**

1. **Uniform Interface:**
   - Mantém constância e padrão na construção da interface.
   - Uso correto dos verbos HTTP, endpoints coerentes (preferencialmente no plural), linguagem única de comunicação (json), e envio consistente de respostas aos clientes são exemplos de aplicação de uma interface uniforme.
`Exemplo:` Uso consistente dos verbos HTTP (GET, POST, PUT, DELETE) para operações específicas em recursos.

2. **Client-server:**
   - Separação clara entre o cliente e o armazenamento de dados no servidor, promovendo a portabilidade do sistema.

3. **Stateless:**
   - Cada requisição do cliente deve conter todas as informações necessárias para que o servidor entenda e responda. O servidor não mantém estado entre requisições.
   - O servidor não mantém o estado entre requisições. Se um usuário faz login, a informação de autenticação deve ser incluída em cada requisição subsequente.

4. **Cacheable:**
   - As respostas para uma requisição devem indicar explicitamente se podem ou não ser cacheadas pelo cliente, melhorando a eficiência e reduzindo a carga no servidor.
   - Por exemplo, um recurso estático como uma imagem pode ser cacheado para reduzir a carga no servidor.

5. **Layered System:**
   - O cliente acessa um endpoint sem precisar conhecer a complexidade interna do servidor. O sistema é organizado em camadas para facilitar a manutenção e escalabilidade.
   - Exemplo: O cliente acessa um endpoint sem precisar conhecer a complexidade interna do servidor. O servidor pode ter várias camadas, como uma camada de banco de dados, sem afetar a interação do cliente.

6. **Code on Demand (Optional):**
   - Oferece a opção da aplicação baixar e executar código no cliente (algum script), proporcionando flexibilidade.

### RESTful

- **RESTful:**
  - Aplicação prática dos princípios REST.

**BOAS PRÁTICAS:**
- Utilizar verbos HTTP apropriados para requisições.
- Escolher entre plural ou singular para os endpoints, mantendo consistência.
- Evitar barras no final do endpoint.
- Sempre fornecer resposta ao cliente.

**VERBOS HTTP:**
- **GET:** Receber dados de um Resource.
- **POST:** Enviar dados ou informações para serem processados por um Resource.
- **PUT:** Atualizar dados de um Resource.
- **DELETE:** Deletar um Resource.
- **PATCH:** Atualizar parcialmente dados de um Resource.

**STATUS DAS RESPOSTAS:**
- **1xx:** Informação.
- **2xx:** Sucesso (200: OK, 201: CREATED, 204: No Content para PUT, POST, DELETE).
  - `200`: OK
  - `201`: CREATED
  - `204`: Não tem conteúdo PUT POST DELETE
- **3xx:** Redirecionamento.
- **4xx:** Erro do Cliente (400: Bad Request, 404: Not Found).
  - `400`: Bad Request
  - `404`: Not Found
- **5xx:** Erro do Servidor (500: Internal Server Error).
  - `500`: Internal Server Error 



