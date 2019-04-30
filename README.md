# Flask + Docker: Backend stack
Backend stack preconfigurado utilizando como herramientas principales: Python, Flask, Docker, Docker Compose, Postgres, PgAdmin, Swagger.

El servicio principal del proyecto (**flask-app**) está configurado en base a la imagen de Docker: [tiangolo/uwsgi-nginx-flask](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/) y la estructura general del backend tiene como referencia al proyecto: [tiangolo/full-stack](https://github.com/tiangolo/full-stack).

## Prerrequisitos

<a href="https://docs.docker.com/v17.09/engine/installation/" target="_blank" title="Install Docker">Docker</a> y <a href="https://docs.docker.com/compose/install/" target="_blank" title="Install Docker Compose">Docker Compose</a> son esenciales para ejecutar el backend.

## Características

* Integración completa con **Docker**.
* Implementación de **Docker Compose** y optimización para desarrollo en local.
* **Python Flask App** con:
  * Autenticación con **JWT token**
  * **SQLAlchemy** como ORM
  * **Alembic** para migraciones en base de datos.
* **Postgres** como motor de base de datos, integrado con Flask.
* **PgAdmin** interfaz de usuario web para administrar la base de datos Postgres.
* **Swagger-UI** para documentación interactiva del API.
* **Despliegue a Producción** con servidor web de Python utilizando Nginx y uWSGI.

**Nota**: Antes de ejecutar cualquier comando de Docker Compose asegúrate de estar ubicado en el directorio principal del proyecto.

## Desarrollo en local en modo interactivo

* Actualiza tu archivo `hosts` local, modifica la IP `127.0.0.1` (tu `localhost`) a `dev.api.backend-stack.com`. El archivo `docker-compose.override.yml` utiliza ese dominio para desplegar la documentación en **Suagger-UI**.

```
127.0.0.1    dev.api.backend-stack.com
```

...eso hará que tu navegador ejecute la app en ese dominio de manera local.

* Inicia el stack con Docker Compose:

```bash
docker-compose up -d
```

* Inicia una sesión interactiva en el contenedor de **flask-app**, por defecto en local solo ejecuta un loop infinito que no hace nada:

```bash
docker-compose exec flask-app bash
```

**Nota**: Sólo en la primera ejecución del proyecto debes ejecutar:

```bash
alembic upgrade head
```

... esto es para crear las tablas de base de datos por defecto que tiene el proyecto.

* Por último ejecuta el servidor de flask con debugging local, solo es necesario invocar la variable de ambiente `RUN`:

```bash
$RUN
```

La App construida con Docker, deberá estar disponible para acceder y todos los cambios realizados al código serán tomados por el servicio de forma automática mientras la App esté en ejecución.

### Migrations

Similar como ejecutamos el servidor de flask en local, también podemos ejecutar migraciones con comandos de `alembic` dentro del servicio **flask-app**.

Asegúrate de crear una "revisión" cada vez que cambies los modelos de la base de datos y realizar un "upgrade" para actualizarlos. De lo contrario, su aplicación tendrá errores.

* Inicia una sesión interactiva en el contenedor de **flask-app**:

```bash
docker-compose exec flask-app bash
```

* Después de cambiar un modelo, crea una revisión dentro del contenedor, por ejemplo:

```bash
alembic revision --autogenerate -m "Add column last_name to User model"
```

* Haz commit al repositorio de git con los archivos generados en el directorio de alembic.

* Después de crear una revisión, ejecuta la migración en la base de datos:

```bash
alembic upgrade head
```

## Despliegue en producción con Rancher

**Prerrequisitos**

Servidor con Docker, Docker Compose, GIT y Rancher (Versión: `v1.6.21` para este ejemplo) correctamente instalados.

* Inicia clonando tu repositorio en el servidor con GIT.
* Construye las imágenes de los servicios del proyecto con Docker Compose:
```bash
docker-compose build
```
* 


* Actualiza tu archivo `hosts` local, modifica la IP `127.0.0.1` (tu `localhost`) a `dev.api.backend-stack.com`. El archivo `docker-compose.override.yml` utiliza ese dominio para desplegar la documentación en **Suagger-UI**.

```
127.0.0.1    dev.api.backend-stack.com
```

...eso hará que tu navegador ejecute la app en ese dominio de manera local.

* Inicia el stack con Docker Compose:

```bash
docker-compose up -d
```

* Inicia una sesión interactiva en el contenedor de **flask-app**, por defecto en local solo ejecuta un loop infinito que no hace nada:

```bash
docker-compose exec flask-app bash
```

## License

Este proyecto está licenciado bajo los términos de la licencia MIT.
