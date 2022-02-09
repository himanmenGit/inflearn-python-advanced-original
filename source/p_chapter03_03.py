# Chapter03-03
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), Class(클래스)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple("Point", "x y")

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)
print(type(pt3))

l_leng1 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng1)

# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])
pt5 = Point1(1.0, 5.0)
print(pt5)

Point2 = namedtuple("Point", "x, y")
pt6 = Point1(1.0, 5.0)
print(pt6)

Point3 = namedtuple("Point", "x y")
pt7 = Point1(1.0, 5.0)
print(pt7)

Point4 = namedtuple("Point", "x y x class", rename=True)
pt8 = Point4(1.0, 5.0, 20, 30)
print(pt8)
print(pt8.x)
print(pt8.y)
print(pt8.x)

# 출력
print(Point1, Point2, Point3, Point4)
print(pt5)
print(pt6)
print(pt7)
print(pt8)

# Dict to Unpacking
temp_dict = {"x": 75, "y": 55}
pt9 = Point3(**temp_dict)
print(pt9)

# 사용
print(pt5[0] + pt6[1])
print(pt5.x + pt6.y)

# UnPacking
x, y = pt7
print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]
# _make(): 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fiels(): 필드 네임 확인
print(pt5._fields, pt6._fields, pt7._fields)

# _asdict(): OrderedDict 반환 | 파이썬 버전 3.8 이상은 그냥 Dict반환
print(pt5._asdict())

# 사용 실습
# 반 20명, 4개의 반 (A,B,C,D) B14 D18

Classes = namedtuple("Classes", ["rank", "number"])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

print(numbers)
print(ranks)

# List Comprehension

students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))

# 추천
students2 = [Classes(rank, str(number))
             for rank in "A B C D".split()
             for number in range(1, 21)
             ]
print(len(students2))
print(students2)

# 출력
for s in students2:
    print(s)

