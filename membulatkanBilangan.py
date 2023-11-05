#menggunakan Python 3.11.4
#jika tidak berfungsi sebagaimana mestinya, berarti pythonnya beda versi
import math

def limaAngkaDibelakangKoma(bilangan):
    bilangan = float(f'{bilangan:.6f}')
    bulat_kebawah = float(f'{bilangan:.5f}')
    hasil_pembulatan = round(bilangan, 5)
    if (bilangan-0.000004) >= bulat_kebawah:
        hasil_pembulatan = round(bilangan+0.000001, 5)
    else:
        pass
    return hasil_pembulatan

def empatAngkaDibelakangKoma(bilangan):
    bilangan = float(f'{bilangan:.5f}')
    bulat_kebawah = float(f'{bilangan:.4f}')
    hasil_pembulatan = round(bilangan, 4)
    if (bilangan-0.00004) >= bulat_kebawah:
        hasil_pembulatan = round(bilangan+0.00001, 4)
    else:
        pass
    return hasil_pembulatan

def tigaAngkaDibelakangKoma(bilangan):
    bilangan = float(f'{bilangan:.4f}')
    bulat_kebawah = float(f'{bilangan:.3f}')
    hasil_pembulatan = round(bilangan, 3)
    if (bilangan-0.0004) >= bulat_kebawah:
        hasil_pembulatan = round(bilangan+0.0001, 3)
    else:
        pass
    return hasil_pembulatan

def duaAngkaDibelakangKoma(bilangan):
    bilangan = float(f'{bilangan:.3f}')
    bulat_kebawah = float(f'{bilangan:.2f}')
    hasil_pembulatan = round(bilangan, 2)
    if (bilangan-0.004) >= bulat_kebawah:
        hasil_pembulatan = round(bilangan+0.001, 2)
    else:
        pass
    return hasil_pembulatan

def satuAngkaDibelakangKoma(bilangan):
    bilangan = float(f'{bilangan:.2f}')
    bulat_kebawah = float(f'{bilangan:.1f}')
    hasil_pembulatan = round(bilangan, 1)
    if (bilangan-0.04) >= bulat_kebawah:
        hasil_pembulatan = round(bilangan+0.01, 1)
    else:
        pass
    return hasil_pembulatan

def pembulatan(bilangan):
    bilangan = satuAngkaDibelakangKoma(bilangan)
    hasil_pembulatan = math.floor(bilangan)
    if (bilangan-0.5) >= int(bilangan):
        hasil_pembulatan = math.ceil(bilangan)
    else:
        pass
    
    return hasil_pembulatan

#contoh penggunaan
a = 12.445467
print(f'Hasil pembulatan dari {a} adalah {limaAngkaDibelakangKoma(a)}')
a = limaAngkaDibelakangKoma(a)
print(f'Hasil pembulatan dari {a} adalah {empatAngkaDibelakangKoma(a)}')
a = empatAngkaDibelakangKoma(a)
print(f'Hasil pembulatan dari {a} adalah {tigaAngkaDibelakangKoma(a)}')
a = tigaAngkaDibelakangKoma(a)
print(f'Hasil pembulatan dari {a} adalah {duaAngkaDibelakangKoma(a)}')
a = duaAngkaDibelakangKoma(a)
print(f'Hasil pembulatan dari {a} adalah {satuAngkaDibelakangKoma(a)}')
a = satuAngkaDibelakangKoma(a)
print(f'Hasil pembulatan dari {a} adalah {pembulatan(a)}')