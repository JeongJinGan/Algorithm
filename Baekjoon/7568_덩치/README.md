## 덩치

```python
각 사람보다 덩치가 큰 사람의 수 = [0] * 사람의 수

if x> p and y > q:
    print("A는 B보다 덩치가 크다")
    B보다 덩치가 큰 사람 수 += 1
```



```python
# 사람의 수 N 입력
N = int(input())

list_ = []
# 각 사람의 몸무게와 키 입력
for i in range(N):
    weight, height = list(map(int, input().split()))
    # 리스트에 몸무게와 키를 저장
    list_.append((weight, height))

ranks = [0] * N  
# 모든 사람을 비교하기 위한 이중 반복문
for a in range(N):
    # 기준이 되는 사람
    A = list_[a]
    for b in range(N):
        # 비교가 되는 사람
        B = list_[b]
        
        # A가 B보다 덩치가 큰지 조건문이 필요하다
        # B가 A보다 덩치가 
        # x > p and y > q
        if A[0] > B[0] and A[1] > B[1]:
            # B보다 덩치가 큰 사람이 한명 더 있다 + 1
            ranks[b] += 1
            # print(A[0],B[0], A[1],B[1], ranks)

print(ranks)
for rank in ranks:
    print(rank+1, end = " ")
```

