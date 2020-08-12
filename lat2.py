## Assignment Operators

# usiaAndi = 40

# usiaAndi *= 2
# print(usiaAndi)

# usiaAndi /= 2
# print(int(usiaAndi))

# usiaAndi += 2
# print(usiaAndi)

# usiaAndi -= 2
# print(usiaAndi)

# usiaAndi %= 2
# print(usiaAndi)

# # Comparison Operators
# # == value sama, dan data type sama
# # > lebih dari
# # < kurang dari
# # >= lebih dari sama dengan
# # <= kurang dari sama dengan

# x = 5
# y = '5'

# print(x == y)
# ## False, karena tipe data tidak sama

# print(x > int(y))
# ## False, karena sama dengan

# print(x >= int(y))
# ## True

# print(x < int(y))
# ## False, karena sama dengan

# print(x <= int(y))
# ## True




# # Logical Operators
# # and (keduanya benar, maka TRUE)
# # or (salah satu benar, maka TRUE)
# # not (membalik logika TRUE/FALSE) 

# x = 5
# y = '5'
# z = 6

# print(x == int(y) and int(y)<z)
# ## true and true -> true

# print(x == int(y) or (y)<z)
# ## true or true -> true

# print(x == int(y) or int(y)<z)
# ## true or true -> true

# print(not(x == int(y) or int(y)<z))
# ## not (true or true) => false



# # ##If, else if & else
# # if (condition) :
# #     program
# # elif (condition) :
# #     program
# # else :
# #     program



# nilai = 40
# if (nilai > 80):
#     print('Excelent! ')
# elif (nilai >= 60 and nilai <= 80):
#     print('Good job!')
# else :
#     print("Don't give up!")

# jomblo = False

# if (jomblo):
#     print('Masih jomblo!')
# else:
#     print('Udah taken!')

## Solve It! #1
# x = int(input('Masukkan angka : '))
# if x % 2 == 0:
#     print('Angka ' + str(x) + ' tergolong bilangan GENAP!')
# else:
#     print('Angka ' + str(x) + ' tergolong bilangan GANJIL!')

# ## Solve It! #2
# massa = float(input('Masukkan Massa (kg) : '))
# tinggi = float(input('Masukkan Tinggi (cm) : '))
# print('Massa ' + str(massa) + ' & tinggi ' + str(tinggi) + ' m')
# imt = round(massa/((tinggi/100)**2),1)

# if imt < 18.5:
#     print('IMT ' + str(imt) + ', BERAT BADAN KURANG!')
# elif imt < 25:
#     print('IMT ' + str(imt) + ', BERAT BADAN IDEAL!')
# elif imt < 30:
#     print('IMT ' + str(imt) + ', BB BERLEBIH!')
# elif imt < 40:
#     print('IMT ' + str(imt) + ', BB SANGAT BEREBIH!')
# else:
#     print('IMT ' + str(imt) + ', OBESITAS!')