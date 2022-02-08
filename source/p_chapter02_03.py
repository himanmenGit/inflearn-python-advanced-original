# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등


class Car:
    """
    car Class
    Author : Park
    Date : 2021.02.08
    Description: Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    # Instance Method
    def get_price(self):
        return f"Before Car Price -> company : {self._company}, price : {self._details.get('price')}"

    # Instance Method
    def get_price_culc(self):
        return f"After Car Price -> company : {self._company}, price : " \
               f"{self._details.get('price') * Car.price_per_raise}"

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 Or More")
            return
        cls.price_per_raise = per
        return print("Succeed! price increased.")

    # Statis Method
    @staticmethod
    def is_bmw(instance):
        if instance._company == "Bmw":
            return f"Ok! This car is {instance._company}"
        return f"Sorry. This car is {instance._company}"


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격정보 (직접 접근)
print(car1._details.get("price"))
print(car2._details.get("price"))

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
