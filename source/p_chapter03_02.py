# Chapter03-02
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), Class(클래스)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제2
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector:
    def __init__(self, *args):
        """
        Create a Vector, example : v = Vector(5, 10)
        :param args: (5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        :return: Return the vector infomations
        """
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other):
        """
        Return the vector addtion of self and other
        :param other: Vector
        :return: Vector
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        """
        Return the vector multiple of self and other
        :param other: Vector
        :return: Vector
        """
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# 매직 메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)
print(Vector.__mul__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2), bool(v3))