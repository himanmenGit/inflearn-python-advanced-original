# Chapter01-02
# 개발 가상 환경 설정 테스트 코드

import pendulum
from datetime import datetime

pst = pendulum.timezone("America/Los_Angeles")
ist = pendulum.timezone("Asia/Seoul")

print(type(pst))

print("Current Date Time in PST = ", datetime.now(pst))
print("Current Date Time in IST = ", datetime.now(ist))

print(type(ist))