import membulatkanBilangan as blt
#library membulatkanBilangan bisa didapat di https://github.com/bagusanugrah/algoritma-python/blob/main/membulatkanBilangan.py

def mutlak(bilangan):
    bilangan_mutlak = bilangan
    if bilangan<0:
        bilangan_mutlak = bilangan_mutlak * (-1)
    else:
        pass

    return bilangan_mutlak

x0 = int(input('x0: '))
y0 = int(input('y0: '))
x1 = int(input('x1: '))
y1 = int(input('y1: '))
print()

xasli = []
yasli = []
x = []
y = []

xasli.append(blt.duaAngkaDibelakangKoma(x0))
yasli.append(blt.duaAngkaDibelakangKoma(y0))
x.append(blt.pembulatan(xasli[0]))
y.append(blt.pembulatan(yasli[0]))

dx = x1-x0
dy = y1-y0

if mutlak(dx) > mutlak(dy):
    r = mutlak(dx)
else:
    r = mutlak(dy)

print('k      x        y      round(x),round(y)')
print(f'                            ({x[0]},{y[0]})')
xr = dx/r
yr = dy/r
xasli.append(blt.duaAngkaDibelakangKoma(xasli[0]+xr))
yasli.append(blt.duaAngkaDibelakangKoma(yasli[0]+yr))
x.append(blt.pembulatan(xasli[1]))
y.append(blt.pembulatan(yasli[1]))
print(f'0    {(xasli[1]):.2f}    {(yasli[1]):.2f}         ({x[1]},{y[1]})')

index = 1
while (xasli[index] != x1) and yasli[index] != y1:
    xasli.append(blt.duaAngkaDibelakangKoma(xasli[index]+xr))
    yasli.append(blt.duaAngkaDibelakangKoma(yasli[index]+yr))
    x.append(blt.pembulatan(xasli[index+1]))
    y.append(blt.pembulatan(yasli[index+1]))
    print(f'{index}    {(xasli[index+1]):.2f}    {(yasli[index+1]):.2f}         ({x[index+1]},{y[index+1]})')

    index += 1

import matplotlib.pyplot as plt
  
plt.plot(x, y, color='red', marker='o')
plt.title('Garis DDA', fontsize=14)
plt.grid(True)
plt.show()