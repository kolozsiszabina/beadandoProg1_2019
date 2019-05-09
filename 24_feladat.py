def toHex():
    nToHex = []
    s = nToHex[::-1]
    m_tiz = 0
    a = 0
    for j in s:
        m_tiz += int(j)*(fromBase**a)
        a += 1
        return m_tiz
    else:
        s = n[::-1]
        m_tiz = 0
        j = 0
        for i in s:
            m_tiz += int(i)*(fromBase**j)
            j += 1
        return m_tiz

def to():
    k = toHex()
    m = ''
    while True:
        if k == 0:
            return m[::-1]
        else:
            m += str(k%toBase)
        k = k//toBase

e=[]
n = input('Szám: ')
fromBase = int(input('Melyik számrendszerből:'))
toBase = int(input('Melyik számrendszerbe:'))
(e.append(int(to())))
n2 = input('Szám: ')
fromBase = int(input('Melyik számrendszerből:'))
toBase = int(input('Melyik számrendszerbe:'))
(e.append(int(to())))
result=sum(e)
print(result)