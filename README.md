# Proyecto-Aguacate
  ### Recomendaciones para sembradíos de aguacate en Colima y Michoacán
  #### Programa para cálculo de árboles de aguacate en un área determinada.
  ###### Facultad de Ingeniería Civil, Carretera Coquimatlán Kilómetro 9, Coquimatlán 28,400, Coquimatlán, Co-lima, Diana Isabel Gaytán Jiménez dgaytan0@ucol.mx, Rosendo Emanuel Valencia Ojeda rvalencia5@ucol.mx, Manuel Antolin Vázquez Hernández mvazquez15@ucol.mx 
  
  
  **Resumen**
  
  Se determinará la cantidad de árboles de aguacate que puede contener un área proporcionada por el usuario, respetando la superficie mínima que necesita cada planta para desarrollarse adecuadamente. 
  De igual manera se obtendrá el promedio de árboles de aguacate que pueda contener una hectárea para su posterior presentación en una gráfica.
  La determinación del número de árboles recomendados en el área de estudio se obtendrá mediante el uso de lenguaje de programación Python, auxiliado por las librerías GDAL, OGR, OSGeo, entre otras.
  Se planea que el programa obtenga las coordenadas de puntos separados por 10m cada uno.
  Con los datos obtenidos, se realizará la gráfica del promedio de árboles que pueden crecer y su respectivo análisis.
  Palabras clave: Recomendación. Aguacate. Canti-dad de árboles. Superficie. Python. GDAL. OGR. OSGeo. Promedio.
  
  
  **Abstract**
  
  The quantity of avocado trees that an area provided by the user can be determined, respecting the mini-mum area that each plant needs to develop properly.
  Similarly, the average number of avocado trees that can contain one hectare will be obtained for later representation in a graph.
  The determination of the number of recommended trees in the study area will be obtained through the use of Python programming language, aided by the libraries: GDAL, OGR, OSGeo, among others.
  The program is planned to obtain the coordinates of points separated by 10m each.
  With the data obtained, the graph and the analysis of the average number of trees that can grow will be made. 
  Keywords: Recommendation. Avocado. Quantity of trees. Surface. Pyhton. GDAL. OGR. OSGeo. Averange. 
  
  
  
  **1. 	Introducción**
  El aguacate es una fruta sabrosa y muy nutritiva que resulta beneficiosa para la salud.
  La semilla de aguacate posee propiedades que ayudan a proteger el corazón, reducir el acné y mejorar el asma. 
  En este trabajo se busca determinar la cantidad de árboles de aguacate que puede contener un área proporcionada por el usuario.
  
  1.1. 	Tipo de aguacate
  Existen 3 tipos de aguacates los cuales pueden ser cultivados en los terrenos de Colima y Mi-choacán, estos son: Aguacate Criollo, Aguacate Hass y Aguacate Orgánico. En nuestro caso, utilizaremos el Aguacate Criollo, el cual crece de forma natural sin ser híbrido ni injerto. Su piel es muy delgada, tanto, que se puede comer, ade-más, contiene fibra. Su sabor es parecido al Aguacate Anís y su consistencia es cremosa.
  Al igual que los otros árboles de aguacate, este puede llegar a crecer hasta 20 metros de altura o más, pero siempre se mantienen en 5 metros, al menos en los cultivos.
  
  1.2. 	Cuidados necesarios
  No todos los aguacates pueden crecer en las mismas condiciones, en este caso, los cuidados escritos aquí son específicamente para el Aguacate Criollo.
  Se necesitan buenas condiciones para su culti-vo, tanto en terreno como en ambiente. Un lugar cálido con luz solar parcial es perfecto para este tipo de plantas al ser subtropicales.
  Abstinencia de frío, viento y heladas. La mayo-ría de las plantas de aguacate no prospera en climas fríos, y esta planta es una de esas. Tem-peratura ideal: 20°C. Temperatura mínima: 10°C
  Tierra con buen drenaje. Distintos suelos capa-ces de drenar el agua que cae en ellos y así lograr que las raíces de la planta sean cubiertas de nutrientes en su totalidad.
  Ph muy bajo en los terrenos a plantar. Existen componentes en los ph’s neutros y altos que pueden dañar la planta.
  Riego frecuente, pero no excedente. La planta, al ser tropical, necesita cierta cantidad de agua; no tan poca como una planta desértica, pero no tanta como otras plantas. 
  Posible uso de fertilizantes de vez en cuando.
  Posible uso de insecticidas que no dañen las plantas, ya que estos pueden afectar el Ph de la planta y su vida.
  
  
  1.3. 	Terrenos a utilizar
  Los suelos más recomendados para cualquier tipo de aguacate son los de textura ligera y profundos, bien drenados y con un Ph como se mencionó anteriormente.
  También se puede cultivar en suelos arcillosos o franco arcillosos, siempre que exista un buen drenaje.
  El exceso de humedad es un medio que provo-ca enfermedades de la raíz, fisiológicas y fúngi-cas.
  Además de todo esto, el terreno debe contar con una buena protección natural contra el vien-to; este puede producir daños a las ramas o caída del fruto.
  
  1.4. 	Programas a utilizar
  Se utilizará Python, un código que al insertar las coordenadas iniciales y las finales va obtenien-do automáticamente las coordenadas de los puntos en lo que los árboles de aguacate deben colocarse.
  Dicha distancia es de 10m.
  De igual manera, el código añade las coordena-das obtenidas a un archivo csv que posterior-mente será leído en QGIS
  También se añadirá una gráfica de la cantidad de aguacates que contiene una hectárea.
  
  1.5. 	Python
  Lenguaje de programación interpretado, basado en una estructura que busca una sintaxis de un código legible. También es un lenguaje multipa-radigma, ya que soporta orientación a objetos, programación imperativa y programación fun-cional.

  1.6. 	GDAL
  Software que funciona como librería para leer y escribir raster, además de vector geoespacial de datos de formatos geoespaciales. Es un software de licencia gratuita.
  Siendo una librería, presenta un modelo de in-formación abstracta para la aplicación de todos los formatos que esta permita. También posee una variedad de comandos muy útiles en su interfaz para traducción de información y proce-samiento. Los proyectos y transformaciones están basados por la librería PROJ.
  Está considerado como el mejor software gratis para proyectos de este tipo por su extensa capacidad de intercambio y manejo de datos, además de su facilidad para comprender el uso de las herramientas que posee y el manejo de las mismas.






  **2. 	Desarrollo Experimental**

  Se busca que el programa obtenga las coorde-nadas de cada uno de los puntos en los que deben ser colocados los árboles de aguacate. Para lo cual, se requiere que se inserten las coordenadas de latitud y longitud de la esquina superior izquierda y la esquina inferior derecha de la imagen.
  De esta manera, mediante un ciclo while dentro de otro ciclo while, se le van sumando 10m a la latitud y longitud inicial hasta llegar a la coorde-nada final.
  De esta manera se obtienen los puntos desea-dos.
  A continuación, se explica qué hace cada uno de los módulos del código.
  Posteriormente se asignan los valores a las latitudes y longitudes
  Lat1= float(input("Introduzca latitud 1 en x: "))
  Lon1= float(input("Introduzca longuitud 1 en y: "))
  Lat2= float(input("Introduzca latitud 2 en x: "))
  Lon2= float(input("Introduzca longuitud 2 en y: "))

  Una vez hecho lo anterior se cambia el nombre de las variables anteriormente mencionadas
  #DY = Lat2-Lat1
  #DY = Lon2-Lon1
  #Variables para las georreferencias

  Y = Lat1
  X = Lon1

  Después se asigna el valor del incremento en cada uno de los casos.
  Para esta parte es importante mencionar que se debe realizar un cálculo con el fin de obtener a cuándos segundos en latitud y longitud equiva-len 10m.

  IncY = 0.323974082
  IncX = 0.33

  Se establecen las variables para el csv
  #Variables paras el CSV
  ff=open("PuntosAGUACATES.csv","w")
  salida=csv.writer(ff)

  Se crean los dos ciclos cuidando que mientras que el valor de la latitud inicial más el incremen-to sean menores a la latitud final el programa vaya imprimiendo cada vez que se le suma el incremento al valor de y, y así sucesivamente.

  print("Coordenadas para plantar arbolitos")
  while Y < Lat2:
    Y = (Y + IncY)
    while X < Lon2:
        X=(X +IncX)
        coordx=X
        coordy=Y
        print(coordx,",",coordy)
        salida.writerow((coordx,coordy))
    X = Lon1
    print("-------------------------")
  del salida


  Finalmente, se da la instrucción de que el pro-grama sea cerrado
  ff.close()

  
  3. 	Manejo de datos
  A continuación, se proporcionarán los datos de los aspectos en los que fue probado el progra-ma.
  
  3.1. 	Tipos de datos manejados
  El tipo de datos que se manejan en el programa son:
  Datos geoespaciales: debido a que el usuario proporciona la porción del territorio (área) en la que se desarrollará su sembradío de aguacate.
  Lenguaje de programación: Para llevar a cabo el cálculo de árboles de aguacate que puede contener una hectárea primero, es preciso divi-dir el área proporcionada mediante códigos que contienen ciclos y asignar una coordenada en latitud y longitud a cada uno de los puntos en los que cada árbol será colocado.
  Sistemas de Información Geográfica: Esto es utilizado para visualizar los resultados, es decir, las áreas de cada árbol y el lugar en dónde este debe ser sembrado.
  Cálculos estadísticos: Este tipo de cálculos fueron realizados con base a los resultados obtenidos del código, se calculó la media arit-mética de árboles que pueden ser contenidos en una hectárea.

  3.2. 	Sistema Operativo
  El programa está diseñado para trabajar en el Sistema Operativo Windows. 

  3.3. 	Equipo de prueba
  El equipo en el cual fue probado el programa es una computadora portátil de la marca Hp con las siguientes características:
  
  ![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Recomendaciones-para-sembrad-os-de-aguacate/master/XD.png)
   					
					Figura 1. Especificaciones del dispositivo


