# Gerenciamento alunos

### Objetivo
Criar uma aplicação para o gerenciamento de alunos, utilizando o framework Django e MySQL.

### Descrição do sistema
O sistema consiste em um projeto Django onde há um app chamado "alunos". O aplicativo "alunos" contém o modelo de dados que define os campos: Nome, Curso, Data de nascimento, CPF, RG, Data de ingresso na instituição e foto do aluno.

O sistema utiliza Bootstrap para estilizar os templates HTML e oferecer uma interface amigável.

O sistema possui os seguintes componentes:

- `index.html`: Este é o template principal que é exibido quando o usuário acessa a página inicial. Ele fornece uma breve descrição do sistema e oferece um link para o formulário de cadastro de alunos.

- `cadastro_aluno.html`: O cadastro de novos alunos é realizado por meio de um modal, que é exibido quando o usuário clica no link de cadastro de alunos. O modal contém um formulário para inserção dos dados do aluno, incluindo nome, idade, curso, data de nascimento e foto. Quando o formulário é submetido, os dados são enviados para o servidor e cadastrados no banco de dados.

- `alunos_cadastrados.html`: Neste template, são exibidos os alunos cadastrados no sistema. O nome de cada aluno é exibido como um link. Quando o usuário clica no nome do aluno, é exibido um modal contendo a foto do aluno.

- `unauthorized.html`: Quando um usuário tenta acessar a rota "Aluno" sem permissão, é exibida uma página personalizada de "Não autorizado". Essa página informa ao usuário que ele não tem permissão para acessar a página solicitada.

Em resumo, o sistema permite o cadastro de novos alunos por meio de um modal e a exibição dos alunos cadastrados em uma página. O Bootstrap é utilizado para estilizar os templates e fornecer uma interface amigável. Além disso, quando um usuário não tem permissão para acessar a rota "Aluno", é exibida uma página personalizada informando a falta de autorização.

### Tecnologias utilizadas
- Python
- Django
- MySQL
- Jinja2 + Bootstrap

---

_Aplicação Django desenvolvida para a disciplina optativa de Desenvolvimento Web Avançado do curso Bacharelado em Sistemas de Informação do IFNMG Campus Januária._
