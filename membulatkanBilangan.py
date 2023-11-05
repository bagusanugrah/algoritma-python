import math

def pembulatan(bilangan):
    hasil_pembulatan = math.floor(bilangan)
    if (bilangan-0.5) >= int(bilangan):
        hasil_pembulatan = math.ceil(bilangan)
    else:
        pass
    
    return hasil_pembulatan

#contoh penggunaan
# a = 12.4
# b = 12.5
# c = 12.6

# print(f'Hasil pembulatan dari {a} adalah {pembulatan(a)}')
# print(f'Hasil pembulatan dari {b} adalah {pembulatan(b)}')
# print(f'Hasil pembulatan dari {c} adalah {pembulatan(c)}')