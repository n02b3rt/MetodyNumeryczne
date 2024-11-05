import numpy as np

# Definiujemy funkcję f(x) = sin(x) - 0.5 * x
def f(x):
    return np.sin(x) - 0.5 * x

# Definiujemy pochodną funkcji
def df(x):
    return np.cos(x) - 0.5

# Funkcja implementująca metodę stycznych (Newtona-Raphsona)
def metoda_stycznych(f, df, x0, epsilon=0.001, max_iter=100):
    """
    Metoda Newtona-Raphsona do znajdowania pierwiastka równania nieliniowego f(x) = 0

    Stosujemy metodę stycznych, która iteracyjnie przybliża miejsce zerowe funkcji:
        x_{n+1} = x_n - f(x_n) / f'(x_n)

    Kroki rozwiązania:
        1. Wyznaczamy pochodną funkcji f(x):
           f'(x) = cos(x) - 0.5

        2. Wybieramy punkt początkowy x_0 w przedziale [π/2, π], np. x_0 = π/2.

        3. Iterujemy zgodnie ze wzorem:
           x_{n+1} = x_n - (sin(x_n) - 0.5 * x_n) / (cos(x_n) - 0.5)

        4. Zatrzymujemy iterację, gdy różnica między kolejnymi przybliżeniami |x_{n+1} - x_n| jest
           mniejsza od epsilon = 0.001.

    Parametry:
        f : funkcja, której pierwiastek szukamy
        df : pochodna funkcji f
        x0 : punkt początkowy
        epsilon : dokładność przybliżenia
        max_iter : maksymalna liczba iteracji

    Zwraca:
        x_new : przybliżenie pierwiastka równania f(x) = 0
    """
    x = x0  # Punkt startowy
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Pochodna równa zero, metoda Newtona-Raphsona nie może być kontynuowana.")

        # Aktualizujemy wartość x zgodnie ze wzorem x_{n+1} = x_n - f(x_n) / f'(x_n)
        x_new = x - fx / dfx

        # Jeśli różnica między kolejnymi przybliżeniami jest mniejsza od epsilon, kończymy iterację
        if abs(x_new - x) < epsilon:
            return x_new

        x = x_new

    raise ValueError("Metoda Newtona-Raphsona nie zbiega w zadanej liczbie iteracji.")


x0 = np.pi / 2
epsilon = 0.001

pierwiastek = metoda_stycznych(f, df, x0, epsilon)
print("Dodatni pierwiastek równania:", pierwiastek)
