import number_theory, continued_fractions

def wiener_attack(e, n):

    _, convergents = continued_fractions.form_continued_fractions(e, n)

    for (k, d) in convergents:

        if k != 0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi +1
            disc = s*s - 4*n
            if(disc>=0):
                t = number_theory.is_perf_sq(disc)
                if t!=-1 and (s+t)%2==0:
                    print("Wiener Attack Succesful")
                    return d
    return "Decryption Exponent Not Found"
    