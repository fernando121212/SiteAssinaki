# Criar a conta no heroku

Antes de começar execute o comando abaixo
```sh
pip install -U pip django gunicorn django-heroku pillow
```

Caso a instalação seja no Windows, utilize o seguinte comando
```cmd
py -m pip install --upgrade pip django gunicorn django-heroku --user
```
Em seguida, crie ou atualize o seu arquivo ```requerimentes.txt```
```sh
 pip freeze > ./requeriments.txt
```
Para autualizar a partir do arquivo ```requerimentes.txt```
```sh
 pip freeze -r ./requeriments.txt
 ```

Agora você precisa ter acesso ao e-mail e seguir os passoa abaixo.

* login: assinaki@hotmail.com
* senha: [ver no rascunho do e-mail](https://outlook.live.com/mail/compose/AQMkADAwATY0MDABLWZiNTQtODdkNS0wMAItMDAKAEYAAANggYPBfJK2SIkCcBRhb8fiBwAfPRAIKmGyT44q9cSc8%2BIfAAACAQ8AAAAfPRAIKmGyT44q9cSc8%2BIfAAABWHIhAAAA)

* requisitos:

    * git

    * python3
    * [windows 64: instalar o cli](https://cli-assets.heroku.com/heroku-x64.exe)
    * [windows 32: instalar o cli](https://cli-assets.heroku.com/heroku-x86.exe)
    
Depois de instalar, digite no terminal da app, na ide, o comando do heroku:

```sh
    heroku login
    heroku: Press any key to open up the browser to login or q to exit:
```

ou

```sh
    heroku login --interactive
    Enter your Heroku credentials.
    Email: assinaki@hotmail.com
    Password: 
```

Para obter mais informações acesse o [devcenter](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

***
Execute com o comando abaixo para prepara o servdidor para receber a app

```sh
heroku create
sudo heroku git:remote -a protected-waters-56490
```
Para fazer o ```deploy``` digite no terminal:
```sh
git add .
git commit -m "deploy de teste"
git push heroku master
```

O app está online com o nome [assinaki](https://assinaki.herokuapp.com/). Contudo não é possível ver nada enquanto o app estiver no modo debug e sem métodos.



