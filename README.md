# Algoritmos de ordenamiento en Python
Los algoritmos de ordenamiento y busqueda de rutas son herramientas fundamentales dentro de la programación y las ciencias computacionales. Los **algoritmos de ordenamiento** permiten organizar datos de forma eficiente para facilitar busquedas, comparaciones, análisis y procesos automáticos.

En Python, los algoritmos de ordenamiento como:
* **Bubble Sort**
* **Quick Sort**
* **Merge Sort**
* **Heap Sort**

Representan distintas estrategias para organizar listas, desde métodos simples y didácticos hasta técnicas avanzadas de alto rendimiento. Cada uno tiene caracteristícas particulares en cuanto a velocidad, complejidad y modo de funcionamiento.

En conjunto, estos algoritmos permiten comprender cómo las computadoras toman decisiones eficientes, ya sea ordenando datos o encontrando la ruta más corta hacia un objetivo.

## Bubble Sort
Es uno de los algoritmos de ordenamiento más sencillos. Funciona comparando pares de elementos adyacentes e intercambiandolos si están en el orden incorrecto. El proceso se repite varias veces hasta que toda la lista queda ordenada. Aunque no es eficiente para listas grandes, es excelente para aprender la lógica básica de los ordenamiento por comparación, ya que su funcionamiento es fácil de visualizar.

**Contexto**: Un estudiante tiene varias calificaciones de tareas y quieres ordenarlas de menor a mayor usando un método simple, como si fuera comparando una a una.

![Imagen del codigo 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Codigo1.png?raw=true)
![Imagen del resultado 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Resultado1.png?raw=true)

## Quick Sort
Es un algoritmo rápido y eficiente basado en la estrategia de divide y vencerás. Para ordenar una lista, elige un pivote y divide los elementos en tres grupos: menores, iguales y mayores al pivote. Luego, ordena recursivamente las partes y las une para formar el resultado final. Su velocidad lo convierte en uno de los métodos de ordenamiento más utilizados en la práctica, especialmente para listas grandes.

**Contexto**: Una empresa de envíos recibe paquetes con distintos tiempos estimados de entrega (en horas). Quiere ordenarlos rápidamente para priorizar los más urgentes.

![Imagen del codigo 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Codigo2.png?raw=true)
![Imagen del resultado 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Resultado2.png?raw=true)

## Merge Sort
También usa la técnica de divide y vencerás, pero lo hace dividiendo la lista en dos mitades, ordenándolas por separado y luego combinándolas de manera ordenada. Su eficiencia es muy estable, incluso en el peor caso, y por eso se utiliza en sistemas que requieren alta fiabilidad. Además, es un algoritmo estable, lo que significa que mantiene el orden relativo de elementos iguales.

**Contexto**: Un sistema de supermercado necesita ordenar los precios de varios productos para mostrarlos de menor a mayor en una pantalla digital.

![Imagen del codigo 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Codigo3.png?raw=true)
![Imagen del resultado 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Resultado3.png?raw=true)

## Heap Sort
Utiliza una estructura llamada **heap** (o montículo), donde el elemento más grande siempre se encuentra en la raíz. Primero convierte toda la lista en un heap máximo y luego extrae el valor mayor repetidamente, reconstruyendo el heap cada vez. Es un algoritmo muy eficiente en memoria, ya que no requiere espacio adicional significativo, y mantiene un rendimiento consistente.

**Contexto**: Una persona tiene varias tareas domésticas y cada una tiene un nivel de prioridad (entre 1 y 10). Se requiere ordenarlas de mayor a menor usando un método basado en un heap.

![Imagen del codigo 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Codigo4.png?raw=true)
![Imagen del resultado 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Resultado4.png?raw=true)

## Algoritmo de Dijkstra
Se utiliza para encontrar **la ruta más corta** entre nodos de un grafo cuyos pesos (costos) son positivos. Comienza asignando al nodo inicial una distancia de 0 y a todos los demás una distancia infinita. Luego selecciona el nodo con la distancia más pequeña aún no visitado, actualiza las distancias de sus vecinos y continúa hasta alcanzar el destino. Este algoritmo es la base de sistemas de navegación, mapas digitales, redes de transporte, routers de internet y muchos sistemas de optimización.

**Contexto**: Tú estás en una ciudad con un sistema de metro. Cada estación está conectada con otras mediante túneles, y cada tramo entre estaciones tiene un tiempo estimado de viaje (en minutos). Quieres ir desde una estación A hasta una estación F pasando por el menor tiempo posible.

El metro tiene las siguientes estaciones y tiempo entre ellas:
* A -> B: 4 min
* A -> C: 2 min
* B -> C: 1 min
* B -> D: 5 min
* C -> D: 8 min
* C -> E: 10 min
* D -> E: 2 min
* D -> F: 6 min
* E -> F: 3 min

Usa el **Algoritmo de Dijkstra** para calcular la ruta más rápida desde la estación A hasta la estación F, y muestra:
1. El tiempo total mínimo
2. El camino (estaciones en orden)


![Imagen del codigo 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Codigo5A.png?raw=true)
![Imagen del codigo 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Codigo5B.png?raw=true)
![Imagen del resultado 1](https://github.com/PublicStaticFun/python_sorting/blob/master/Imagenes/Resultado5.png?raw=true)
