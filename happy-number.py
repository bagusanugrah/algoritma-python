'''
Soal
Buatlah program yang menerima inputan n, 
yang apabila jumlah dari angka penyusun n yang dikuadratkan adalah 1
maka n adalah happy number, namun jika jumlah dari angka penyusun n yang dikuadratkan adalah n
maka n bukan happy number. Berikut ini adalah gambaran detailnya:

n = 4 
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4

4 bukan happy number


n = 19
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

19 adalah happy number
'''

list_hasil =  []

n = int(input('n = '))

target_split = [n]
list_hasil.append(n)

count = 0
while list_hasil[len(list_hasil)-1] != 1:
    jumlah = 0
    list_perangka = list(map(int, str(target_split[0])))
    
    if count!=0 and  list_hasil[len(list_hasil)-1] == n:
        break

    for i in range(len(list_perangka)):
        jumlah = jumlah + list_perangka[i]**2
        print(f'{list_perangka[i]}^2 ', end='')
        if i<len(list_perangka)-1:
            print('+ ', end='')
        else:
            print('= ', end='')
    print(jumlah)

    
    list_hasil.append(jumlah)
    target_split = [jumlah]
    count+=1

print()
if list_hasil[len(list_hasil)-1] == 1:
    print(f'{n} adalah happy number')
else:
    print(f'{n} bukan happy number')


