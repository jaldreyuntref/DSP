El código de la prentrega contempla los algoritmos de Correlación cruzada en el dominio temporal dentro del archivo CC.py,
y la Correlación cruzada generalizada dentro de GCC.py. Estos archivos inclyuen tanto la función que aplica el algoritmo
como un código de prueba bajo el formato de if __name__ == "__main__". La prentrega también incluye una simulación simple
en el archivo simulacion.py y el archivo DOA.py que aplica la simple operación que obtiene el ángulo en funcion de los 
delays obtenidos.

CC.py presentó problemas con lo que entendemos que es aliasing temporal en los extremos del resultado de la correlación
cuando el ruido supera cierto umbral. No estamos seguro si esto se debe a un error en la implementación del algoritmo,
o un limitación del mismo. Por esta razón no fue aplicado en la simulación.

GCC.py incluye los 3 metodos de la familia de correlación cruzada generalizada, donde el parametro "mode" define que
método utilizará el algoritmo: "classic", "scot" o "phase". También incluye el parametro booleano "graphs" que si es
verdadero, graficará las señales de entrada y el resultado del algoritmo. Sobre lo que no estamos seguros si está 
correctamente implementado es el calculo de la esperanza de la multiplicación de los espectros de las señales que está
detallado en la bibliografía. Investigando en internet, entendimos que esto se logra ventaneando la señal, calculando 
la multiplicación de los espectros para cada ventana, y promediandolas. Esto es lo que hace el "for" del algoritmo.

La simulación y el código de ejemplo es bastante simple, simula el room junto con el array de micrófonos y una fuente
emitiendo un impulso. Luego, las señales se pasan por los 3 algoritmos de GCC.py, y se calculan los ángulos con DOA.py
(se omitió el uso de CC.py por lo mencionado anteriormente). Notamos que los 3 algoritmos de GCC.py devuelven exactamente 
los mismos valores. No estamos seguros si esto se debe a un error en la implementación de los algoritmos o que estamos 
usando señales simples. Estaremos atentos a esto cuando utilicemos señales mas reales.

Luego de corregir los problemas de CC.py, se expandirá y se complejizará la simulación para contemplar mas factores que 
afectan el método DOA, y el uso de señales reales. De aquí ya vamos a poder analizar todos los casos propuestos para 
el desarrollo del TP y debatirlos en el informe.
