# AlertMapUX

## Introducción

Aplicación para creación de avisos y alertas barriales con el fin de informar de distintas situaciones del estilo de lugares que necesitan reparaciones, lugares donde se inunda o lugares seguros en caso de inundación y por el estilo.

## Requisitos

- docker (<=20.10.14)
- docker-Compose (<=2.2.3)
- python3.10-venv

## Docker (producción)

Para poder correr el proyecto usando docker se utiliza docker compose.

Para levantar la aplicación en producción

```bash
# Este comando construye, (re)crea e inicia contenedores para el servicio 
# definido en docker-compose.yml. El contenedor es creado en modo detached (background) 
# para poder segir utilizando la terminal.
docker compose up -d

# Para ver el nombre de la imagen, el cual es el nombre del proyecto más el nombre del servicio.
docker images

# Para comprobar que se encuentra corriendo.
docker ps
```

> **Nota:** es probable que si no se realizaste la post 
> instlacion de Linux ([Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/))
> debas utilizar sudo al comienzo de cada uno de los comandos anteriores.



## Flask (desarrollo)

Alternativamente también pueden probar localmente la aplicación en desarrollo utilizando flask ejecutando los siguientes comandos

```bash
# Opcional pero recomendado, crear un entorno virtual.
python3 -m venv venv

# Acttivar el entorno virtual
. venv/bin/activate

# Instalar las dependencias a partir del archivo requirements.txt.
pip install -r requirements.txt

# Setear la variable de entorno para desarrollo, como alternativa se 
# puede agregar estas variables en una archivo .env.
export FLASK_ENV=development

# Correr la aplicación. Este comando no informará donde podemos 
# ingresar para poder ver la página en nuestro navegador en el valor 
# indicado por "Running on http:".
flask run
```

## Pythonanywhere

La aplicación a su vez se encuentra hosteada en el siguiente link **enlace de la página**.
