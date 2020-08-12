# Soal 1
#angka = (input('Masukan empat digit angka dengan spasi: '))
#l_angka = (angka.split())
#l_angka[0], l_angka[1], l_angka[2], l_angka[3]= l_angka[2], l_angka[3], l_angka[0], l_angka[1]
#print(l_angka)

##Jawab
# a = int(input("Masukkan Angka : "))
# print(a % 100 * 100 + a // 100)

# Jawab dina
# a = int(input("Masukkan 4 digit angka : "))
# print('Output : '  + str(a % 100 * 100 + a // 100))

#Soal 2
#import math
 
#radius = int(input('Input radius : '))
#output = math.pi * (radius**2)
#print(f'Output area : {output}')

##Jawab
# from math import pi, floor, ceil, pow
# ##phi * r^2
# r = float(input("Input the radius of the circle: "))
# #formula = round((pi * r**2),2) 
# #print("The area of the circle with radius " + str(r) + ' is ' + str(formula))

# ##Jawaban lain
# from math import pi, floor, ceil, pow
# r = float(input("Input the radius of the circle: "))
# print("The area of the circle with radius " + str(r) + ' is ' + str(pi * r**2))

#Soal3
#angka1 = (input('Masukan dua digit angka dengan spasi: '))
#l_angka1 = (angka1.split())

#angka2 = (input('Masukan dua digit angka dengan spasi: '))
#l_angka2 = (angka2.split())

#output = (l_angka1 + l_angka2)

#output[1], output[2] = output[2], output[1]
#print(f'Output: {output}')

##Jawab:
#x = int(input("Input first number (2 digit): "))
#y = int(input("Input second number (2 digit): "))

#a = x // 10 #ambil angka awal di 2 angka pertama
#b = x % 10 #ambil angka akhir di 2 angka pertama
#c = y // 10 #ambil angka awal di 2 angka kedua
#d = y % 10 #ambil angka akhir di 2 angka kedua

##Output [a] [c] [b] [d]
#print(a*1000 + c*100 + b*10 + d)

##Jawaban lain
# x = int(input("Input first number (2 digit): "))
# y = int(input("Input second number (2 digit): "))
# print('Output : ' + str(x//10*1000 + y//10*100 + x%10*10 + y%10))


#Soal 4
#import.re
#sentence = input('Input string: ')
#remove = input('Input character to remove: ')
##str?
#output = str(sentence.replace(remove, ""))
#print(f'Output: {output}')

##Jawab
#input_kalimat = input("Input your sentence : ")
#replace = input("Remove word : ")
#print(input_kalimat.replace(replace,"")

##Jawaban lain
# sentence = input('Input string: ')
# remove = input('Input character to remove: ')
# print(sentence.replace(remove,""))

#Soal 5
#input = input('Input two words separated by a space: ')
#kalimat= (input.split())
#print('Output: ' + kalimat[1], kalimat[0])

##Jawab
#input_kalimat = input('Input your sentence: ')
#list_kata = input_kalimat.split()
#print(list_kata[1] + " " + list_kata[0]