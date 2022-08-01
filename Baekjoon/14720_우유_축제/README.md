# BOJ - 14720 (우유 축제)

데크로 풀기

```python
from collections import deque
n = int(input())                            # 우유 가게 수
store = list(map(int, input().split()))     # 우유 가게 정보
pattern = deque([0, 1, 2])                  # 우유 패턴을 덱으로 정의
cnt = 0
for i in range(n):
    if store[i] == pattern[0]:        # 영학이의 우유 구매 패턴이 우유가게의 품목과 일치하면
        cnt += 1                            # 카운트
        pattern.append(pattern.popleft())   # 패턴 변화시키기 [0, 1, 2] -> [1, 2, 0]
print(cnt)                                  # 일치한 만큼 숫자 출력하기
```

