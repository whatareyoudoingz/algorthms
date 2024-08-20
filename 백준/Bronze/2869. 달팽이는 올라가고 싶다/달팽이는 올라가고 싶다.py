a,b,v=map(int,input().split())

target=v-a 
n,stan=target//(a-b) ,target%(a-b)
if stan==0: 
    print(n+1)
elif stan>=1: 
    print(n+2)
else:
    print(n)