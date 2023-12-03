import mysql.connector
from time import sleep

#konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'pemdas_prak'
}

#fungsi untuk mengecek id apakah ada atau tidak
def cariID(con, inputan_id):
    #konversi id jadi integer
    inputan_id = int(inputan_id)
    #membuat cursor untuk berinteraksi dengan database
    cursor = con.cursor()
    #query sql untuk membaca id dari masing-masing row
    select_query = 'SELECT id FROM barang'

    #jalankan query
    cursor.execute(select_query)

    #simpan semua id ke dalam variabel ids
    ids = cursor.fetchall()

    id_ketemu = False
    #baca setiap id
    for id in ids:
        #jika id yang diinputkan user ada di database
        if id == (inputan_id,):
            id_ketemu = True

    #jika id ketemu
    if id_ketemu:
        #kembalikan nilai True
        return True
    #jika tidak
    else:
        #kembalikan nilai False
        return False

#fungsi untuk memasukkan data baru ke dalam database
def create(con, inputan_nama, inputan_stok, inputan_harga):
    #membuat cursor untuk berinteraksi dengan database
    cursor = con.cursor()
    #query sql untuk insert data ke database
    insert_query = 'INSERT INTO barang (nama_barang, stok, harga) VALUES (%s, %s, %s)'

    #data yang akan dimasukkan ke database
    value = (inputan_nama, inputan_stok, inputan_harga)

    #masukkan data ke database
    cursor.execute(insert_query, value)

    #simpan perubahan
    con.commit()

    #print ini
    print('Berhasil tambahkan barang.')
    #jeda 2 detik
    sleep(2)

#fungsi untuk membaca semua data di database
def read(con):
    #membuat cursor untuk berinteraksi dengan database
    cursor = con.cursor()
    #query sql untuk membaca data dari database
    select_query = 'SELECT * FROM barang'

    #jalankan query
    cursor.execute(select_query)

    #simpan semua data ke dalam variabel rows
    rows = cursor.fetchall()

    print('no (id, nama_barang, stok, harga)')
    #print semua row
    for i in range(len(rows)):
        print(f'{i+1} {rows[i]}')

#fungsi untuk update data di database
def update(con, id, inputan_nama, inputan_stok, inputan_harga):
    #membuat cursor untuk berinteraksi dengan database
    cursor = con.cursor()
    #query sql untuk update data
    update_query = 'UPDATE barang SET nama_barang=%s, stok=%s, harga=%s WHERE id=%s'

    #data yang akan dimasukkan ke database
    value = (inputan_nama, inputan_stok, inputan_harga, id)

    #ubah data
    cursor.execute(update_query, value)

    #simpan perubahan
    con.commit()

    #print ini
    print('Berhasil update barang.')
    #jeda 2 detik
    sleep(2)

#fungsi untuk hapus data di database
def delete(con, id):
    #membuat cursor untuk berinteraksi dengan database
    cursor = con.cursor()
    #query sql untuk hapus data
    delete_query = 'DELETE FROM barang WHERE id=%s'

    #id dari data yang akan dihapus
    value = (id,)

    #hapus data
    cursor.execute(delete_query, value)

    #simpan perubahan
    con.commit()

    #print ini
    print('Berhasil hapus barang.')
    #jeda 2 detik
    sleep(2)

