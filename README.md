# Presentación
<p align="center"><img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"width="200" height="200">
</img><br>
<i><b>Docente:</b></i> Camilo Rodriguez
<br>
<i><b>Asignatura:</b></i> Big Data
<br>
<i><b>Estudiante:</b></i> Edna Sofía Orjuela Puentes <br> Herlendy Alejandro Sánchez Gaitán
<br>
<i><b>Tema:</b></i> Primer Parcial. Despliegue continuo
<br>
<i><b>Fecha:</b></i>11/03/23
<br>
</p>

# Objetivo

Crear dos funciones lambdas mediante zappa, en primer lugar una función la cual realice todos los lunes a las 9 am, webscrapping a la pagina fincaraiz, almacenando la información html original en un bucket, y la otra función será la encargada mediante un desencadenador generar un csv apartir del html guardado en el bucket anterior, para luego agregarlo a un nuevo bucket de forma organizada.<br>

El archivo final guardará la siguiente información de las casas de la pagina finca raiz, fecha de descarga, el area, los baños, habitaciones, localidad y precio, además el nombre del archivo será la fecha en la cual se descargo la pagina.
# Procedimiento

1. Usando zappa crear una función lambda que descargue la primera página de resultados del sitio Finca Raiz(https://www.fincaraiz.com.co) para la venta de casas en el sector de chapinero.
Esta lambda se debe ejecutar todos los lunes a las 9 am, es importante tener en cuenta que hay una diferencia de 5 horas debido a que esta configurado en Londres, por esta razón, se colocó 14:00.
La página html se debe guardar en un bucket s3://landing-casas-xxx/yyyy-mm-dd.html
2. Al llegar la página web al bucket se debe disparar un segundo lambda que procese el archivo y extraiga la información de cada casa.
Se debe crear un archivo CSV en s3://casas-final-xxx/yyyy-mm-dd.csv con la siguiente estructura de columnas:
FechaDescarga, Barrio, Valor, NumHabitaciones, NumBanos, mts2

Esta lambda también se debe crear con Zappa.

3. Se deben utilizar pruebas unitarias con pytest(mínimo 3). Para probar la función de descarga utilizar un mock(https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python)

4. Se debe crear un pipeline de despliegue continuo con GitHubActions al hacer push o pull request con las siguientes etapas:
* Revisión de código limpio con flake8
* Ejecución de pruebas unitarias
* Despliegue automático en AWS

# Guía de ejecución<br>
En este repositorio se encuentran los siguientes archivos:
* **/lambda1/apps.py:** Código para obtener la información de la página "finca raiz"
* **/lambda1/test_scraping:** Código para realizar las pruebas unitarias con mock
* **/lambda2/apps.py:** Código para convertir el .json en .csv y subirlo al bucket
* Los archivos zappaSettings, permiten configurar ambos lambda y agregar un evento para el desencadenador
