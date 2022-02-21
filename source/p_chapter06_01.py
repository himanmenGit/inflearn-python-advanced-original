# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator 반복가능한 객체, Generator 반복가능한 객체를 만들어 줌

# 파이썬 반복 가능한 타입
# collections, text, list, dict, set, tuple, unpacking, *args... : iterable

# 반복가능한 이유 -> iter(x) 함수 호출
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for c in t:
#     print(c)

# while
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 반복형 확인
from collections import abc

print("__iter__" in dir(t))
print(isinstance(t, abc.Iterable))
print(hasattr(t, "__iter__"))

print()
print()


# Next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        # print("Called __next__")
        try:
            word = self._text[self._idx]
            self._idx += 1
        except IndexError:
            raise StopIteration("Stopped Iteration!")
        return word

    def __repr__(self):
        return f"WordSplit({self._text})"


wi = WordSplitter("Do today what you colud do tommorrow")
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

print()
print()


# Generator 패턴
# 1. 지능형 리스트, Dict, Set -> 데이터 양 증가 후 메모리 사용 증가 -> Generator 권장
# 2. 단위 실행 가능한 코루틴(Coroine) 구현과 연동
# 3. 작은 메모리 조각을 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return

    def __repr__(self):
        return f"WordSplitGenerator({self._text})"


wg = WordSplitGenerator("Do today what you colud do tommorrow")
print(wg)

wt = iter(wg)
print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))

print()
print()