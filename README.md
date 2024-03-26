# Extractor de Definiciones de la RAE

Este script en Python permite extraer las definiciones de palabras desde el Diccionario de la Real Academia Española (RAE) y también muestra la definición de la "palabra del día".

## Requisitos

- Python 3.x
- BeautifulSoup
- requests

## Instalación

1. Clona este repositorio o descarga el archivo ZIP.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala las dependencias utilizando pip:
    ```sh
    pip install beautifulsoup4 requests
    ```

## Uso

Para obtener la definición de una palabra específica, ejecuta el script `extractor_rae.py` con el siguiente formato:

```sh
python extractor_rae.py <palabra>
```

Si no proporcionas una palabra, el script mostrará la definición de la "palabra del día".

## Ejemplo

```sh
python extractor_rae.py programar
```

Esto mostrará las definiciones de la palabra "programar" según el Diccionario de la RAE:

Definición de programar:

1. tr. Formar programas, previa declaración de lo que se piensa hacer y anuncio de las partes de que se ha de componer un acto o espectáculo o una serie de ellos.
2. tr. Idear y ordenar las acciones necesarias para realizar un proyecto. U. t. c. prnl.
3. tr. Preparar ciertas máquinas o aparatos para que empiecen a funcionar en el momento y en la forma deseados.
4. tr. Elaborar programas para su empleo en computadoras. U. t. c. intr.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error, tienes alguna sugerencia de mejora o deseas añadir nuevas características, por favor, abre un issue o envía un pull request.

## Agradecimientos

A la Real Academia Española (RAE) por proporcionar acceso público a su diccionario en línea.
A los desarrolladores de BeautifulSoup y requests por crear herramientas poderosas para el web scraping y las solicitudes HTTP en Python.

## Licencia

Este proyecto está bajo la Licencia MIT.

Asegúrate de reemplazar `<palabra>` con la palabra específica que quieras buscar cuando estés usando el script. También puedes personalizar el contenido según sea necesario para reflejar mejor tu proyecto.





