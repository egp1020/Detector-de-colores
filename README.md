# Paso a Paso: Ejecución del Programa

## Crear entorno virtual
Para crear un entorno virtual, debe posicionarse desde la terminal en el directorio dónde se encuentra el archivo requirements.txt.

Luego se procede a ejecutar el siguiente comando ```python -m venv venv```. Con esto se crea el entorno virtual llamado "venv".

Aunque se creó el entorno virtual, no está activado, para activarlo debemos ejecutar el siguiente comando ```. venv/Scripts/activate``` (note que hay un punto al principio de la instrucción), otro comando puede ser ```source venv/bin/activate```. Va notar un leve cambio en la terminal cuando el entorno virtual esté activo y es que encima o al principio del indicador de la dirección del directorio le aparecerá "venv".

## Instalar dependencias
Una vez tenga activo el entorno virtual, procedemos a instalar en este las librerías, para ello usamos el comando ```pip install -r requirements.txt```, al final debe decir "Successfully installed ..."

## Ejecución del archivo
Ahora, con el entorno virtual activo procedemos a ejecutar el programa con el comando ```python color_detector.py```. Se aclara que el comando funciona siempre y cuando se ejecute en el directorio donde se encuentra el archivo "color_detector.py"

## Detener programa
Presione ```ctrl + c``` para detener el programa.
