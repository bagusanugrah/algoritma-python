#import library csv
import csv  
#import pandas sebagai pd
import pandas as pd
#import fungsi sleep dari library time
from time import sleep

#fungsi untuk menuliskan data baru di csv
def create(csv_file, nama, gender, nohp):
    #untuk menampung id terbaru
    id_terbaru = ''
    #buka file csv dengan mode readonly
    with open(csv_file, 'r') as openedcsv:
        #baca setiap data di csv yang dipisahkan koma
        readcsv = csv.reader(openedcsv, delimiter=',')
        #lakukan perulangan untuk setiap row
        for row in readcsv:
            #jika csv sudah ada datanya
            if row[0] != 'id':
                '''inisialisasikan id_terbaru dengan nilai id dari row yang dibaca'''
                id_terbaru = row[0]
    
    #jika csv belum ada datanya
    if id_terbaru == '':
        #inisialisasi id_terbaru dengan 1
        id_terbaru = 1
    #jika csv sudah ada datanya
    else:
        #tambahkan id_terbaru dengan 1
        id_terbaru = int(id_terbaru)+1

    #jika argumen gender adalah 'l'
    if gender.lower() == 'l':
        #inisialisasikan gender dengan 'Laki-laki'
        gender = 'Laki-laki'
    #jika argumen gender bukan 'l'
    else:
        #inisialisasikan gender dengan 'Perempuan'
        gender = 'Perempuan'
    
    '''buat dictionary data_baru untuk menampung data baru yang akan dimasukkan ke csv'''
    data_baru = {'id': str(id_terbaru), 'nama': nama, 'jenis_kelamin': gender, 'nohp': nohp}

    #buka file csv dengan mode append
    with open(csv_file, 'a', newline='') as openedcsv:
        #siapkan alat untuk memasukkan data baru ke csv
        writer = csv.DictWriter(openedcsv, data_baru.keys())
        #masukkan data baru ke dalam csv
        writer.writerow(data_baru)
    #print ini
    print('Berhasil tambah data')
    #buat baris baru
    print()
    #jeda 2 detik
    sleep(2)



#fungsi untuk menampilkan semua data csv
def read(csv_file):
    #baca file csv menggunakan pandas
    df = pd.read_csv(csv_file)
    #print dataframe
    print(df)

#fungsi untuk mengupdate row di csv
def update(csv_file, id, nama, gender, nohp):
    #buka file csv dengan mode readonly
    with open(csv_file, 'r') as openedcsv:
        #baca setiap data di csv yang dipisahkan koma
        readcsv = csv.reader(openedcsv, delimiter=',')
        #masukkan semua row dari csv ke array rows
        rows = [row for row in readcsv]

        #jika argumen gender adalah 'l'
        if gender.lower() == 'l':
            #inisialisasikan gender dengan 'Laki-laki'
            gender = 'Laki-laki'
        #jika argumen gender bukan 'l'
        else:
            #inisialisasikan gender dengan 'Perempuan'
            gender = 'Perempuan'

        #sebagai status apakah id sudah ditemukan atau belum
        id_tidak_ada = True
        #lakukan perulangan untuk setiap elemen array rows
        for row in rows:
            #jika id ketemu
            if row[0] == id and row[0] != 'id':
                #ganti id_tidak_ada menjadi False
                id_tidak_ada = False
                #ganti data nama
                row[1] = nama
                #ganti data jenis_kelamin
                row[2] = gender
                #ganti data nohp
                row[3] = nohp
        
        #jika id tidak ditemukan
        if id_tidak_ada:
            #print ini
            print(f'Id pelanggan tidak ditemukan')
            #jeda 2 detik
            sleep(2)
            #kembalikan nilai False
            return False

    #buka file csv dengan mode write
    with open(csv_file, 'w', newline='') as openedcsv:
        #siapkan alat untuk replace data
        writer = csv.writer(openedcsv)
        #replace data lama data baru ke dalam csv
        writer.writerows(rows)
    
    #print ini
    print('Data berhasil diupdate')
    #buat baris baru
    print()
    #jeda 2 detik
    sleep(2)
    #kembalikan nilai True
    return True

#fungsi untuk delete row di csv
def delete(csv_file, id):
    #buka file csv dengan mode readonly
    with open(csv_file, 'r') as openedcsv:
        #baca setiap data di csv yang dipisahkan koma
        readcsv = csv.reader(openedcsv, delimiter=',')
        '''untuk menampung semua row dari csv kecuali data dengan id yang dipilih'''
        rows = []

        #sebagai status apakah id sudah ditemukan atau belum
        id_tidak_ada = True
        #lakukan perulangan untuk setiap row di csv
        for row in readcsv:
            #jika id ketemu
            if row[0] == id and row[0] != 'id':
                #ganti id_tidak_ada menjadi False
                id_tidak_ada = False
            #jika id yang dibaca bukanlah id yang diinputkan
            if row[0] != id:
                #tambahkan data row csv ke array rows
                rows.append(row)
                
        
        #jika id tidak ditemukan
        if id_tidak_ada:
            #print ini
            print(f'Id pelanggan tidak ditemukan')
            #jeda 2 detik
            sleep(2)
            #kembalikan nilai False
            return False

    #buka file csv dengan mode write
    with open(csv_file, 'w', newline='') as openedcsv:
        #siapkan alat untuk replace data
        writer = csv.writer(openedcsv)
        #replace data lama data baru ke dalam csv
        writer.writerows(rows)
    
    #print ini
    print('Data berhasil dihapus')
    #buat baris baru
    print()
    #jeda 2 detik
    sleep(2)
    #kembalikan nilai True
    return True

