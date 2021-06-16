# Instalacion de ambiente de desarrollo

Asegurate de tener pip3 & virtualenv instalados en python 3.9

```shell
brew install python@3.9
python3 -m pip install --upgrade pip
pip3 install virtualenv
```

Crea ambiente virtual utilizando `python 3.9`

```shell
virtualenv -p python3.9 venv
```

activa el ambiente

```shell
source venv/bin/activate
```
## Ejecutar Proyecto

Para correr el Backend primero se navega a la carpeta Backend, después de activado el virtual environment y se ejecuta el comando
 ```python manage.py runserver```

 Para correr el Frontend se navega a la carpeta Frontend y se ejecuta el comando ```npm start````

## Nota
No pude terminar la parte de los PR
Todo lo demás funciona