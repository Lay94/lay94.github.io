## Actividades del Curso Herramientas de Productividad para Ciencia de Datos

A través de este proyecto se podrá visualizar la información sobre los casos de dengue confirmados en México cuyos datos son obtenidos de la [dirección general de epidemiología](https://www.gob.mx/salud/documentos/datos-abiertos-152127). 

### ¿Qué puedo obtener? 🚀

Con este proyecto se obtienen dos funciones, una primera `bd_dengue.sh` para descargar y actualizar la base de datos a utilizar, y una segunda `casos_dengue.py` que genera y salva un gráfico interactivo en formato html. Este gráfico visualiza los casos confirmados por fechas y por clasificación en cuanto a la edad: Infante (< 12 años), Joven (<27 años), Adulto (<60 años) y Anciano (>=60 años)

### ¿Qué necesito? 🛠️

Se debe tener instalado previamente [Docker](https://www.docker.com/get-started/) y [Git Bash](https://carpentries.github.io/workshop-template/#shell). Si reside en algún país donde se limitan los servicios de [Docker Hub](https://hub.docker.com/) y no puede descargar las imágenes, le recomendamos [DockerImageSave](https://github.com/jadolg/DockerImageSave) para descargar `ubuntu`, necesaria para el proyecto.

### ¿Cómo lo ejecuto? ⚙️
**1.** Clonar el repositorio:
```
git clone https://github.com/Lay94/lay94.github.io
```
**2.** Ir a la carpeta clonada. En este caso:
```
cd lay94.github.io
```
**3.** Construir contenedor:
```
docker build -t dengue_mx .
```
**4.** Ejecutar el contenedor de docker:
```
docker run -it --name casos_dengue dengue_mx bash
```
**5.** Dentro del contenedor podremos encontrar tanto las funciones como los archivos que ellas generan:
* La base de datos actualizada `dengue_data.csv`
* El gráfico interactivo [`fig.html`](https://lay94.github.io/fig.html)

### Aquí un ejemplo del gráfico interactivo 🤓


<figure class="figure_container">
  <iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="fig.html" height="345" width="100%"></iframe>
</figure>

### Resultados 📊📝

A través del gráfico obtenido se pudo visualizar que desde inicio del año 2022 hasta el 1ero de marzo del mismo año, los casos confimados de dengue han ido en descenso y que en este periodo de tiempo, el grupo etario menos afectado por esta enfermedad son los ancianos.



---
⌨️ con ❤️ por [Elaine Grenot Castellano](https://github.com/Lay94/lay94.github.io) 😊
