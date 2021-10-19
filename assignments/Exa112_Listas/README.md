![Tec de Monterrey](../../images/logotecmty.png)
# Listas, promedio
### Tema Listas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
    pass  

if __name__ == '__main__':
    main()
```

Escribe un programa que primero lea la cantidad de elementos que vas a ingresar en la lista y después acepte cada uno de los elementos. Todos los datos que se ingresan deben ser números tipo float y meterlos en una lista. <br>

Si la cantidad de elementos es 1 o menor, se debe mostrar el mensaje de 
"Error en la cantidad".<br>

Posteriormente, el programa debe calcular el promedio de los datos ingresados en la lista y presentar el resultado redondeado a 2 decimales máximo, puedes utilizar la función "round(cantidad, 2)" <br>

## Entrada
Un número entero que representa la cantidad de valores que tiene la lista, asi como cada uno de los valores de la lista.

## Salida
El promedio de los datos con un máximo de 2 decimales "round(cantidad,2)"
## Ejemplo1 de ejecución del programa:
### Entrada
```
1
```
### Salida
```
Error en la cantidad
```

## Ejemplo2 de ejecución del programa:
### Entrada
```
5
12.4
23.45
12.32
5
17.6
```
### Salida
```
14.15
```

## Ejemplo3 de ejecución del programa:
### Entrada
```
4
5
2
4
3
```
### Salida
```
3.5
```

No uses letreros para pedir los datos. 

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.
