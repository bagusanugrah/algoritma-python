#fungsi untuk mengubah string ke list integer
#inputan_string adalah string yang akan diproses
#pemisah adalah karakter yang memisahkan angka2 di dalam string
def stringKeListInteger(inputan_string, pemisah):
    '''list_penampung untuk menampung angka2 yang didapat dari string yang mana list ini akan menjadi keluaran fungsi'''
    list_penampung = []

    '''variabel string perangka untuk menampung sementara setiap angka yang dipisahkan oleh pemisah'''
    perangka = ''

    #perulangan untuk membaca setiap karakter dari string
    for i in range(len(inputan_string)):
        '''tampung karakter ke-i dari string ke dalam variabel perkarakter'''
        perkarakter = inputan_string[i]

        '''jika karakter ke-i bukan pemisah dan bukan karakter yang terakhir'''
        if (perkarakter != pemisah) and (i < len(inputan_string)-1):
            '''maka masukkan karakter ke-i ke dalam variabel perangka'''
            perangka = perangka + perkarakter
        #jika karakter ke-i adalah pemisah atau karakter yang terakhir
        else:
            #jika variabel perangka sudah terisi maka
            if perangka != '':
                '''jika karakter ke-i bukan pemisah dan karakter ke-i adalah karakter yang terakhir'''
                if (perkarakter != pemisah) and (i == len(inputan_string)-1):
                    '''maka masukkan karakter ke-i ke dalam variabel perangka'''
                    perangka = perangka + perkarakter
                    '''konversi isi variabel perangka dari string ke integer kemudian masukkan isinya ke list_penampung'''
                    list_penampung.append(int(perangka))
                    '''kosongkan isi dari variabel perangka'''
                    perangka = ''
                else:
                    '''jika karakter ke-i adalah pemisah atau bukan karakter yang terakhir'''
                    '''maka konversi isi variabel perangka dari string ke integer kemudian masukkan isinya ke list_penampung'''
                    list_penampung.append(int(perangka))
                    '''kosongkan isi dari variabel perangka'''
                    perangka = ''
    '''keluarkan list_penampung sebagai keluaran dari fungsi'''
    return list_penampung

#contoh penggunaan
# '''inputan harga saham dipisahkan oleh spasi dan merupakan string'''
# input_harga_saham = input('Masukkan harga saham (pisahkan dengan spasi): ')

# '''panggil fungsi stringKeListInteger menjadikan inputan harga saham yang string itu menjadi sebuah list yang berisikan angka2 yang sebelumnya dipisahkan oleh spasi'''
# list_harga_saham = stringKeListInteger(input_harga_saham, ' ')
# '''list untuk menampung nomor hari dari harga saham'''
# hari = []
# '''list untuk menampung profit2 yang didapat dari hasil harga saham hari ke-n dikurangi harga saham sebelum n'''
# list_profit = []

# '''lakukan perulangan sepanjang list_harga_saham'''
# for i in range(len(list_harga_saham)):
#     '''j adalah hari ke-n (pointer 2) sementara i adalah sebelum n (pointer 1)'''
#     j = i+1
#     '''lakukan perulangan dari harga saham ke-j hingga harga saham terakhir'''
#     while j<len(list_harga_saham):
#         '''profit adalah harga saham ke-j dikurangi harga saham ke-i'''
#         profit = list_harga_saham[j] - list_harga_saham[i]
#         '''masukkan profit ke list_profit'''
#         list_profit.append(profit)
#         '''tambahkan j dengan 1'''
#         j += 1
#     '''masukkan nomor2 hari ke list hari'''
#     hari.append(i)
# '''variabel maksimum_profit untuk menampung profit yang >0 dan terbesar'''
# maksimum_profit = 0

# '''baca setiap profit yang ada di dalam list_profit'''
# for profit in list_profit:
#     '''jika profit ke-n lebih besar dari maksimum_profit'''
#     if profit > maksimum_profit:
#         '''maka ganti nilai maksimum_profit dengan profit ke-n'''
#         maksimum_profit = profit
# #print maksimum profit
# print(f'Keuntungan maksimum yang bisa didapat adalah: {maksimum_profit}')

# #import pyplot dari matplotlib sebagai plt
# import matplotlib.pyplot as plt
# '''atur plot dengan list hari sebagai titik2 x dan list_harga_saham sebagai titik2 y'''
# plt.plot(hari, list_harga_saham, color='blue', marker='o')
# #buat label 'hari' pada sumbu x
# plt.xlabel("Hari")
# #buat label 'harga' pada sumbu y
# plt.ylabel("Harga")
# #beri judul grafik
# plt.title('Grafik Harga Saham dan Titik Pembelian/Penjualan', fontsize=14)
# plt.grid(True)
# #tampilkan grafik
# plt.show()
    