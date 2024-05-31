# Calculadora de impuestos 

## ¿Quién hizo esto? (Autores)

- Santiago Rodriguez.
- Pablo Troncoso.

## ¿Qué es y para qué es?

Una calculadora de impuestos, tiene como propósito principal automatizar y simplificar el proceso de preparación y presentación de las declaraciones de impuestos. Esto puede ayudar a reducir errores y minimizar el tiempo necesario para completar las tareas relacionadas con los impuestos.

## ¿Cómo lo hago funcionar?

### Prerequisitos
- **Editor de codigo fuente:** Asegúrate de tener instalado un editor de codigo funete en tu sistema. Te recomendamos Visual Studio Code puedes descargarlo e instalarlo desde el sitio oficial de Visual Studio Code: [Descargar VS Code](https://code.visualstudio.com/Download).
- **Python:** Debes tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde el sitio oficial de Python: [Descargar Python](https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la casilla "Agregar Python al PATH".

### Datos necesarios para la ejecucion 
- **Total de ingresos laborales en el año:** Representa la suma acumulada de los salarios percibidos a lo largo de todo el año.
- **Valor otros ingresos gravables:** Comprende aquellos ingresos que, de acuerdo con la legislación colombiana, están sujetos a un porcentaje de impuestos. Esto incluye fuentes como loterías, negocios, inversiones, alquileres, entre otros
- **Valor otros ingresos no gravables:** Son aquellos que no están sujetos a un porcentaje de impuesto según la legislación. Ejemplos de estos ingresos incluyen subsidios, indemnizaciones, herencias, donaciones, entre otros.
- **Valor retencion en la fuente al año:** Representa la cantidad total retenida en concepto de impuestos a lo largo del año.
- **Pago créditos hipoteca en el año:** Es un deducible que abarca todos los gastos relacionados con la vivienda, incluyendo seguros y préstamos hipotecarios.
- **Valor donaciones en el año:** Es una deducción que se refiere a las contribuciones que has realizado a lo largo del año en forma de donaciones.
- **Gastos en educación en el año:** Representan una deducción relacionada con los costos asociados a la educación durante el período anual.

### Datos resultantes de la ejecucion
- **Total de ingresos gravados:** (Ingresos laborales + otros ingresos gravados + otros ingresos no gravables) – otros ingresos gravables. 
- **Total ingresos no gravables:** Todos los ingresos no gravables del año. 
- **Total costos deducibles:** pago seguridad social + aportes pensión en el año + pago créditos hipotecarios en el año + valor donaciones en al año + gastos educación en el año. 
- **Valor a pagar por impuesto de renta:** Se refiere a la cantidad total que debe abonarse como impuesto de renta. Este monto está determinado por porcentajes variables que se definen en función de la cantidad total de ingresos gravables percibidos.

## ¿Cómo esta hecho?

El proyecto, esta diseñado con clases, funciones, erroes y excepciones, tambien tenemos tres bibliotecas importadas, las cuales son, **unittes** para ejecutar las pruebas, **sys** para poder guiar la ruta completa y de manera segura en las carpetas del programa y **Kivy** para la creacion de la interfaz grafica y **flask** para la creacion de la interfaz web.

En este proyecto tenemos dos carpetas principales, las cuales son **src**(en esta carpeta, esta una carpeta llamada **Logic** con un archivo llamado TaxLogic en el cual esta toda la logica del proyecta, tambien tenemos una carpeta llamada **console**, en donde hay un archivo llamdado TaxConsole en el nos permite ejecutar el programa por medio de la consola/terminal y otra carpeta llamada **GUI**, en donde hay un archivo llamado Tax_GUI el cual nos permite correr la interfaz grafica) y por ultimo tenemos una carpeta llamada **test**, en donde hay un archivo llamado TaxTests, en el cual estan todos los test del programa.

## Estructura sugerida
    -Carpeta image, en la cual se encuentra el logo de la app.
    -Carpeta scr, en la cual se encuentran tres carpetas, en Controller se encuentra el controlador con la base de datos y  el archivo para conectarse con esta, en Model la logica del proyecto y en View la interfaz grafica y la interfaz por consola.
    -Carpeta test, en esta carpeta estan las pruebas unitarias.
    -Carpeta testBD, en esta carpeta se encuentran las pruebas unitarias de la base de datos.
    
## ¿Cómo lo hago funcionar?
Tener en cuenta: primeramente debe descargar el repositorio, para hacerlo ten en cuenta los siguientes pasos:
1. Instalada la aplicación Git. [Descargar Git](https://git-scm.com/download/win)
2. Copiar el link del repositorio. 
3. Entra a el escritorio de tu computadora, das click derecho y presiona la opción open git bash here.
4. En la consola de git bash escribe el comando "git clone" y pega el link del repositorio, recuerde que para pegar el link debes presionar click derecho y luego presiona en pegar, despues le das entrer y el repositorio se comenzara a descargar en el escritorio. 

### NOTA
- En esta aplicacion la Base de datos funciona unicamente con la interfaz grafica

### Configuracion Base de datos
1. Debes ingresar a la pagina Neon. [Neon.Tech](https://neon.tech/)
2. Te registrar/logea, una vez registrado debes crear un proyecto, el titulo del proyecto a tu preferencia y el nombre de la base de datos puede porle: "Calculadora_Impuestos" y le das es crear proyecto.
3. Una vez  creado el proyecto y la base de datos te dirijes a la opcion **Dashboard**.
4. Desplegas el menu donde dice **Connection string**, alli seleccionas la opcion de **Parameters only**.
5. Copias todo lo que se encuentra en el campo de texto y te dirijes donde tienes el repositorio abierto.
6. Creas un archivo llamado **SecretConfig.py** donde pegaras todas tus credenciales, de la siguiente forma:

#### PGDATABASE = "Nombre de la base de datos"
---
#### PGUSER = "Nombre de usuario asignado" 
---
#### PGPASSWORD = "Contraseña asiganda por Neon.tech" 
---
#### PGHOST = "Host asignado"
---
#### PGPORT = 5432 # POR DEFECTO ES 5432, PERO PUEDE CAMBIAR EN SU DB
---
#### PGCODE = "postgresql://neonDB_owner:************@ep-crimson-hat-a5bpoec2.us-east-2.aws.neon.tech/neonDB?sslmode=require"--> en el apartado connection string, copiar y pegar el postgresql de tu base de datos asi como este de ejemplo.

### Ejecutar la página web (Base de Datos)

1. Instalar todas las dependencias necesarias para poder acceder a la librería flask y poder ingresar a la página web:

    `pip install flask`

2. Clona el repositorio o descarga los archivos del programa.

    `git clone https://github.com/gfrda347/Entrega5-Calculadora-Impuestos.git`

3. Abre una terminal en la carpeta donde se encuentran los archivos del programa.

    `cd Entrega5-Calculadora-Impuestos`

4. Ejecuta el siguiente comando para iniciar el programa: 

    `python view_web\vista_usuarios.py`

### Ejecutar por consola 
1. Abra la terminal en su computadora.
2. En la terminal utilice el comando **cd** para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
3. Utilice el mismo comando para entrar a la aplicación "cd Calculadora_Impuestos". 
4. Utilice el mismo comando para entrar a la carpeta src, que es donde estan organizadas las carpetas con los archivos necesarios para que la aplicación funcione "cd src". 
5. Luego copie la ruta que lleva hasta el momento en la terminal y luego escriba el comando "set PYTHONPATH=ruta" aqui va la ruta que copio, ejemplo: set PYTHONPATH=C:\ruta\Escritorio\Calculadora_Impuestos\src
6. Utilice el comando cd para entrar a la carpeta console que es donde se encuentra el menú "cd console".
7. Despues utilice el comando "python TaxConsole.py".
8. Aparecera un menú y usted sigue las instrucciones.
    
### Ejecutar pruebas e información de más
1. Abra la terminal en su computadora.
2. En la terminal utilice el comando **cd** para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
3. Utilice el mismo comando para entrar a la aplicación "cd Calculadora_Impuestos". 
4. Utilice el mismo comando para entrar a la carpeta src, que es donde estan organizadas las carpetas con los archivos necesarios para que la aplicación funcione "cd src". 
5. Luego copie la ruta que lleva hasta el momento en la terminal y luego escriba el comando "set PYTHONPATH=ruta" aqui va la ruta que copio, ejemplo: set PYTHONPATH=C:\ruta\Escritorio\Calculadora_Impuestos\src
6. Utilice el comando cd.. para salir de la carpeta src "cd.."
7. Utilice el comando cd para entrar a la carpeta que desee, **test** que es donde se encuentran las pruebas unitarias de la logica: "cd test" o **testBD** que es donde se encuentran las pruebas unitarias de la Base de datos.
8. Despues utilice el comando "python TaxTests.py" si estas en **test** o utiliza el comando "python TestsBD.py" si estas en **testBD**. 

### Ejecutar la interfaz grafica (Base de Datos)
1. Abra la terminal en su computadora.
2. En la terminal utilice el comando **cd** para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
3. Utilice el mismo comando para entrar a la aplicación "cd Calculadora_Impuestos". 
4. Utilice el mismo comando para entrar a la carpeta src, que es donde estan organizadas las carpetas con los archivos necesarios para que la aplicación funcione "cd src". 
5. Luego copie la ruta que lleva hasta el momento en la terminal y luego escriba el comando "set PYTHONPATH=ruta" aqui va la ruta que copio, ejemplo: set PYTHONPATH=C:\ruta\Escritorio\Calculadora_Impuestos\src
6. Utilice el comando cd para entrar a la carpeta GUI que es donde se encuentra la interfaz "cd GUI".
7. Despues utilice el comando "python Tax_GUI.py".


## Tener en cuenta lo siguiente para que no lance errores:
- No ingresar los ingresos laborales totales en el año
- Ingresar valores en texto 
- Ingresar valores muy grandes > 10 digitos 
- No ingresar los datos obligatorios
- Ingresar los deducibles negativos
- No ingresar los activos 
- Ingresar un valor negativo en los ingresos 