#fungsi program utama
def main():
    #path dari file csv
    path = 'data-pelanggan.csv'

    #loopingkan program utama terus menerus
    while True:
        '''jalankan fungsi read() dengan path sebagai file csv yang akan dibaca'''
        read(path)

        #buat baris baru
        print()
        #aksi masih belum dipilih
        aksi = ''
        #selagi aksi belum dipilih maka jalankan
        while aksi == '':
            #print aksi apa saja yang tersedia
            print('Aksi:')
            print('1. Tambah')
            print('2. Edit')
            print('3. Hapus')

            #input nomor aksi yang ingin dilakukan
            pilihan_aksi = input('Pilih aksi [1/2/3]: ')

            #jika nomor aksi yang diinput adalah 1/2/3
            if pilihan_aksi == '1' or pilihan_aksi == '2' or pilihan_aksi == '3':
                #maka aksi diisikan dengan nomor aksi dari inputan
                aksi = pilihan_aksi
            else:#jika inputan selain 1/2/3
                #printkan yang dibawah ini
                print('Inputan salah! Harusnya inputkan 1/2/3')
                #buat baris baru
                print()
                #jeda 2 detik
                sleep(2)

        #jika aksi yang dipilih adalah tambah
        if aksi == '1':
            #digunakan untuk menghentikan while
            inputan_salah = True

            #selagi inputan_salah masih True
            while inputan_salah:
                #buat baris baru
                print()
                #inputkan nama pelanggan
                nama_pelanggan = input('Nama Pelanggan: ')
                #inputkan jenis kelamin dengan huruf l atau p
                jenis_kelamin = input('Jenis Kelamin [L/P]: ')
                #inputkan nomor handphone
                no_hp = input('Nomor Handphone: ')

                #jika inputan jenis kelamin adalah l atau p
                if jenis_kelamin.lower() == 'l' or jenis_kelamin.lower() == 'p':
                    '''maka panggil fungsi create() untuk menuliskan data baru ke dalam csv'''
                    create(path, nama_pelanggan, jenis_kelamin, no_hp)
                    '''ganti nilai inputan_salah menjadi False agar looping while berhenti'''
                    inputan_salah = False
                #jika inputan jenis kelamin selain l atau p
                else:
                    #print ini
                    print('Inputan Jenis Kelamin salah! Harusnya inputkan L/P')
                    #jeda 2 detik
                    sleep(2)
        #jika aksi yang dipilih adalah edit
        elif aksi == '2':
            #untuk menghentikan while yang pertama
            id_ditemukan = False

            #selagi id belum ditemukan
            while not id_ditemukan:
                #digunakan untuk menghentikan while yang kedua
                inputan_salah = True

                #selagi inputan_salah masih True
                while inputan_salah:
                    #buat baris baru
                    print()
                    #inputkan id pelanggan
                    id_pelanggan = input('Id Pelanggan: ')
                    #inputkan nama pelanggan
                    nama_pelanggan = input('Nama Pelanggan: ')
                    #inputkan jenis kelamin dengan huruf l atau p
                    jenis_kelamin = input('Jenis Kelamin [L/P]: ')
                    #inputkan nomor handphone
                    no_hp = input('Nomor Handphone: ')

                    #jika inputan jenis kelamin adalah l atau p
                    if jenis_kelamin.lower() == 'l' or jenis_kelamin.lower() == 'p':
                        '''panggil fungsi update() untuk replace data lama dengan data baru ke dalam csv'''
                        id_ditemukan = update(path, id_pelanggan, nama_pelanggan, jenis_kelamin, no_hp)
                        '''ganti nilai inputan_salah menjadi False agar looping while berhenti'''
                        inputan_salah = False
                    #jika inputan jenis kelamin selain l atau p
                    else:
                        #print ini
                        print('Inputan Jenis Kelamin salah! Harusnya inputkan L/P')
                        #jeda 2 detik
                        sleep(2)
        else:#jika aksi yang dipilih adalah hapus
            #untuk menghentikan while
            id_ditemukan = False

            #selagi id belum ditemukan
            while not id_ditemukan:
                #buat baris baru
                print()
                #inputkan id pelanggan
                id_pelanggan = input('Id Pelanggan: ')
                '''panggil fungsi delete() untuk menghapus row di csv dengan id tertentu'''
                id_ditemukan = delete(path, id_pelanggan)

main()
