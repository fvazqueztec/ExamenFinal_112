![Tec de Monterrey](../../images/logotecmty.png)
# Cambia negativos a positivos

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():  
  pass

if __name__ == '__main__':
    main()
```

<h3>Cambia negativos a positivos</h3>
Desarrolla la función leer_matriz para leer la matriz, la cual recibe el número de renglones (num_ren). <br>

En la función se deberán pedir los num_ren, cada renglon que se solicita tiene el siguiente formato: <br>
12,5,1, es decir cada uno de los números va separado por una "," 
la función debe regresar la matriz con los números en string.<br> 

Desarrolla la función convierte_matriz_enteros para convertir los numeros (string) a enteros, la función recibe como parámetro de entrada la matriz con los datos y regresa la matriz ya con los números (int)<br>

Desarrolla la función cambia_negativos_positivos que recibe una matriz de enteros, la función debe regresar la matriz solo con números positivos, es decir, cada número que sea negativo, éste deberá ser cambiado a positivo, por ejemplo el -5 se convierte en 5 <br><br>

El programa deberá: <br>
1.- Solicitar la cantidad de renglones<br>
2.- Llamar la función leer_matriz  (el usuario ingresa los renglones correspondientes)<br>
3.- Llamar a la función convierte_matriz_enteros <br>
4.- Imprimir la matriz de enteros "print (matriz)" <br>
5.- Llamar a la función cambia_negativos_positivos <br>
6.- Imprimir la nueva matriz con cada uno de los elementos "print (matriz)" <br>



Entrada <br>
Número de renglones de la matriz
Los datos de la matriz que son renglones separados por una "," 

Salida<br>
Una matriz con los enteros ingresados
Una matriz con solo números positivos

Ejemplo1 de ejecución del programa:<br>
```
3   <--- cantidad de renglones o filas 
1,-2,-10 <--- cada uno de los renglones
-1,3,6
4,-2,5
```
### Salida
```      
[[1, -2, -10], [-1, 3, 6], [4, -2, 5]]  <--- Matriz con los números enteros
[[1, 2, 10], [1, 3, 6], [4, 2, 5]]  <--- Matriz con los números positivos 
```

Ejemplo2 de ejecución del programa:<br>
```
2
1,3,-4,5,-7
-5,-3,2,-8,9
```
### Salida
```      
[[1, 3, -4, 5, -7], [-5, -3, 2, -8, 9]]
[[1, 3, 4, 5, 7], [5, 3, 2, 8, 9]]
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.
NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

