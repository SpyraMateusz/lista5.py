import numpy as np

# Generowanie tablicy numpy z liczbami losowymi
random_array = np.random.rand(3, 3)  # Tablica 3x3 z losowymi liczbami z przedziału [0, 1)

# Obliczanie średniej wartości
mean_value = np.mean(random_array)

# Obliczanie odchylenia standardowego
std_deviation = np.std(random_array)

# Wyświetlanie wyników
print("Tablica losowych liczb:\n", random_array)
print("Średnia wartość:", mean_value)
print("Odchylenie standardowe:", std_deviation)