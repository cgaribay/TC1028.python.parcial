# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["3", "a", "p", "t", "p", "a", "a"],
            ["Número de juegos: ", "Tirada de Ana: ", "Tirada de Juan: ", "Gana Juan", "Tirada de Ana: ", "Tirada de Juan: ", "Gana Ana", "Tirada de Ana: ", "Tirada de Juan: ", "Empate"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["4", "piedra", "a"],
            ["Número de juegos: ", "Tirada de Ana: ", "Tirada de Juan: ", "Las tiradas deben ser un caracter"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["3", "t", "a", "p", "r"],
            ["Número de juegos: ", "Tirada de Ana: ", "Tirada de Juan: ", "Gana Juan", "Tirada de Ana: ", "Tirada de Juan: ", "Tirada incorrecta"],
            "Revisa tu código",
        ),
        # Test case 4
        (
            ["0"],
            ["Número de juegos: ", "Las jugadas deben ser mayor a 0"],
            "Revisa tu código",
        ),
        # Test case 5
        (
            ["3", "p", "a", "p", "t", "t", "t"],
            ["Número de juegos: ", "Tirada de Ana: ", "Tirada de Juan: ", "Gana Ana", "Tirada de Ana: ", "Tirada de Juan: ", "Gana Juan", "Tirada de Ana: ", "Tirada de Juan: ", "Empate"],
            "Revisa tu código",
        )
    ]
