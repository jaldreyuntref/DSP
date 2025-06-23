El repositorio consiste en tres carpetas:

1. Algoritmos: 

Contiene los cinco algoritmos utilizados para estimar los retrasos temporales entre señales captadas por los micrófonos,
junto con el algoritmo DOA.

2. Helpers:

Contiene funciones de ayuda principalmente para aplicar los cambios a los recintos necesarios al variar los parametros
seleccionados, junto con una función simple para visualizar el resultado de la correlación de los algoritmos.

3.  Notebooks:

Contiene los notebooks donde se lleva a cabo las simulaciones variando todos los parametros propuestos, y se guardan los
resultados en un Excel. Esta compuesta por cinco notebooks, uno corresponde a un escenario base para demostrar el proceso
experimental, y los otros cuatro contienen los distintos escenarios donde se varian los parametros elegidos. No hay un notebook
para cada parametro, sino que cada parametro fue clasificado en que parte de la simulación altera. Las clasificaciónes son:

- La señal de entrada       ->      signal.ipynb
- El recinto                ->      room.ipynb
- El arreglo de micrófonos  ->      array.ipynb
- La posición de la fuente  ->      source.ipynb

Los resultados y datasets de los parametros se encuentran en un excel dentro de datos-resultados llamados "Datos.xslx" y 
"doa_results.xlsx" respectivamente. Estos, juntos con el audio utilizado "p262_001.wav", estan excluidos del repositorio, 
pero se encuentran en el drive: https://drive.google.com/drive/folders/1yI2AfLoghB312Rh8-p-NPr-zBQSG2SAH
