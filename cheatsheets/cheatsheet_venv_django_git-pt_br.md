### Ativando virtualenv
- Windows:  
`myvenv\Scripts\activate`
- OSX / Linux:   
`source myvenv/bin/activate`
(or `. myvenv/bin/activate`)

### Comandos para gerenciar Django
- Criando novas migrações:  
`python manage.py makemigrations blog`
- Aplicar migrações:  
`python manage.py migrate blog`
- Inicizalizar servidor web:  
`python manage.py runserver`
- Abrir console Python do Django:
`python manage.py shell`...
- ...e sair dele: `>>> exit()`


### Git
- Ver quais arquivos você alterou e o que foi adicionado no Git:  
`git status`  
- Adicionar um arquivo:  
`git add <arquivo>`
- Adicionar todos arquivos novos/modificados do diretório atual: 
`git add .`  
- Adicionar todos arquivos (novos/modificados e deletados) do diretório atual:
`git add -A .`  
- Salvar as alterações no histórico de commits do Git:
`git commit -m "mensagem"`  
