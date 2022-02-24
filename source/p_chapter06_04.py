# Chapter06-04
# Futures(동시성) - python 3.2부터 나온 기능
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> File, Network I/O 관련 작업에 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티스레딩/멀티프로세싱 API가 통일 -> 매우 사용하기 쉬움
# 2. 실핼중인 작업 취소, 완료 여부 체크, 타임 아웃 옵션, 콜백 함수 추가, 동기화 코드 매우 쉽게 작성
#  -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2

# Python에만 존재하는 스레드 스위칭관련 내용
# GIL(Global Interpreter Lock) : 두 개 이상의 쓰레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는경우
# -> 문제점을 방지 하기 위하여 GIL이 실행 됨, 리소스 전체에 Lock이 걸림
# -> Context Switch(문맥 교환)

# GIL 우회 : 멀티프로세싱 사용, CPython

import os
import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 100000000]


# 동시성 합계 메인 함수
# 누적 합계 함수 (제네레이터)

def sum_generator(n):
    return sum(n for n in range(1, n + 1))


def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_time = time.time()

    # 결과 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor(max_workers=worker) as excutor:
        # map은 작업 순서를 유지 함
        result = excutor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_time = time.time() - start_time
    # 출력 포맷
    msg = f"\n Result {list(result)} Time : {end_time:.2f}s"
    # 최종결과 출력
    print(msg)


# 실행
if __name__ == "__main__":
    main()
