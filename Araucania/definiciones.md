## Definiciones simulación

La idea básica es la siguiente. 
- nativos deambulan alrededor de sus ciudades
- colonos llegan por un lado del mapa, buscando incrementar territorio
- cuando se encuentran, hay una probabilidad de lucha, o de escape
- hay un parámetro, que llamamos cultura, asociada a cada ciudad. Este numero aumenta cuando mueren nativos en un enfrentamiento (y quizás aumenta por si solo)

### Parámetros identificados

- numero de ciudades
- cultura inicial de nativos
- numero inicial de nativos x ciudades (puede ser un rango para sacar algo al azar también)
- tasa a la que llegan colonos
- tasa a la que se reproducen nativos
- movimiento de los nativos. Debería ser un random walk pero que dependa de cuan cerca o lejos este de su ciudad (por parámetro), y del nivel de cultura de esa ciudad. 
- ventana para enfrentamientos, cuan cerca o lejos deben estar los bandos para enfrentarse
- rangos de resultado de enfrentamientos: la diferencia entre colonos y nativos en el entorno cercano al enfrentamiento es un entero D. Luego podría ser que los nativos o colonos escapen, o que se enfrenten. Puede o debe depender de la cultura también.   
- probabilidad con la que el enfrentamiento resulta en muertes (debería depender de la cantidad de colonos y nativos)
- cuanta cultura se pasa al reproducir
- Como agregar cultura cuando muere un nativo, a cada ciudad. Se debe agregar dependiendo inversamente de la distancia entre el nativo y la cultura. 

### Definiciones 

#### Espacio
- Por ahora, un cuadrado. Se identifica el lado por donde llegan colonos, y se asignan n ciudades. 

#### Movimiento
- los nativos deberían moverse bajo la restricción de que se queden cerca de su ciudad de origen
- los colonos llegan desde un lado, y comienzan un random walk. 
- Hay un contador general del #de celdas ocupadas por los colonos. Consideraría que una celda está "ocupada" por españoles si hay una especie de camino entre el norte, esa celda y un colono, sin pasar por un nativo. 
- Luego el movimiento de ellos está dado por maximizar esa cantidad de celdas (es decir, hay mas probabilidad de moverse a un cuadrado que maximize eso). 

#### enfrentamiento
cuando un nativo y un colono se acercan a una cierta ventana, pasa lo siguiente. 
- se cuentan los nativos cerca de ese nativo
- se cuentan los colonos cerca de ese colono
- con una probabilidad: Hay un enfrentamiento, o escapa una facción (a celdas cercanas a la ventana pero no tanto como para volver a gatillar un enfrentamiento altiro)
- el enfrentamiento puede acabar con la muerte de colonos o nativos. Hay que armar una regla, deberia ser aleatoria pero favorecer a los colonos?
- a mayor cultura de los nativos aumenta la probabilidad de enfrentamiento por sobre escapar.

3- cultura
- los nativos tienen cultura. Esta cultura aumenta con los enfrentamientos. Cuando se muere un nativo, todos los nativos en una ventana incrementan su cultura en un x% (o en un incremento fijo). 

4- generaciones
- los nativos tienen hijos, y los hijos heredan un porcentaje de la cultura (puede ser con cierta probabilidad). 
- por ahora, los nativos se reproducen como células (cada nativo tiene una probabilidad de dividirse en dos)
- los colonos llegan cada cierto tiempo (no tienen hijos)

5- datos
- Para entender lo que pasa, definitivamente hay que ir ploteando los números de nativos y españoles, deberían estar equilibrados. 
-Además de eso, interesa ir viendo cómo cambia la distribución de los enfrentamientos -> la hipótesis es que con el paso del tiempo, los enfrentamientos van a estar más concentrados en unas zonas específicas (hay que ver cómo visualizar eso, una posibilidad para empezar es ver el nº de enfrentamientos en cada celda al final de la simulación).
