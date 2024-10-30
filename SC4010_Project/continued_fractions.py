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