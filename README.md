# Gestor de Correos 💚
Es una aplicación de envío de correos masivos, la cual se compone de una pantilla en HTML, una lista de correos en un archivo de texto plano tipo .csv. Adicionalmente, se requiere el uso del archivo hidden.py, el cual almacena las credenciales de acceso al correo a través de la API de GMAIL.

Agradecimientos a https://realpython.com/python-send-email/ por publicar su blog relacionado al tema.

## Vamos a usar los siguientes archivos
* main.py  --> contiene el programa principial
* hidden.py --> contiene las credenciales de gmail
* emails.csv --> contiene la lista de correos destino y el nombre del destinatario (en nuestro caso son nombres de empresas)
* template.py --> es la plantilla del correo a enviar.
* requirements.txt --> librerias necesarias para correr el programa

Este aplicativo fue diseñado utilizando el contenido del [curso de Git y GitHub de Platzi](https://platzi.com/cursos/git-github/ "a ver el curso").

# Instrucciones para usar el proyecto

## Primer paso: clonar el proyecto
```sh
git clone git@github.com:LuisMendozaCOL/EmailManagement.git
cd EmailManagement
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
mkdir files
touch hidden.py
```
## Segundo paso: agregar tu correo y contraseña de GMAIL al archivo hidden.py
```sh
user="TuCorreo"
password="TuContraseña"
```

## Tercer paso (opcional): modificar el archivo template.html
Modifica el archivo template para enviar un correo personalizado

## Cuarto paso: modifica el archivo emails.csv
Modifica el archivo para agregar la lista de correos a los cuales le quires enviar el correo

## Quinto paso: modifica las variables subject y sender_email para personalizar el título del correo y el correo que envía el mensaje

subject = "Vacante: desarrollador en Python"
sender_email = "TuCorreo"

## Sexto paso: agregar archivos adjuntos
Agrega tus archivos adjuntos a la carpeta files en formato pdf
        
## Septimo paso: correr el script

```sh
python3 main.py
```

