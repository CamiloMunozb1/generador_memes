# Generador de Memes con la API de Imgflip

Este es un script en Python que permite generar memes personalizados utilizando la API de Imgflip. Los usuarios pueden ingresar su propio texto y seleccionar una plantilla de meme disponible en la API.

## Requisitos

- Python 3.x
- Biblioteca `requests`

Puedes instalar `requests` con el siguiente comando:
```bash
pip install requests
```

## Uso

1. Clona este repositorio o descarga el archivo `generador_memes.py`.
2. Ejecuta el script:
   ```bash
   python generador_memes.py
   ```
3. Ingresa el texto para la parte superior e inferior del meme.
4. Escribe el nombre de la plantilla de meme que deseas usar.
5. Si la plantilla existe, se generará un enlace con el meme creado.

## Funcionamiento

1. **Solicitar datos al usuario**: El script pide el texto y la plantilla del meme.
2. **Buscar la plantilla en la API**: Se realiza una petición GET a la API de Imgflip para obtener las plantillas de memes disponibles.
3. **Generar el meme**: Si la plantilla es encontrada, se envía una solicitud a la API con los textos ingresados y se genera el meme.
4. **Mostrar el enlace del meme**: Si la generación es exitosa, el script muestra el enlace para descargar o compartir el meme.

## Ejemplo de Uso

```bash
Ingresa el texto del meme en la parte de arriba: Cuando intento programar...
Ingresa el texto del meme en la parte de abajo: ... y todo falla
Que plantilla deseas: Distracted Boyfriend
Meme generado y listo para su uso: https://i.imgflip.com/abcd1234.jpg
```

## Notas
- Si la plantilla no es encontrada, se mostrará un mensaje de error.
- Asegúrate de ingresar correctamente el nombre de la plantilla (es sensible a mayúsculas y minúsculas).
- Debes reemplazar `YOUR_USERNAME` y `YOUR_PASSWORD` en el código con tus credenciales de Imgflip para poder generar memes.

## Autor
Este proyecto fue desarrollado por Juan Camilo Muñoz.

