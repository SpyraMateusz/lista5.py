import numpy as np

# Tworzenie tablicy numpy z liczbami całkowitymi od 1 do 100
array = np.arange(1, 101)

# Znajdowanie minimum i maksimum w tablicy
min_value = np.min(array)
max_value = np.max(array)

# Wyświetlanie wyników
print("Tablica:", array)
print("Minimum:", min_value)
print("Maksimum:", max_value)