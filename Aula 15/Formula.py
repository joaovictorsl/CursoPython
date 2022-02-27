class Formula():

    # Estático
    pi = 3.14

    @staticmethod
    def increase_pi():
        Formula.pi += 1

    @staticmethod  # Decorator
    def sqrt(num, idx=2):
        return num ** (1/idx)

    @staticmethod
    def bhaskara(a, b, c):
        delta = Formula.delta(a, b, c)
        if delta >= 0:
            x1 = (-b + Formula.sqrt(delta)) / (2 * a)
            x2 = (-b - Formula.sqrt(delta)) / (2 * a)
            return x1, x2
        return None, None

    @staticmethod
    def delta(a, b, c):
        return b**2 - 4 * a * c

    @staticmethod
    def comprimento_circunferencia(raio):
        return 2 * Formula.pi * raio

    @staticmethod
    def area_circunferencia(raio):
        return Formula.pi * raio ** 2
