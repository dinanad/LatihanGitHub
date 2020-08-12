## Aplikasi membuat segitiga

Exit = False #check keluar dari aplikasi
while Exit == False :

    
    check = False #check keluar dari menu utama
    while check == False: 
        # menu utama
        print('--------------------------')
        menu = input("Pilih Menu \n 1. Segitiga Siku-Siku \n 2. Segitiga Sama Kaki \n 3. Persegi \n Pilih menu nomor : ")
        # untuk proses validasi input hanya string angka 
        if menu.isdigit() == True :
            if int(menu) > 0 and int(menu) <= 3: # validasi input hanya 1-3
                check = True #masuk ke rangkaian while, jika true masuk ke menu yng dipilih 1-3
                #ke menu selanjutnya
                print('--------------------------')
            else :
                print('Input salah, masukkan pilihan 1-3')
                print('---------------------')
        else :
            print('Input salah, masukkan angka hanya 1-3')
            print('-------------------------')
    
    ## Proses bila menu 1 yang terpilih
    if menu == '1':
        # Pemilihan menu belanja dan check hanya angka sesuai dengan yang ada di menu
        check = False #check keluar dari menu utama 1
        while check == False :
            menuSiku = input("Pilih Menu Segitiga Siku-Siku \n 1. Segitiga Siku Atas \n 2. Segitiga Siku Bawah \n Pilih menu Segitiga Siku-Siku : ")
            # Validasi input string hanya berupa angka
            if menuSiku.isdigit() == True :
                if int(menuSiku) > 0 and int(menuSiku) <=2: #validasi input hanya 1-3
                    check = True #exit way untuk ke proses menu selanjutnya
                else :
                    print('Input salah, masukkan angka hanya 1-2')
                    print('------------------------')
            else :
                print('Input salah, masukkan angka hanya 1-2')
                print('-----------------------')
        

        if menuSiku == '1' :
            check = False #check keluar dari menu siku atas
            while(check==False):
                ## Segitiga Siku2 atas
                print ('\nSEGITIGA SIKU-SIKU ATAS')
                segitiga_sa = ''
                a = input("\nMasukkan panjang ruas siku atas (1-10) : ")

                if a.isdigit() == True : #validasi nilai yang dimasukkan berupa string angka
                    if int(a) > 0 and int(a) <=10: #validasi nilai yang dimasukkan 1-10
                        check = True #exit way untuk ke proses selanjutnya
                    else :
                        print('Input salah, masukkan angka hanya 1-10')
                        print('------------------------')
                else :
                    print('Input salah, masukkan angka hanya 1-10')
                    print('------------------------')
            ## Segitiga Siku2 atas
            for x in range(int(a),0,-1):
                for y in range (0,x):
                    segitiga_sa += '*'
                segitiga_sa += '\n'
            print(segitiga_sa)

        else :
            check = False
            while (check==False):
                ##Segitiga Siku2 bawah
                print ('\nSEGITIGA SIKU-SIKU BAWAH')
                segitiga_sb = ''
                b = input("Masukkan panjang ruas siku bawah (1-10) : ")

                if b.isdigit() == True : #validasi input string berupa angka
                    if int(b) > 0 and int(b) <=10:
                        check = True #exit way untuk ke proses selanjutnya
                    else :
                        print('Input salah, masukkan angka hanya 1-10')
                        print('-----------------------')
                else :
                    print('Input salah, masukkan angka hanya 1-10')
                    print('-----------------------')
            ##Segitiga Siku2 bawah
            for x in range(int(b)):
                for y in range (0,x+1):
                    segitiga_sb += '*'
                segitiga_sb += '\n'
            print(segitiga_sb)

        check = False
        while check == False :
            #Pilihan ke menu awal/exit
            ask1 = input('\nPilih menu \n 1. Menu awal \n 2. Exit Rp.\n Pilih Nomor : ')
            if (ask1.isdigit() == True) :
                if int(ask1) > 0 and int(ask1) <=3:
                    check = True
                else :
                    print('Input salah, masukkan angka hanya 1-3')
                    print('------------------------')
                        
            else :
                print('Input salah, masukkan angka hanya 1-3')
                print('-----------------------')
            if(ask1=='2'):
                Exit= True

    elif menu == '2':
        check = False
        while check == False :
            print('SEGITIGA SAMA KAKI')
            segitiga_k = ''
            k = input("Masukkan panjang ruas segitiga sama kaki (1-10) : ")
            spasi = int(k)

            if k.isdigit() == True : #validasi input berupa string angka
                if int(k) > 0 and int(k) <=10: #validasi input 1-10
                    check = True #exit way untuk ke proses selanjutnya
                else :
                    print('Input salah, masukkan angka hanya 1-10')
                    print('------------------------')
            else :
                print('Input salah, masukkan angka hanya 1-10')
                print('------------------------')

        ##Segitiga sama sisi
        #Looping Baris
        while spasi >= 0:
                
            #Looping kolom kosong (spasi)
            kolom = spasi
            while kolom > 0:
                segitiga_k = segitiga_k + '   '
                kolom = kolom - 1

            #Looping kolom bintang sisi kiri
            kiri = 1
            while kiri < (int(k)-(spasi-1)) :
                segitiga_k = segitiga_k + ' * '
                kiri = kiri + 1
                    
            #Looping kolom bintang sisi kanan
            kanan = 1
            while kanan < kiri - 1 :
                segitiga_k = segitiga_k + ' *  '
                kanan = kanan + 1
                    
            segitiga_k = segitiga_k + '\n'
            spasi = spasi - 1

        print(segitiga_k)

        check = False
        while check == False :
            #Pilihan ke menu awal/exit
            ask2 = input('\nPilih menu \n 1. Menu awal \n 2. Exit Rp.\n Pilih Nomor : ')
            if (ask2.isdigit() == True) :
                if int(ask2) > 0 and int(ask2) <=3:
                    check = True
                else :
                    print('Input salah, masukkan angka hanya 1-2')
                    print('------------------------')
                        
            else :
                print('Input salah, masukkan angka hanya 1-2')
                print('-----------------------')
            if(ask2=='2'):
                Exit= True


    else :
        check = False
        while(check==False):
            
            #PERSEGI PANJANG
            print ('\nPERSEGI PANJANG')
            persegi=''
            p = input("Masukkan panjang ruas persegi (1-10) : ")
            l = input("Masukkan lebar ruas persegi (1-10) : ")
            if p.isdigit() == True :
                if l.isdigit() == True :
                    if int(p) > 0 and int(p) <=10:
                        if int(l) > 0 and int(l) <=10:
                            check = True #exit way untuk ke proses selanjutnya
                        else :
                            print('Input panjang atau lebar ruas persegi salah, masukkan angka hanya 1-10') #validasi angka yg dimasukkan 1-10
                            print('------------------------')
                    else :
                        print('Input panjang atau lebar ruas persegi salah, masukkan angka hanya 1-10') #validasi angka yg dimasukkan 1-10
                        print('------------------------')
                else :
                    print('Input panjang atau lebar ruas persegi salah, masukkan angka hanya 1-10') #validasi string berupa angka
                    print('------------------------')
            else :
                print('Input panjang atau ruas persegi salah, masukkan angka hanya 1-10') #validasi string berupa angka
                print('------------------------')
        #Persegi panjang
        for x in range (int(l)):
            for y in range (int(p)):
                persegi += '*'
            persegi += '\n'
        print(persegi)

        
        check = False
        while check == False :
            #Pilihan ke menu awal/exit
            ask3 = input('\nPilih menu \n 1. Menu awal \n 2. Exit Rp.\n Pilih Nomor : ')
            if (ask3.isdigit() == True) :
                if int(ask3) > 0 and int(ask3) <3:
                    check = True
                else :
                    print('Input salah, masukkan angka hanya 1-2')
                    print('------------------------')
            else :
                print('Input salah, masukkan angka hanya 1-2')
                print('-----------------------')
            if(ask3=='2'):
                Exit= True

else :
    Exit = True
print('Terima kasih sudah menggunakan aplikasi segitiga\n\n')