#fungsi program utama
def main(con):
    #untuk menghentikan while
    program_berjalan = True

    #selagi program_berjalan bernilai True
    while program_berjalan:
        #buat baris baru
        print()
        #jalankan fungsi read()
        read(con)

        #buat baris baru
        print()
        #print daftar aksi yang bisa dilakukan
        print('Aksi:')
        print('1. Tambah Barang')
        print('2. Update Barang')
        print('3. Hapus Barang')
        print('4. Hentikan Program')
        #aksi yang dipilih
        aksi_dipilih = input('Pilih aksi [1-4]: ')

        #jika aksi yang dipilih adalah tambah barang
        if aksi_dipilih == '1':
            #untuk menghentikan while
            inputan_kosong = True

            #selagi ada inputan yang kosong
            while inputan_kosong:
                #buat baris baru
                print()
                #print ini
                print('Tambah Barang')
                #inputan nama barang
                nama_barang = input('Nama Barang: ')
                #inputan stok barang
                stok = input('Stok Barang: ')
                #inputan harga barang
                harga = input('Harga Barang: ')

                #jika ada inputan yang tidak diisi
                if nama_barang=='' or stok=='' or harga=='':
                    #print ini
                    print('Inputan tidak boleh ada yang kosong!')
                    #jeda 2 detik
                    sleep(2)
                #jika inputan diisi semua
                else:
                    try:
                        #konversi stok menjadi integer
                        stok = int(stok)
                        #konversi harga menjadi integer
                        harga = int(harga)
                        #jalankan fungsi create()
                        create(con, nama_barang, stok, harga)
                        #hentikan while
                        inputan_kosong = False
                    #jika stok atau harga bukan integer
                    except:
                        #print ini
                        print('Inputan stok dan harga harus berupa integer!')
                        #jeda 2 detik
                        sleep(2)

        #jika aksi yang dipilih adalah update barang
        elif aksi_dipilih == '2':
            #untuk menghentikan while pertama
            inputan_kosong = True

            #selagi ada inputan yang kosong
            while inputan_kosong:
                #untuk menghentikan while kedua
                id_ketemu = False

                #selagi id belum ketemu
                while not id_ketemu:
                    #buat baris baru
                    print()
                    #print ini
                    print('Update Barang')
                    #inputan id barang
                    id_barang = input('Id Barang: ')
                    #inputan nama barang
                    nama_barang = input('Nama Barang: ')
                    #inputan stok barang
                    stok = input('Stok Barang: ')
                    #inputan harga barang
                    harga = input('Harga Barang: ')

                    try:
                        #konversi id_barang menjadi integer
                        id_barang = int(id_barang)
                        #jika id ketemu
                        if cariID(con, id_barang):
                            #jika ada inputan yang tidak diisi
                            if nama_barang=='' or stok=='' or harga=='':
                                #print ini
                                print('Inputan tidak boleh ada yang kosong!')
                                #jeda 2 detik
                                sleep(2)
                            #jika inputan diisi semua
                            else:
                                try:
                                    #konversi stok menjadi integer
                                    stok = int(stok)
                                    #konversi harga menjadi integer
                                    harga = int(harga)
                                    #jalankan fungsi update()
                                    update(con, id_barang, nama_barang, stok, harga)
                                    #hentikan while pertama
                                    inputan_kosong = False
                                #jika stok atau harga bukan integer
                                except:
                                    #print ini
                                    print('Inputan stok dan harga harus berupa integer!')
                                    #jeda 2 detik
                                    sleep(2)
                            #hentikan while kedua
                            id_ketemu = True
                        #Jika id tidak ketemu
                        else:
                            #print ini
                            print(f'Tidak ada barang dengan id={id_barang}!')
                            #jeda 2 detik
                            sleep(2)
                    #jika id_barang bukan integer
                    except:
                        #print ini
                        print('Inputan id harus berupa integer!')
                        #jeda 2 detik
                        sleep(2)

        #jika aksi yang dipilih adalah hapus barang
        elif aksi_dipilih == '3':
            #untuk menghentikan while
            id_ketemu = False
            #selagi id belum ketemu
            while not id_ketemu:
                #buat baris baru
                print()
                #print ini
                print('Hapus Barang')
                #inputan id barang
                id_barang = input('Id Barang: ')
                
                try:
                    #konversi id_barang menjadi integer
                    id_barang = int(id_barang)
                    #jika id ketemu
                    if cariID(con, id_barang):
                        #jalankan fungsi delete()
                        delete(con, id_barang)
                        #hentikan while
                        id_ketemu = True
                    #Jika id tidak ketemu
                    else:
                        #print ini
                        print(f'Tidak ada barang dengan id={id_barang}!')
                        #jeda 2 detik
                        sleep(2)
                #jika id_barang bukan integer
                except:
                    #print ini
                    print('Inputan id harus berupa integer!')
                    #jeda 2 detik
                    sleep(2)
            
        #jika aksi yang dipilih adalah hentikan program
        elif aksi_dipilih == '4':
            #hentikan while
            program_berjalan = False
        #jika aksi yang dipilih selain 1/2/3/4
        else:
            #print ini
            print('Inputan aksi salah! Masukkan angka 1/2/3/4')
            #jeda 2 detik
            sleep(2)

try:
    #membuat koneksi dengan database
    connection = mysql.connector.connect(**db_config)

    #jika berhasil terhubung dengan database
    if connection.is_connected():
        #jalankan program utama
        main(connection)
#jika gagal terhubung dengan database
except mysql.connector.Error as e:
    #print error message
    print(f'Error connecting to mysql: {e}')
#jika semua kodingan try sudah dijalankan dan tidak ada error
finally:
    #jika sudah terhubung dengan database
    if 'connection' in locals() and connection.is_connected():
        #tutup koneksi
        connection.close()
        #print ini
        print('Connection closed')