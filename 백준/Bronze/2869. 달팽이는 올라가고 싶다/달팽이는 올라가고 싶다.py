#### 내 풀이 ####
a,b,v=map(int,input().split())

n,stan=(v-a)//(a-b) ,(v-a)%(a-b)
if stan==0: # 나머지가 0이면 n+1 출력
    print(n+1)
elif stan>=1: # 나머지가 1이상이면 a와 합쳐서 n+2 출력
    print(n+2)
else:
    print(n)

#### 다른사람 풀이 ####
import math
a,b,v = map(int,input().split())
day = (v-b)/(a-b)
print(math.ceil(day))

# 차이점 : 나는 a에 집중해서 수학식을 생각했다면, 다른 사람은 b에 집중해서 수학식을 작성했다.
# 배울점 : 이렇게 간단하게 구현할 수 있다니.. 코테에서 사용할 수 있는 기본적인 모듈을 잘 숙지해야 겠다.
