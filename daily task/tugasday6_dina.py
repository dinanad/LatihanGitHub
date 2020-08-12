# # Menu
# #  1) Show Produk
# #  2) Tambahkan Produk
# #  3) Update Harga
# #  4) Hapus Produk

nama = ['Jeruk', 'Kiwi', 'Apel']
harga = [1000,2000,3000]

### Function u/ menampilkan list produk
def show_produk():
    daftar_produk=''
    print('\nDaftar produk :')
    for item in range (len(nama)):
        daftar_produk += str(item+1) + '. ' + nama[item] + ' Rp.' + str(harga[item]) + '\n'
    return daftar_produk

# # ### Function u/ menambahkan list produk (nama & harga)
# def tambah_produk (add_nama, add_harga): #gagal menggunakan function
#     nama.append(add_nama)
#     nama.append(add_harga)
#     return nama, harga

### Function u/menampilkan list produk
def update_harga (urutan, up_harga):
    harga.pop(urutan-1)
    harga.insert(urutan-1,up_harga)
    return harga

### Function u/ nmenghapus  list produk
def hapus_produk (hapus):
    nama.pop(hapus-1)
    harga.pop(hapus-1)
    return nama, harga



check = False #check keluar dari menu utama
while check == False: 
    # menu utama
    print('--------------------------\n')
    menu = input('Menu : \n 1) Show Produk\n 2) Tambahkan Produk\n 3) Update Harga\n 4) Hapus Produk\n\n Pilih Menu Nomor : ')
    
    ## show produk
    if menu == '1':
        print(show_produk())

    ## tambah produk
    elif menu == '2':
        add_nama = input('\nMasukkan produk baru : ')
        add_harga = input('Masukkan harga baru : ')
        # tambah_produk(add_nama, add_harga) #function blm berhasil
        nama.append(add_nama)
        harga.append(add_harga)
    
    ## update harga
    elif menu == '3':
        print(show_produk()) 
        urutan = int(input('Pilih produk yang akan diupdate harganya : '))
        up_harga = input('Masukkan harga produk yang akan diupdate harganya : ')
        update_harga(urutan, up_harga)   

    ## hapus produk
    elif menu == '4':
        print(show_produk()) 
        hapus = int(input('Pilih produk yang akan dihapus dari daftar: '))
        hapus_produk(hapus-1) 


else :
    Exit = True

