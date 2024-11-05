import numpy as np

# f(x) = 3x - cos(x) - 1
def f(x):
    return 3 * x - np.cos(x) - 1

def falsi_method(f, x0, x1, epsilon=0.00001, max_iter=1000):
    """
    Metoda regulacji fałszywej (falsi) do znajdowania pierwiastka równania nieliniowego f(x) = 0

    Metoda falsi iteracyjnie przybliża miejsce zerowe funkcji, zachowując przedział początkowy.

    Kroki rozwiązania:
        1. Wybieramy dwa punkty początkowe x_0 i x_1, takie że f(x_0) * f(x_1) < 0.

        2. Iterujemy, znajdując kolejne przybliżenie x_{n+1} zgodnie ze wzorem:
           x_{n+1} = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))

        3. Aktualizujemy przedział tak, aby utrzymać w nim pierwiastek.

        4. Iterację kończymy, gdy różnica |x_{n+1} - x_n| jest mniejsza od epsilon.

    Parametry:
        f : funkcja, której pierwiastek szukamy
        x0 : początek przedziału, gdzie f(x0) * f(x1) < 0
        x1 : koniec przedziału
        epsilon : dokładność przybliżenia
        max_iter : maksymalna liczba iteracji

    Zwraca:
        x_new : przybliżenie pierwiastka równania f(x) = 0
    """
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # Sprawdzamy, czy osiągnięto wymaganą dokładność
        if abs(f(x_new)) < epsilon:
            return x_new

        # print(x_new)
        # print(x0,x1)

        if f(x_new) * f_x0 < 0:
            x1 = x_new  # Pierwiastek jest w przedziale [x0, x_new]
        else:
            x0 = x_new  # Pierwiastek jest w przedziale [x_new, x1]

    raise ValueError("Metoda regulacji fałszywej nie zbiega w zadanej liczbie iteracji.")


x0 = 0.25
x1 = 0.75
epsilon = 0.00001

pierwiastek = falsi_method(f, x0, x1, epsilon)
print("Pierwiastek równania:", pierwiastek)
