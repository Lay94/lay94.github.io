# Descarga y limpia la base de datos de Enfermedades Transmitidas por Vectores (Dengue)
# Uso: bash bd_dengue.sh

handle_error() {
    echo "--La descarga de la base de datos falló, por favor, vuelva a intentarlo--"
    exit 1
}

trap 'handle_error $LINENO $?' ERR

rm -f *.csv #Eliminando bd para ser actulizada
curl -L -O https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/etv/datos_abiertos_dengue.zip #Descargando bd
unzip -q *.zip #Descomprimiendo el archivo
mv *.csv dengue_data.csv #Renombrando el archivo
rm -f *.zip #Eliminando comprimido

echo "**** La base de datos fue actualizada con éxito ****"
