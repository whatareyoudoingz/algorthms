n=int(input())
an=[x for x in map(int,input().split()) if x != 1] 
q=[]
for x in an:
    for y in range(2,x+1):
        if x%y==0:
            if y!=x:
                q.append(x)
                break
print(len([x for x in an if x not in q]))