![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Recomendaciones-para-sembrad-os-de-aguacate/master/Foto1.png)

 					Figura 2. Especificaciones del Windows
					
					
					
**4. Resultados**
Lo que se logró obtener con el código fue un programa en el cual se le insertan las coorde-nadas de las latitudes y longitudes de dos de los extremos del polígono.
Con lo anterior, se genera serie de puntos con 10m de separación entre mediante dos ciclos “while” que van sumando 10m en latitud y longi-tud, obteniendo las coordenadas de cada punto.
A continuación se presenta una imagen con las coordenadas.

![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Recomendaciones-para-sembrad-os-de-aguacate/master/Foto%203.png)

						Figura 3. Coordenadas obtenidas

Para lograr que el incremento fueran correcto se tuvo que investigar la equivalencia de 10m en latitud y longitud.



**5. Conclusiones**
El lenguaje de programación Python puede ser utilizado para trabajar con Sistemas de Informa-ción Geográfica, ya que facilita la realización de diversas tareas en ellos.
Un ejemplo de lo anterior es el programa expli-cado a lo largo de este artículo, el cual se aplica al área de agricultura.
Este programa facilita al usuario conocer la cantidad de árboles que pueden ser contenidos en un área proporcionada, con lo cual se puede aprovechar al máximo el terreno del usuario y obtener una mejor ganancia.
Las expectativas que se tenían de este progra-ma fueron cumplidas, ya que se logra de mane-ra eficiente y sistematizada el cálculo y la ubica-ción de los árboles de aguacate, ahorrando tiempo y personal.El resultado se obtuvo al proporcionar dos coordenadas.
Sin embargo, la plantación de árboles de agua-cate no es el único caso en el cual se puede aplicar esta herramienta, ya que, con un poco de ingenio se pueden resolver infinidad de si-tuaciones.



**Bibliografía**
UCANR. University of California Agriculture and Natural Resources. Avocados. S/D. Recuperado de:
https://ucanr.edu/sites/alternativefruits/Avocados/

FIRA. Fideicomisos Instituidos en Relación con la Agricultura. Agrocostos. S/D. Recuperado de:
https://www.fira.gob.mx/agrocostosApp/AgroApp.jsp

INIAP. Instituto Nacional Autónomo de Investigaciones Agropecuarias. INIAP evalúa cultivo de aguacate. S/D. Recuperado de: 
https://www.agricultura.gob.ec/iniap-evalua-cultivo-de-aguacate/





