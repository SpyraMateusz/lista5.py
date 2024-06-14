import numpy as np

# Tworzenie tablicy numpy z liczbami całkowitymi od 1 do 10
array = np.arange(1, 11)

# Wybieranie liczb większych od 5
filtered_array = array[array > 5]

# Wyświetlanie wyników
print("Tablica początkowa:", array)
print("Liczby większe od 5:", filtered_array)