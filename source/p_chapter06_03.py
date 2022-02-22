# Chapter06-03
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행, 단일 프로그램안에서 여러일을 쉽게 해결
# 병렬성(parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행, 속도
# 코루틴(Coroutine)

# 코루틴 : 단일(싱글) 쓰레드에서 스텍을 기반으로 동작하는 비동기 작업
# 쓰레드 : OS에서 관리, CPU 코어에서 실시간 또는 시분할 비동기 작업 -> 멀티쓰레드
# yield, send : 메인 <-> 서브
# yield from : iterable한 객체를 순차적으로 반환(yield)
# 코루틴을 제어, 상태, 양방향 전송 (왼쪽은 서브루틴에서 받는 값, 오른쪽은 메인쓰레드로 반환 되는 값)
# -> x yield y -> y반환 x대입

# 서브루틴 : 메인루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴을 실행중에 중지 한 다음 재실행 -> 동시성 프로그래밍
# 코루틴 : 쓰레드에 비해 오버헤드가 감소
# 쓰레드 : 싱글쓰레드, 멀티쓰레드 -> 복잡하다 -> 공유되는 자원
#  -> 교착상태가 발생(Dead Lock, Race Condition)
#  -> 컨텍스트 스위칭 비용이 발생(큼) -> 자원 소비 가능성이 증가 된다.

# python 3.5 이상에서는 def -> async, yield -> await로 실행 가능

# 코루틴 Ex1
# yield가 들어가면 generator
# 코루틴은 generator에서 파생
# generator기반 코루틴
# 함수, 제너레이터, 코루틴은 def 로 선언
# 함수인지 제너레이터인지 코루틴은지는 내용을 봐야 한다.
def corouine1():
    # 제너레이터, 서브루틴
    print(">>> coroutine started.")
    i = yield
    print(f">>> conroutine received: {i}")


# 제너레이터 선언
# 제너레이터는 for문에서 사용시 StopIteration Exception이 발생하지 않는다.
cr1 = corouine1()
print(cr1, type(cr1))

# yield 지점까지 서브루틴을 수행
# next(cr1)

# 기본 전달 값 None
# 값 전송
# cr1.send(100)

# 잘못된 사용
cr2 = corouine1()


# 시작단계에서는 바로 send를 할 수 없고 yield가 된 지점(순간)부터 send가 가능하다.
# cr2.send(100)

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print(f">>> coroutine started : {x}")
    y = yield x
    print(f">>> coroutine received1 : {y}")
    z = yield x + y
    print(f">>> coroutine received2 : {z}")


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

# next이후 y값을 받을 대기 상태
print(next(cr3))
print(getgeneratorstate(cr3))

# send 이후 z값을 받을 대기 상태
print(cr3.send(100))
print(getgeneratorstate(cr3))

# send 이후 print후 yield가 없으므로 StopIteration Exception raise
# print(cr3.send(100))
# print(getgeneratorstate(cr3))

print()
print()


# 코루틴 Ex3
# StopIteration Exception도 3.5버전 이상에서는 await로 자동 처리 가능
# 중첩 코루틴 처리


def generator1():
    for x in "AB":
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()

print(list(t2))

print()
print()


def generator2():
    # from은 제너레이터에서 iterable한 객체를 순차적으로 반환함.
    yield from "AB"
    yield from range(1, 4)


t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print("---")
t4 = generator2()
for t in t4:
    print(t)

# 제너레이터와 코루틴의 차이는
#  제너레이터는 서브 루틴 함수 내에서 yield로 iterable한 객체를 만들어 데이터를 반환하는것이고
#  코루틴은 메인 루틴 에서 서브 루틴 함수 내로 yield로 데이터를 주입해서 소비 가공 할 수 있다는 것.