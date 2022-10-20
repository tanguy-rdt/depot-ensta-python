import math

# question 1
import time


# # question 2
# def sont_proche(x, y):
#     atol = 10 ** -5
#     rtol = 10 ** -8
#
#     calc1 = abs(x - y)
#     calc2 = atol + abs(y) * rtol
#
#     if calc1 <= calc2:
#         print(calc1, "<=", calc2)
#         return True
#     else:
#         print(calc1, "=>", calc2)
#         return False
#
#
# print(sont_proche(2, 2))
#
#
# # question 3 --> on doit obtenir 3 comme c'est une fonction récursive ont fait 1+1+1+0
# def mystere(x, b):
#     if x < b:
#         return 0
#     else:
#         return 1 + mystere(x / b, b)
#
#
# print(mystere(1001, 10))
#
# # question 4
# # ln(1001) en base 10
# print(math.log(1001, 10))
#
#
# question 8
def erato_iter(N):
    if N < 1:
        return 0

    list_bool = [True] * N
    list_bool[0] = False

    for i in range(2, int(math.sqrt(N) + 1)):
        if list_bool[i - 1] is not False:
            for j in range(len(list_bool)):
                if j % i == 0 and j != i:
                    list_bool[j - 1] = False

    return list_bool


print(erato_iter(20))
#
#
# question 12
def bbs(N):
    # cherche un nombre aléatoire entre 0 et 2**(N-1)
    p1 = 24375763
    p2 = 28972763

    M = p1 * p2
    xi = time.time()*12
    xi = int((xi - int(xi)) * 1e7)
    A = 0

    for i in range(N):
        if xi % 2:
            A = A + 2 ** i
            xi = (xi ** 2) % M

    return A


# question 13
# def premier_rapide(n_max):
#     N = math.ceil(math.log(n_max))
#     random_number = bbs(N)
#
#     if random_number != 0 and random_number < n_max:
#         return random_number
#     else:
#         return premier_rapide(n_max)


# # question 13 avec récursivité, fonctionne uniquement avec un grand n_max
# def premier_rapide(n_max):
#     N = math.ceil(math.log(n_max, 2))
#     p = bbs(N)
#
#     if p == 0 or p >= n_max or not((2**(p-1))%p == 1 and (3**(p-1))%p == 1 and (5**(p-1))%p == 1
#                                  and (7**(p-1))%p == 1):
#         return premier_rapide(n_max)
#     else:
#         return p
#
# print(premier_rapide(100))

# question 13
def premier_rapide(n_max):
    N = math.ceil(math.log(n_max, 2))
    p = bbs(N)


    while p == 0 or p >= n_max or (not(pow(2, p-1, p)) == 1 and not(pow(3, p-1, p)) == 1
                                   and not(pow(5, p-1, p)) == 1 and not(pow(7, p-1, p)) == 1):
        p = bbs(N)

    return p

print(premier_rapide(6))

#question14
def etat_bbs_fermat(N, nb):
    tab_prime_true = erato_iter(N)
    res_prime_true = []
    res_prime_false = []

    for i in range(nb):
        p = premier_rapide(N)
        if tab_prime_true[p-1]:
            res_prime_true.append(p)
        else :
            res_prime_false.append(p)

        time.sleep(0.015) #gros souci avec la graine dans bbs

    return [res_prime_true, res_prime_false, len(res_prime_false)/nb]

prime_true, prime_false, err = etat_bbs_fermat(100, 50)

print("taux relatif d'erreur: %s \n avec comme nombre premier vrais : %s \n et comme nombre"
      "premier faux : %s" %(err, prime_true, prime_false))



