# Gestor de Correos 💚
Es una aplicación de envío de correos masivos, la cual se compone de una pantilla en HTML, una lista de correos en un archivo de texto plano tipo .csv. Adicionalmente, se requiere el uso del archivo hidden.py, el cual almacena las credenciales de acceso al correo a través de la API de GMAIL.

## Vamos a usar los siguientes archivos
* main.py  --> contiene el programa principial
* hidden.py --> contiene las credenciales de gmail
* emails.csv --> contiene la lista de correos destino y el nombre del destinatario (en nuestro caso son nombres de empresas)
* template.html --> es la plantilla del correo a enviar.

Este aplicativo fue diseñado utilizando el contenido del [curso de Git y GitHub de Platzi](https://platzi.com/cursos/git-github/ "a ver el curso").

# Instrucciones para usar el proyecto
```sh
git clone
cd EmailManagement
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
