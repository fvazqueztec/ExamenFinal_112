# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
        [5, 3, 4, 2, 6.7, 3.45],
        ["", "", "", "", "", "", "3.83"],
        ["La salida no cumple con el caso de prueba\nVerifica los requerimientos"]
    ),
    # Test case 2
    (
        [3, 56.23, 54.2, 8.5],
        ["", "", "", "", "39.64"],
        ["La salida no cumple con el caso de prueba\nVerifica los requerimientos"]
    ),
    # Test case 3
    (
        [1],
        ["", "Error en la cantidad"],
        ["La salida no cumple con el caso de prueba\nVerifica cuando el numero de elementos es 1 o menor que uno"]
    ),
    # Test case 4
    (
        [-5],
        ["", "Error en la cantidad"],
        ["La salida no cumple con el caso de prueba\nVerifica cuando el numero de elementos es 1 o menor que uno"]
    ),
]
