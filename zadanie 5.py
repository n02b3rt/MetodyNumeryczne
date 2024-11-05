# f(x) = x^3 + x^2 - 3x - 3
def f(x):
    return x**3 + x**2 - 3*x - 3

def metoda_siecznych(f, x0, x1, epsilon=0.0001, max_iter=100):
    """
    Metoda siecznych do znajdowania pierwiastka równania nieliniowego f(x) = 0

    Metoda siecznych iteracyjnie przybliża miejsce zerowe funkcji bez korzystania z pochodnej:
        x_{n+1} = x_n - f(x_n) * (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))

    Kroki rozwiązania:
        1. Wybieramy dwa początkowe punkty x_0 i x_1 w przedziale [1, 2].

        2. Iterujemy, aż różnica między kolejnymi przybliżeniami |x_{n+1} - x_n|
           będzie mniejsza od epsilon = 0.0001.

    Parametry:
        f : funkcja, której pierwiastek szukamy
        x0 : pierwszy punkt początkowy
        x1 : drugi punkt początkowy
        epsilon : dokładność przybliżenia
        max_iter : maksymalna liczba iteracji

    Zwraca:
        x_new : przybliżenie pierwiastka równania f(x) = 0
    """
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            raise ValueError("Różnica wartości funkcji jest zerowa, metoda siecznych nie może być kontynuowana.")

        # Obliczamy kolejny przybliżony pierwiastek zgodnie z metodą siecznych
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # print(x_new)

        if abs(x_new - x1) < epsilon:
            return x_new

        # Przesuwamy punkty dla kolejnej iteracji
        x0 = x1
        x1 = x_new

    raise ValueError("Metoda siecznych nie zbiega w zadanej liczbie iteracji.")


x0 = 1
x1 = 2
epsilon = 0.0001

pierwiastek = metoda_siecznych(f, x0, x1, epsilon)
print("Pierwiastek równania:", pierwiastek)