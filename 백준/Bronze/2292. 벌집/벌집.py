x=int(input())
z,i,l=0,0,0
while z<=x:
    l+=1
    if x in range(z,6*i+2):
        print(l)
        break
    else:
        z=6*i+2
        i+=l