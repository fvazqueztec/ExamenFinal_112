# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["5", "1,2,3,-4,5", "-6,7,8,-9,10", "6,5,4,3,2",
            "8,-7,-5,2,-1", "9,8,7,-6,-2", ],
        ["", "", "", "", "", "", "[[1, 2, 3, -4, 5], [-6, 7, 8, -9, 10], [6, 5, 4, 3, 2], [8, -7, -5, 2, -1], [9, 8, 7, -6, -2]]",
            "[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [6, 5, 4, 3, 2], [8, 7, 5, 2, 1], [9, 8, 7, 6, 2]]"],
        "Verifica los requerimientos que se solicitan"
    ),

    # Test case 2
    (
        ["3", "7,-6,2", "1,2,-3", "-1,-2,-3"],
        ["", "", "", "", "[[7, -6, 2], [1, 2, -3], [-1, -2, -3]]",
            "[[7, 6, 2], [1, 2, 3], [1, 2, 3]]"],
        "Verifica los requerimientos que se solicitan"
    ),
]
