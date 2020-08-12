#Variabel
#nama = 'Andi'
#print(nama)
#usia = 22
#usia = 32
#print(usia)
# jomblo = True
# print(jomblo)

#Data Type
#nama = 'Andi'
#usia = 22
#jomblo = True
#print(type(nama))
#print(type(usia))
#print(type(jomblo))

#Input
#nama = input("Whats your name? : ")
#print(nama)

#Solved It1
#nama = input("Nama kamu? : ")
#umur = input("Umur kamu? : ")
#jenis_k = input("Jenis kelamin kamu? : ")
#pekerjaan = input("Pekerjaan kamu? : ")
#print('Nama : ' + nama)
#print('Umur : ' + umur)
#print('Jenis kelamin : ' + jenis_k)
#print('Pekerjaan : ' + pekerjaan)

#Numbers & Arithmetic Operators
#usiaAndi = 40
#usiaBudi = 20
#print(usiaAndi * usiaBudi)
#print(usiaAndi / usiaBudi)
#print(usiaAndi + usiaBudi)
#print(usiaAndi - usiaBudi)
#print(usiaAndi % usiaBudi)
#print(usiaBudi ** 2)

##Numbers & Arithmetic Operators
#usiaAndi = 40
#usiaBudi = 20
#usiaAndi += 3
## usiaAndi = usiaAndi + 3
#usiaBudi *= 4
## usiaBudi = usiaBudi * 4
#print(usiaAndi)
#print(usiaBudi)

#Math Module
# import math
# print(math.pi)
# print(math.fabs(-4.7)) #absolute value
#print(math.pow(8, 2))
#print(math.sqrt(64))
#Round, Ceil, & Floor
#import math
#print(round(4.7))
#print(round(4.4))
#print(math.floor(4.7))
#print(math.ceil(4.4))

##Strings
# x = 'Halo Dunia'
# print(len(x))
# print(x.index('Dunia'))
# print(x.split(' '))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

#Strings
# singleQuotes = 'single quotes'
# doubleQuotes = "double quotes"
# combineQuotes = "wrap lot's of other quotes"
# print(singleQuotes)
# print(doubleQuotes)
# print(combineQuotes)

#Strings Indexing
# text = "I'm Baron, nice to meet you"
# print(text[0])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[:])

# #Convert Strings to Numbers
# angka1 = input("Masukkan Angka 1 : ")
# angka2 = input("Masukkan Angka 2 : ")

# print(type(angka1))
# print(angka1 + angka2)

# print(int(angka1) + int(angka2))
# print(type(angka1))

# angka1 = float(angka1)
# angka2 = float(angka2)
# print(angka1 + angka2)

# ##Adding Strings & Numbers
# usia = 22
# nama = 'Andi'
# print(usia + usia)
# print(nama + ' ' + nama)
# print(nama + ' ' + str(usia))

# ##Solve IT #1
# x = 4
# y = 3
# z = 2
# w = print(round((((x+y*z)/(x*y))**z),2))


##Solve IT #2

# x = int(input("Silakan masukkan angka berapapun : "))
# y = print(x**2)

##listing yg memastikan angka yang diinputkan berupa angka

# check = False
# while check == False:

#     x = input("Silakan masukkan angka berapapun : ")
#     if x.isdigit() == True :
#         check = True #exit way ke menu selanjutnya
#     else :
#         print('Input yang anda masukkan bukan berupa angka, silahkan masukkan input angka kembali')
    
# y = print('Kuadarat dari ' + x + ' = ' + str(int(x)**2))


# ##Solve It! #3

# check = False
# while check == False :

#     x = input("Silakan masukkan jumlah hari : ")
#     if x.isdigit() == True :
#         check = True
#     else :
#         print('Input yang anda masukkan bukan berupa angka, silahkan masukkan input angka kembali')

# print('Dalam ' + str(x) + ' hari, terdapat ' + str(int(x)//360) + ' tahun, ' + str(int(x)%360//30) + ' bulan, ' +  str(int(x)%360%30) + ' hari.')



##Solve It! #4

# x = int(input('Jumlah usia Andi & Budi (th) : '))
# y = float(input('Rasio usia Andi & Budi (0-1) : '))
# z = int(input('Berapa usia Andi & Budi dalam berapa tahun lagi? : '))

# # A / B = y
# # A = B * y

# # A + B = x
# # B*y + B = x
# # (B(y+1)) = x

# B = x / (y+1)
# A = x - B
# Bz = int(B) + 2
# Az = int(A) + 2
# print('Usia Andi ' + str(z) + ' tahun lagi adalah ' + str(Az))
# print('Usia Budi ' + str(z) + ' tahun lagi adalah ' + str(Bz))


# ##Solve It! #5
# x = input('Masukkan kalimat : ')
# y = input('Masukkan karakter yang ingin dihitung dalam kalimat : ')
# print('Dalam kalimat ' + x + ' memiliki huruf ' + y + ' sebanyak ' + str(x.count(y)) + ' buah.' )


##Solve It! #6
# import math
# x = int(input('Jarak mobil a & b (km): '))
# y = int(input('Kecepatan mobil a dari arah timur (km/h) : '))
# z = int(input('Kecepatan mobil b dari arah timur (km/h) : '))
# p = int(input('Masukkan jam A & B mulai berangkat : '))

# # sA + sB = x

# # vA + vB = tot_v
# # y + z = tot_v

# waktu = x / (y+z)
# # menit = int(waktu%1*60)
# print('Jam mobil a dan b bertabrakan adalah jam ' + str(p+math.floor(waktu)) + ' lebih ' + str(int(math.ceil(waktu % 1 * 60))) + ' menit')


# ##Tugas soal 1
# from math import floor
# x = int(input('Input four-digit number : '))
# print('Output : ' + str((x%100*100)+floor(x/100)))

# ## Tugas soal 2
# from math import pi
# x = float(input('Input radius : '))
# print('Output area : ' + str(round((x**2*pi),2)))

# ## Tugas soal 3
# x = int(input('Input 1 (two-digit numbers) : '))
# y = int(input('Input 2 (two-digit numbers) : '))
# print('Output : ' + str((x//10*1000)+(y//10*100)+(x%10*10)+(y%10)))

# ## Tugas soal 4
# x = input('Input string/ sentence : ')
# y = input('Input character you want remove : ')
# print('Output : ' + x.replace(y,''))

# ## Tugas soal 5
# x = input('Input two words separated by a space: ')
# y = x.split()
# ##print('Output : ' + y[1] + ' ' + y[0])
# print('Output : ' + y[1], y[0])
