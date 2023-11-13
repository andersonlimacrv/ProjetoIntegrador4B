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

Este material fornece uma compreensão abrangente de API, REST e RESTful, destacando tanto os conceitos fundamentais quanto as práticas recomendadas.
