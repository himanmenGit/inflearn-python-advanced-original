# Chapter02-01
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등

# 일반적인 구조
car_company_1 = "Ferrari"
cat_detiul_1 = [
    {"color": "white"},
    {"horsepower": 400},
    {"price": 8000}
]

car_company_2 = "Bmw"
cat_detiul_2 = [
    {"color": "Black"},
    {"horsepower": 270},
    {"price": 5000}
]

car_company_3 = "Audi"
cat_detiul_3 = [
    {"color": "Silver"},
    {"horsepower": 300},
    {"price": 6000}
]

# 리스트 구조
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "white", "horsepower": 400, "price": 8000},
    {"color": "Black", "horsepower": 270, "price": 5000},
    {"color": "Silver", "horsepower": 300, "price": 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
car_dicts = [
    {"car_company": "Ferrari", "car_detail": {"color": "white", "horsepower": 400, "price": 8000}},
    {"car_company": "Bmw", "car_detail": {"color": "Black", "horsepower": 270, "price": 5000}},
    {"car_company": "Audi", "car_detail": {"color": "Silver", "horsepower": 300, "price": 6000}},
]

del car_dicts[1]
print(car_dicts)

print()
print()


class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "Black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

print(car1)
print(car2)
print(car3)
print()
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print()
print(dir(car1))
print()
print()

car_list = list()
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

for x in car_list:
    print(repr(x))
    print(str(x))