import numpy as np
import random
def terkep():
    x=int(input('Add meg a szigetek szamat: '))
    viz=np.full((100,100),"~")
    k=[]
    t=[]
    a=random.randrange(2,97,4)
    c=random.randrange(2,97,4)

    for i in range(x):
        
        while a in k:
            a=random.randrange(2,97,4)

        k.append(a)
        while c in t:
            c=random.randrange(2,97,4)
        t.append(c)

        #print(k)
        #print(t)
        viz[a][c]="O"
        viz[a-1][c-1]="O"
        viz[a][c-1]="O"
        viz[a-1][c]="O"
        viz[a+1][c]="O"
        viz[a+1][c-1]="O"
        viz[a+1][c+1]="O"
        viz[a][c+1]="O"
        viz[a-1][c+1]="O"

    print(b)
    osszes_kirajzolhato_sziget=10000/16
    print(osszes_kirajzolhato_sziget)

try:
    terkep()
except Exception:
    print(Exception)