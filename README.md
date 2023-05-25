# MusicProAPIrest

Esta es una API REST para gestionar productos de una tienda de música, donde los usuarios pueden ver, crear, actualizar y eliminar productos.

Requisitos previos
Asegúrate de tener instalados los siguientes componentes antes de ejecutar la API:

instalar Python 3.x(3.11.2 recomendable)
Instalar anaconda3 ultima version

lista
-MongoDB(opcional mongo compass para poder revisar desde forma local el servidor)
-uvicorn
-fastapi
-black
-transbank-sdk(python, opcional ya que no se hizo la integracion de webpay)
-pymongo
-flask

Instalación
1.Clona este repositorio en tu máquina local:
bash
Copy code
git clone https://github.com/MoisesFigueroaDeveloper/MusicProAPIrest.git

2.Ve al directorio del proyecto:
bash
Copy code
cd MusicProAPIrest

3.Crea un entorno virtual:
bash
Copy code
python -m venv env

4.Activa el entorno virtual:
En Windows:
bash
Copy code
env\Scripts\activate
En Linux o macOS:
bash
Copy code
source env/bin/activate

5.Instala las dependencias del proyecto:
Copy code
pip install -r requirements.txt

6.Configura la conexión a la base de datos:
Abre el archivo config.py en el directorio config.
Reemplaza los valores de host, port, username y password con la información de tu base de datos MongoDB.

7.Inicia la API:
css
Copy code
uvicorn main:app --reload
La API se ejecutará en http://localhost:8000.

Endpoints
Obtener todos los productos
bash
Copy code
GET /products
Este endpoint devuelve todos los productos disponibles.

Obtener un producto por ID
bash
Copy code
GET /products/{id}
Este endpoint devuelve un producto específico basado en su ID.

Crear un nuevo producto
bash
Copy code
POST /products
Este endpoint crea un nuevo producto. Se deben proporcionar los datos del producto en el cuerpo de la solicitud.

Actualizar un producto existente
bash
Copy code
PUT /products/{id}
Este endpoint actualiza un producto existente basado en su ID. Se deben proporcionar los nuevos datos del producto en el cuerpo de la solicitud.

Eliminar un producto
bash
Copy code
DELETE /products/{id}
Este endpoint elimina un producto existente basado en su ID.

Contribución
Si deseas contribuir a este proyecto, siéntete libre de enviar pull requests o abrir issues en el repositorio.

Licencia
Este proyecto está bajo la Licencia MIT. Puedes consultar el archivo LICENSE para obtener más detalles.

Espero que esto te ayude a comenzar con tu proyecto. No dudes en personalizar y agregar más información relevante según tus necesidades. ¡Buena suerte con tu API REST de MusicPro!
