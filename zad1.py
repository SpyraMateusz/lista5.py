import numpy as np

# Tworzenie dwóch tablic numpy o wymiarach 3x3
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

array2 = np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

# Dodawanie dwóch tablic
result = np.add(array1, array2)

# Wyświetlanie wyników
print("Pierwsza tablica:\n", array1)
print("Druga tablica:\n", array2)
print("Wynik dodawania:\n", result)