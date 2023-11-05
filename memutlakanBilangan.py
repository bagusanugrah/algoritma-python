def mutlak(bilangan):
    bilangan_mutlak = bilangan
    if bilangan<0:
        bilangan_mutlak = bilangan_mutlak * (-1)
    else:
        pass

    return bilangan_mutlak

#contoh penggunaan
# a = 15
# b = -15
# print(f'|{a}| = {mutlak(a)}')
# print(f'|{b}| = {mutlak(b)}')
