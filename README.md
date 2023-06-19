# Game Project

Para poder correr el juego debes realizar estas instrucciones:

```sh
cd game
pip3 install -r requirements.txt
python3 main.py
```

Linea 1 -> Nos permite movernos a la carpeta en la que se encuentra dicho proyecto.
Linea 2 -> Nos permite instalar todas las dependecias que se necesitan en el proyecto.
Linea 3 -> Ejecutamos el proyecto.

# App Project

Para poder correr el proyecto debes realizar estas instrucciones:

```sh
cd app
pip3 install -r requirements.txt
python3 main.py
```

Linea 1 -> Nos permite movernos a la carpeta en la que se encuentra dicho proyecto.
Linea 2 -> Nos permite instalar todas las dependecias que se necesitan en el proyecto.
Linea 3 -> Ejecutamos el proyecto.



# Nota recuerda crear tu propio entorno de desarrollo antes de instalar dependencias.

####Verificar donde esta python y pip

```sh
which python3
which pip3
```

####Si estas en linux o wsl debes instalar

```sh
sudo apt install -y python3-venv
```

####Luego para cada proyecto lo ideal es que tenga su propio ambiente moviendonos a cada carpeta haciendo ```sh cd app``` por ejemplo:

```sh
python3 -m venv <NombreDelAmbiente>
```
Asegurate de cambiar "<NombreDelAmbiente>" por el nombre que le quieres poner a tu ambiente.

####Despues debemos activar el ambiente:

```sh
source "<NombreDelAmbiente>"/bin/activate
```

####Para salir del ambiente virtual usamos:

```sh
deactivate
```