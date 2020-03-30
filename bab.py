import time
def bab(x):
    b=[]
    c=[]
    z=0
    y=int(input())
    start=time.time()
    for i in range(len(x)):
        if x[i]>y:
            b.append(i)
            c.append(x[i])
            z+=1
            if z==3:
                break
    for t in range(2):
        for y in range(2):
            if c[y]<c[y+1]:
                w=c[y]
                c[y]=c[y+1]
                c[y+1]=w
                r=b[y]
                b[y]=b[y+1]
                b[y+1]=r
    end=time.time()
    p=end-start
    return b,p
    print(b,p)

