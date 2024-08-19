#### 내 풀이 ####
x=int(input())
z,i,l=0,0,0 # 범위의 끝값, i : 범위의 끝값을 구하기 위해 필요한 규칙 수, l : 결과값 
while z<=x:
    l+=1
    if x in range(z,6*i+2):
        print(l)
        break
    else:
        z=6*i+2
        i+=l

#### 아이디어 : 수학적 규칙 ####
## range(0,2)
## range(2,8)
## range(8,20)
## range(20,38)
## range(38,62)

## 2 - 8 - 20 - 38 - 62
## 6*0+2 - 6*(0+1)+2 - 6*(0+1+2)+2 - ... 
## f(i)=6*i+2

#### 다른 사람 풀이 ####
n = int(input())
nbox = 1
cnt = 1
while n > nbox:
    nbox += 6 * cnt
    cnt += 1
print(cnt)

# 차이점 : 나보다 변수를 1개 줄여 변수 2개로 풀이했고, if문을 사용하지 않아 코드가 짧아짐.
# 배울점 : if문 대신 while문의 조건과 변수를 사용해서 범위를 제한하는 것이 좋다.
