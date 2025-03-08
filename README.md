
<p align="center">
  <img src="biblioteca/static/svgs/logo.svg" width="200" alt="Logo do Projeto">
</p>


Projeto acadêmico desenvolvido para comparar diferentes stacks em uma aplicação com **registro de usuários**, **autenticação** e **CRUD de livros**, utilizando **Django**, **PostgreSQL** e **Docker**.

## Tecnologias Utilizadas
- **Backend:** Django (Python)
- **Banco de Dados:** PostgreSQL
- **Containerização:** Docker + Docker Compose

## Pré-requisitos
- Docker e Docker Compose instalados
- Python 3.x

## Funcionalidades

### Autenticação de Usuários
- Cadastro com: Nome, E-mail, CPF e Senha
- Login usando CPF + Senha

### CRUD de Livros
- Cadastro de Livros
- Listagem de Livros
- Atualização de Livros
- Exclusão de Livros

## Relacionamento
Um **Usuário (1)** pode ter vários **Livros (N)**, e cada Livro pertence a apenas um Usuário.

## Banco de Dados

### Estrutura dos modelos:
- **Usuário**
  - Nome
  - CPF
  - E-mail
  - Senha

- **Livro**
  - Título
  - Autor
  - Gêneros
  - Páginas
  - Usuário (chave estrangeira)

## Autores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/CeciliaCarol">
        <img src="https://github.com/CeciliaCarol.png" width="100px;" alt="Foto do Usuário Cecilia Carolina"/><br>
        <sub><b>Cecilia Carolina</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Tuanno">
        <img src="https://github.com/Tuanno.png" width="100px;" alt="Foto do Usuário Tuanno"/><br>
        <sub><b>Tuanno</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Isabela-Alves">
        <img src="https://github.com/Isabela-Alves.png" width="100px;" alt="Foto do Usuário Isabela Alves"/><br>
        <sub><b>Isabela Alves</b></sub>
      </a>
    </td>
  </tr>
</table>
