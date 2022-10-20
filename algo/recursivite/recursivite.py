import sys


def factorial(n):
    if n <= 1:
        return 1

    f = n * factorial(n-1)
    return f

def fibonacci(n):
    if n < 0:
        return 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_term(Unow, Ubefore, n):
    if n == 0:
        return Ubefore
    else :
        return fibonacci_term(Unow+Ubefore, Unow, n-1)

def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

def pgcd(a, b):
    reste = a%b

    if reste == 0:
        return b

    return pgcd(b, reste)

def decomp(n, k_max=-1):
    if k_max == -1 :
        k_max = int(n**0.5)
    if n == k_max**2 :
        return [k_max]

    for k in range(k_max, 0, -1):
        new_n = n - k**2
        decomp_par = decomp(new_n, min(k-1, int(new_n**0.5))) #min pour éviter les cas pourris quand k est le plus petits
        if len (decomp_par) > 0:
            return decomp_par + [k]
    return []




if __name__ == '__main__':
    #print(factorial(10))
    #print(fibonacci_term(1, 0, 92))
    #print(ack(2,2)+1)
    #print(pgcd(477865542, 717173730))
    print(decomp(8855))
    sys.exit()


