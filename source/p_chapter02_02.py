# Chapter02-02
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등


class Car:
    """
    car Class
    Author : Park
    Date : 2021.02.08
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self.car_count = 10
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

print(car1._company == car2._company)
print(car1 is car2)
print(car1 == car2)

print(dir(car1))
print(dir(car2))

print(car1.__class__ == car2.__class__)

print(car1.__dict__)
print(car2.__dict__)

print(Car.__doc__)
print()

car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)

print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))

print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

print(car1.car_count)
print(Car.car_count)

del car2

print(car1.car_count)
print(Car.car_count)