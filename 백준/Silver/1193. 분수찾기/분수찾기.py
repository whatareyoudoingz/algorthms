#### 내 풀이 ####
q = int(input())
x,y,v,cnt=1,1,0,q-1
for z in range(10000000):
    total,v=5*z+5+4*z*(z+1)//2,int(z)
    if total>q: break
    
for p in range(v+1):
    cnt1,cnt2,cnt3=1,2*p+1,2*p+2
    if cnt>0:
        move=min(cnt, cnt1)
        y+=move
        cnt-=move
    if cnt>0:
        move=min(cnt, cnt2)
        x+=move
        y-=move
        cnt-=move
    if cnt>0:
        x+=1
        cnt-=1
    if cnt>0:
        move=min(cnt, cnt3)
        x-=move
        y+=move
        cnt-=move
        
print(f'{x}/{y}')

#### 아이디어 : 수학적 규칙 ####
README.md에 첨부

#### 다른 사람 풀이 ####
X = int(input())
n, i = 0, 1
while X > n:
    n += i
    i += 1
a = n - X + 1
b = i - a
print(f"{a}/{b}" if i % 2 == 0 else f"{b}/{a}")

# 차이점 : 나는 분수 전체의 규칙성에 집중한 반면, 분자,분모 각각의 규칙성에 집중함.
# 배울점 : 굉장히 1차원에서 접근했음에 헛웃음이 나고 허탈하다. 타인의 풀이는 굉장히 짧고 효율적이다. 다각도로 생각하는 힘을 길러야겠다.
