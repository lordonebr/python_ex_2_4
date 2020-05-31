POS graduação

Curso: Desenvolvimento Web Full Stack

Disciplina: Frameworks back end: Python

Professor: Matheus Alcântara Souza

Exercício 2 e 4

Aluno: André Guilherme de Almeida Santos

### Comandos básicos

- COMANDO para criar a migração
```
  python manage.py makemigrations people
```  

- COMANDO para executar a migração:
```
  python manage.py migrate people
```  

- COMANDO para subir o servidor na porta 8000:
```
  python manage.py runserver
```  

### Rotas
* Página inicial:
```
  http://localhost:8000/people/
```    

* Página cadastrar usuário:
```
  http://localhost:8000/people/cadastro/
```  

* Página listar usuários:
```
  http://localhost:8000/people/listar/
```  

* Página detalhar um usuário:
```
  http://localhost:8000/people/detalhar/{id}/
```  
    Exemplo para recuperar o usuário de id = 1:  
    http://localhost:8000/people/detalhar/1/
    
* Página editar um usuário:
```
  http://localhost:8000/people/edicao/{id}/
```  
    Exemplo para editar o usuário de id = 1:  
    http://localhost:8000/people/edicao/1/  
    

### Rotas utilizando POST (chamadas pelos templates das rotas acima):
* Cadastrar novo usuário:
```
  POST http://localhost:8000/people/cadastrar/
```       

* Editar um usuário:
```
  POST http://localhost:8000/people/editar/{id}/
```  
    Exemplo para editar o usuário de id = 1:  
    POST http://localhost:8000/people/editar/1/   

* Exclusão de um usuário:
```
  POST http://localhost:8000/people/excluir/{id}/
```  
    Exemplo para excluir o usuário de id = 1:  
    POST http://localhost:8000/people/excluir/1/         
