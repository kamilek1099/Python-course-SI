import time
def ins(x):
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
    for i in range(2):
        o = c[i]
        j = i - 1
        while j>=0 and c[j]>o:
            c[j + 1] = c[j]
            c[j + 1] = o
            b[j + 1] = b[j]
            b[j + 1] = o

    end=time.time()
    return b,end-start
    print(b,end-start)

