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