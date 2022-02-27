from cmath import sqrt


class Triangle():
    def __init__(self, a: float, b: float, c: float) -> None:
        # Encapsulamento
        if not self.__is_triangle_valid(a, b, c):
            raise ValueError('Triângulo inválido.')
        # Privado
        self.__a = a
        self.__b = b
        self.__c = c
        self.__height, self.__base = self.__calc_height()
    # Privado

    def __is_triangle_valid(self, a, b, c):
        return \
            abs(b - c) < a < b + c and \
            abs(a - c) < b < a + c and \
            abs(a - b) < c < a + b

    def __calc_height(self):
        is_equilateral, is_isosceles = self.__side_classification()

        if is_equilateral:
            return (self.__a * sqrt(3)) / 2, self.__a
        elif is_isosceles:
            equal_side, different_side = self.__get_equal_and_different_side()
            return sqrt(4 * equal_side**2 - different_side**2) / 2, different_side
        else:
            semiperimeter = (self.__a + self.__b + self.__c) / 2
            area = sqrt(semiperimeter * (semiperimeter - self.__a) *
                        (semiperimeter - self.__b) * (semiperimeter - self.__c))
            return 2 * area / self.__a, self.__a

    def __side_classification(self):
        is_equilateral = self.__a == self.__b and self.__b == self.__c and self.__a == self.__c
        is_isosceles = self.__a == self.__b and self.__b != self.__c \
            or self.__b == self.__c and self.__c != self.__a \
            or self.__a == self.__c and self.__c != self.__b
        return is_equilateral, is_isosceles

    def __get_equal_and_different_side(self):
        if self.__a == self.__b:
            return self.__a, self.__c
        elif self.__a == self.__c:
            return self.__a, self.__b
        else:
            return self.__b, self.__a
    # Getter

    def get_perimeter(self):
        return self.__a + self.__b + self.__c
    # Getter

    def get_sides(self):
        return self.__a, self.__b, self.__c
    # Getter

    def get_height(self):
        return self.__height
    # Getter

    def get_area(self):
        return self.__calc_area()

    def __calc_area(self):
        return (self.__base * self.__height) / 2
    # Setter

    def set_sides(self, a, b, c):
        self.__init__(a, b, c)
