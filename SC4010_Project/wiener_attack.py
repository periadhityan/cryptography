def wiener_attack(e, n):

    _, convergents = form_continued_fractions(e, n)

    print_conv = False
    #print_conv = True
    for (k, d) in convergents:

        if(print_conv):
            print()
            print("Convergent K = ", k)
            print("Convergent D = ", d)

        if k != 0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi +1
            disc = s*s - 4*n
            if(disc>=0):
                t = is_perf_sq(disc)
                if t!=-1 and (s+t)%2==0:                    
                    return d
        if(print_conv):        
            print("Invalid convergents")

    return "Decryption Exponent Not Found"

def is_sqrt(n):

    if n<0:
        raise ValueError('Square root is not defined for negtive numbers')
    
    if n == 0:
        return 0
    
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a+b)

    while True:
        y = (x+n//x)//2

        if y >= x:
            return x
        x = y

def is_perf_sq(n):

    h = n & 0xF

    if h > 9:
        return -1
    
    if (h!=2 and h!=3 and h!=5 and h!=6 and h!=7 and h!=8):
        t = is_sqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    
    return -1

CFList = list[int]
CVList = list[tuple[int, int]]

def form_continued_fractions(x: int, y: int) -> tuple[CFList, CVList]:
    a = x // y
    cflist = [a]
    cvlist = [(a, 1)]
    ppn, ppd = 1, 0
    pn, pd = a, 1

    while a*y != x:
        x, y = y, x - a*y
        a = x // y
        cflist.append(a)

        cn, cd = a*pn + ppn, a * pd + ppd
        cvlist.append((cn, cd))

        ppn, ppd = pn, pd
        pn, pd = cn, cd
        
    return cflist, cvlist