import math

def mutlak(bilangan):
    bilangan_mutlak = bilangan
    if bilangan<0:
        bilangan_mutlak = bilangan_mutlak * (-1)
    else:
        pass

    return bilangan_mutlak

def pembulatan(bilangan):
    hasil_pembulatan = math.floor(bilangan)
    if (bilangan-0.5) >= int(bilangan):
        hasil_pembulatan = math.ceil(bilangan)
    else:
        pass
    
    return hasil_pembulatan



x0 = int(input('x0: '))
y0 = int(input('y0: '))
x1 = int(input('x1: '))
y1 = int(input('y1: '))
print()

xasli = []
yasli = []
x = []
y = []

xasli.append(x0)
yasli.append(y0)
x.append(pembulatan(xasli[0]))
y.append(pembulatan(yasli[0]))

dx = x1-x0
dy = y1-y0

if mutlak(dx) > mutlak(dy):
    r = mutlak(dx)
else:
    r = mutlak(dy)

print('k      x        y      round(x),round(y)')
print(f'                            ({pembulatan(x[0])},{pembulatan(y[0])})')
xr = dx/r
yr = dy/r
xasli.append(xasli[0]+xr)
yasli.append(yasli[0]+yr)
x.append(pembulatan(xasli[1]))
y.append(pembulatan(yasli[1]))
print(f'0    {(xasli[1]):.2f}    {(yasli[1]):.2f}         ({x[1]},{y[1]})')

index = 1
while (xasli[index] != x1) and yasli[index] != y1:
    xasli.append(xasli[index]+xr)
    yasli.append(yasli[index]+yr)
    x.append(pembulatan(xasli[index+1]))
    y.append(pembulatan(yasli[index+1]))
    print(f'{index}    {(xasli[index+1]):.2f}    {(yasli[index+1]):.2f}         ({x[index+1]},{y[index+1]})')

    index += 1

import matplotlib.pyplot as plt
  
plt.plot(x, y, color='red', marker='o')
plt.title('Garis DDA', fontsize=14)
plt.grid(True)
plt.show()