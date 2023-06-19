# Game Project

Para poder correr el juego debes realizar estas instrucciones:

```sh
cd game
pip3 install -r requirements.txt
python3 main.py
```

Linea 1 -> Nos permite movernos a la carpeta en la que se encuentra dicho proyecto. <br>
Linea 2 -> Nos permite instalar todas las dependecias que se necesitan en el proyecto. <br>
Linea 3 -> Ejecutamos el proyecto. <br>

# App Project

Para poder correr el proyecto debes realizar estas instrucciones:

```sh
git clone
cd app
python3 -m venv <NombreDelAmbiente>
source <NombreDelAmbiente>/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Linea 1 -> Clonar el proyecto. <br>
Linea 2 -> Nos permite movernos a la carpeta en la que se encuentra dicho proyecto. <br>
Linea 3 -> Creamos el entorno. <br>
Linea 4 -> Activamos el entorno. <br>
Linea 5 -> Nos permite instalar todas las dependecias que se necesitan en el proyecto. <br>
Linea 6 -> Ejecutamos el proyecto. <br>



# Nota recuerda crear tu propio entorno de desarrollo antes de instalar dependencias.

Verificar donde esta python y pip

```sh
which python3
which pip3
```

Si estas en linux o wsl debes instalar

```sh
sudo apt install -y python3-venv
```

Luego para cada proyecto lo ideal es que tenga su propio ambiente moviendonos a cada carpeta haciendo ```cd app``` por ejemplo:

```sh
python3 -m venv <NombreDelAmbiente>
```
Asegurate de cambiar "<NombreDelAmbiente>" por el nombre que le quieres poner a tu ambiente.

Despues debemos activar el ambiente:

```sh
source <NombreDelAmbiente>/bin/activate
```

Para salir del ambiente virtual usamos:

```sh
deactivate
```

Tambien es importante tener en cuenta que si al entorno no le ponemos como nombre ```env``` entonces debemos agregar ese nombre que pongamos al .gitignore para evitar que se cargue dicha carpeta en el github.