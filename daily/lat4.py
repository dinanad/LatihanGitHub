## Function

# def contoh() :
#     print('Halo Dunia')

# contoh()

# x=10
# y=50
# def contoh() :
#     print(x+y)

# contoh()


# ##Function with a Parameter
# def namaku (nama):
#     print(nama + ' Susilo')

# namaku('Adi')
# namaku('Budi')
# namaku('Caca')
# namaku('Dedi')



# ### Function with 2 Parameters
# # def data (x,y):
# #     print(x + ' Lahir th '+y)

# # data('Adi','1990')
# # data('Budi','1991')
# # data('Caca','1992')
# # data('Dedi','1993')



##Return Function
# z=''
# def total(x,y):
#     z = x + y
#     return z

# print(total(4,5))
# print(z)
# # out: 5

## z adalah local variabel dalam func total, tidak dapat dipanggil di luar function tersebut
## jika z tidak di return maka total (4,5) = none


# z=''
# def total(x,y):
#     z = x + y
# print(total(4,5))
# print(z)
# # Out: None




# def total(x,y):
#     z = x + y

# print(total(4,5))
# # None


# ##Fn inside Fn
# def kali(x):
#     if (x < 2):
#         return 1
#     else:
#         return(x * tiga())

# def tiga():
#     return 3

# hasil = int(input('masukkan angka : '))
# print(kali(hasil))
###setelah return dapat diberikan nilai berupa angka
###operasi matematika tipe data harus int & u/operasi string tdk boleh ada int


### DEFAULT PARAMETER

# def kali(angka1 = 5, angka2 = 2):
#     return angka1 * angka2
# print(kali(angka2 = 4))
# ####out: 20



##LIST - Arrays are container-like values that can hold other values. 
##The values inside an array are called elements
# mobil = ['Alya', 'Xenia', 'Avanza']
# print(mobil)
# print(mobil[0])
# print(mobil[1])
# print(mobil[2])
####OUT
# # ['Alya', 'Xenia', 'Avanza']
# # Alya
# # Xenia
# # Avanza



###ACCESS LIST VALUE
# buah = ['Jeruk', 'Nanas', 'Apel']
# for item in buah:
#     print(item)
# # OUT:
# # Jeruk
# # Nanas
# # Apel



# buah = ['Jeruk', 'Nanas', 'Apel']
# print(buah[1:])
# print(buah[:3])
# print(buah[2:4])
# print(buah[:])
# # # OUT
# # # ['Nanas', 'Apel']
# # # ['Jeruk', 'Nanas', 'Apel']
# # # ['Apel']
# # # ['Jeruk', 'Nanas', 'Apel']


###CHANGE LIST VALUE
# buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']
# buah[1] = 'Kelapa'
# print(buah)
# # OUT: ['Jeruk', 'Kelapa', 'Apel', 'Mangga']



###LIST APPEND & POP
# buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']
# buah.append('Kelapa')
# print(buah)
# buah.pop()
# buah.pop()
# print(buah)
##OUT:
# # ['Jeruk', 'Nanas', 'Apel', 'Mangga', 'Kelapa']
# # ['Jeruk', 'Nanas', 'Apel']



# ###LIST INSIDE LIST AND DIFF TYPE DATA
# listTest = [1, 'hi', ['hello', 2, True, [0,1]]]
# print(listTest[1])
# print(listTest[:2])
# print(listTest[2])
# print(listTest[2][1:])
# print(listTest[2][2])
# print(listTest[2][3][0])
# # # out:
# # # # hi
# # # # [1, 'hi']
# # # # ['hello', 2, True, [0, 1]]
# # # # [2, True, [0, 1]]
# # # # True
# # # # 0



###ALGORITMA MENGURUTKAN DATA ASCENDING
# x = [400,100,50,20,5]
# for i in range (len(x)-1,0,-1):
#     for j in range (i):
#         if x[j] > x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
#         print(f'{i}\t{j}\t{list(x)}')
# print(list(x))

# OUT:
# 4       0       [100, 400, 50, 20, 5]
# 4       1       [100, 50, 400, 20, 5]
# 4       2       [100, 50, 20, 400, 5]
# 4       3       [100, 50, 20, 5, 400]
# 3       0       [50, 100, 20, 5, 400]
# 3       1       [50, 20, 100, 5, 400]
# 3       2       [50, 20, 5, 100, 400]
# 2       0       [20, 50, 5, 100, 400]
# 2       1       [20, 5, 50, 100, 400]
# 1       0       [5, 20, 50, 100, 400]

# [5, 20, 50, 100, 400]

###ALGORITMA MENGURUTKAN DATA DESCENDING
# x = [5,20,50,100,500]
# for i in range (len(x)-1,0,-1):
#     for j in range (i):
#         if x[j] < x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
#         print(f'{i}\t{j}\t{list(x)}')
# print(list(x))

# OUT:
# 4       0       [20, 5, 50, 100, 500]
# 4       1       [20, 50, 5, 100, 500]
# 4       2       [20, 50, 100, 5, 500]
# 4       3       [20, 50, 100, 500, 5]
# 3       0       [50, 20, 100, 500, 5]
# 3       1       [50, 100, 20, 500, 5]
# 3       2       [50, 100, 500, 20, 5]
# 2       0       [100, 50, 500, 20, 5]
# 2       1       [100, 500, 50, 20, 5]
# 1       0       [500, 100, 50, 20, 5]
# [500, 100, 50, 20, 5]



## Solve IT 1 Buatlah algoritma untuk mengurutkan elemen array berikut :
# x = [40, 100, 1, 5, 25, 10]
# for i in range (len(x)-1,0,-1):
#     for j in range (i):
#         if x[j] > x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
# print(list(x))

# # out : [1, 5, 10, 25, 40, 100]


## Solve IT 2 Buatlah algoritma untuk mengurutkan elemen array berikut :
# x = [40, 100, 1, 5, 25, 10]
# for i in range (len(x)-1,0,-1):
#     for j in range (i):
#         if x[j] < x[j+1]:
#             x[j], x[j+1] = x[j+1], x[j]
# print(list(x))

# # # out : [100, 40, 25, 10, 5, 1]







