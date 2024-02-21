R = [188, 145, 208, 251, 242, 164, 187, 240, 141]
G = [161, 202, 234, 246, 209, 135, 164, 240, 211]
B = [132, 215, 243, 241, 213, 107, 138, 244, 219]
gArray = []
binerArray = []
pencahayaanArray = []


#konversi ke GRAYSCALE
print('Operasi GRAYSCALE')
index = 0
for baris in range(3):
    for kolom in range(3):
        grayscale = round(0.299*R[index] + 0.587*G[index] + 0.114*B[index], 3)
        gArray.append(grayscale)
        print(f'0.299({R[index]}) + 0.587({G[index]}) + 0.114({B[index]}) = {grayscale}  #  ', end='')
        index += 1
    print()
    for i in range(3):
        for j in range(51):
            print('-', end='')
    print()

print()
#print GRAYSCALE
print('GRAYSCALE')
index = 0
for baris in range(3):
    for kolom in range(3):
        print(f'{gArray[index]} # ', end='')
        index += 1
    print()

print()
#konversi ke BINER
print('Masukkan nilai T')
T = int(input('T = '))
print()
print('BINER')
index = 0
for baris in range(3):
    for kolom in range(3):
        if gArray[index]<T:
            binerArray.append(0)
            print(f'{binerArray[index]} # ', end='')
        else:
            binerArray.append(1)
            print(f'{binerArray[index]} # ', end='')
        index += 1
    print()

print()
#pencahayaan citra
print('Masukkan nilai b')
b = int(input('b = '))
print()
print('BINER')
index = 0
for baris in range(3):
    for kolom in range(3):
        pencahayaan = round(gArray[index] + b)
        if pencahayaan<0:
            pencahayaanArray.append(0)
            print(f'{pencahayaanArray[index]} # ', end='')
        elif pencahayaan>255:
            pencahayaanArray.append(255)
            print(f'{pencahayaanArray[index]} # ', end='')
        else:
            pencahayaanArray.append(pencahayaan)
            print(f'{pencahayaanArray[index]} # ', end='')
        index += 1
    print()