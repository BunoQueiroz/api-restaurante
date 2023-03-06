# API Restaurante
![em desenvolvimento](https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-brightgreen)

# 🔨Ferramentas Utilizadas
* Django 4.1.7
* Django Rest Framework 3.14.0

# Funcionalidades
* Disponibilizar TODOS os recursos dos clientes

# Para Utilizar o projeto em seu PC realize os seguintes passos:


Crie uma pasta pasta:
```
mkdir my-project
```
E entre nela, assim:
```
cd my-project
```

No seu terminal (de preferencia o *git bash*) digite:
``` 
git clone https://github.com/BunoQueiroz/api-restaurante.git .
```

E em seguida, crie um ambiente virtual:

```
python -m venv venv
```

Ative o ambiente:

* COMANDO WINDOWS
```
venv/Scripts/activate
```

* COMANDO LINUX / MAC

```
source venv/bin/activate
```

Atualize o PIP (Recomendação):

```
python -m pip install --upgrade pip
```

Instale os recursos necessários:

```
python -m pip install -r requirements.txt
```

*Por fim crie, na raiz do seu projeto, um arquivo .env e defina dentro dele suas variáveis de ambiente.*

Para realizar as migrações necessárias em seu banco de dados, rode o comando:

```
python manage.py migrate
```

Depois de tudo isso, rode o comando:

```
python manage.py runserver
```
E seja feliz ; )

*Dúvidas ou erros fale diretamente comigo, boa sorte com tudo*
