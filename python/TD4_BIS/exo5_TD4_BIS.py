def f2(x):
    return (x + 1)

def f3(x, f):
    return (f(x) * 2)

res_f3 = f3(4, f2)

print(res_f3)