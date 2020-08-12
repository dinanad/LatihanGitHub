# ## While Loop
# ## Ehile running jika true, jika false looping akan berhenti
# angka = 1
# while (angka <= 10):
#     print(angka)
#     angka += 1


## For Loop and List
# listItem = list(range(1,12,2))
# print(listItem)

# for item in range(1,11,2):
#     print(item)

## Solve It #1

# urut = 0
# while (urut <=10):
#     urut += 1
#     print('Nomor urut ' + str(urut))

# y = 'Nomor urut '
# for item in range(1,11):
#     print(y + str(item))

# y = 'Nomor urut '
# for item in range(0,21,2):
#     print(y + str(item))

# y = 'Nomor urut '
# for item in range(1,21,2):
#     print(y + str(item))


## For Loop Drawing
# z = ''
# for item in range (0,5):
#     z += ' * '
# print(z)

# # *  *  *  *  * 

# z = ''
# for item in range (0,5):
#     z += ' * \n'
# print(z)

# #  *
# #  *
# #  *
# #  *
# #  *



# z = ''
# for item in range (0,5):
#     for item in range(0,5):
#         z += ' * '
#     z += '\n'
# print(z)

# #  *  *  *  *  * 
# #  *  *  *  *  *
# #  *  *  *  *  *
# #  *  *  *  *  *
# #  *  *  *  *  *

# z = ''
# for x in range (0,5):
#     for y in range(0,5,x+1):
#         print(' * ')
#     print('\n')
# print(z)

# #  * 
# #  *
# #  *
# #  *
# #  *


# #  *
# #  *
# #  *


# #  *
# #  *


# #  *
# #  *


# #  *




# z = ''
# for x in range (0,5):
#     for y in range (5,1,-1):
#         z += ' * '
#     z += '\n'
# print(z)

# #  *  *  *  * 
# #  *  *  *  *
# #  *  *  *  *
# #  *  *  *  *
# #  *  *  *  *

# z = ''
# for x in range (5):
#     for y in range(0,x+1):
#         z += ' * '
#     z += '\n'
# print(z)

# #  * 
# #  *  *
# #  *  *  *
# #  *  *  *  *
# #  *  *  *  *  *

##Solve It! #1
# a = ''
# for x in range(5,0,-1):
#     for y in range (0, x):
#         a += ' * '
#     a += '\n'
# print(a)

# #  *  *  *  *  * 
# #  *  *  *  *
# #  *  *  *
# #  *  *
# #  *


##Solve It! #2
# a = ''

# for x in range(10,0,-1):
#     if x > 5 :
#         for y in range(0,x-5):
#             a += ' * '
#         a += '\n'
#     else:
#         for z in range(0,x):
#             a += ' * '
#         a += '\n'  
# print(a)
#  *  *  *  *  * 
#  *  *  *  *
#  *  *  *
#  *  *
#  *
#  *  *  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *

# x=1
# while(x<=10):

#     if x <=5:
#         a =6
#         for i in range(0,a):
#             for j in range(0, a-1):
#                 print(' * ', end = '')
#             a -= 1
#             print('')
    
    
#     else:
#         for k in range(0,5):
#             for l in range(0, k+1):
#                 print(' * ', end = '')
#             print(' ')

#     x += 1

## Solve It#2
# a =10
# for i in range(0,a):
    
#     if a > 5:
#         for j in range(0, a-5):
#             print(' * ', end = '')
#         a -= 1
#         print('')


#     else:
#         for k in range(i-4):
#             print(' * ', end = '')
#         a -= 1
#         print('')
#  *  *  *  *  * 
#  *  *  *  *
#  *  *  *
#  *  *
#  *
#  *
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *






# ## Solve It! #3
# a = '   '

# ##Looping baris
# bar = 10
# while bar >= 0:
    

#     ##Looping spasi kosong
#     kol = bar
#     while kol > 0:
#         a += '   '
#         kol = kol - 1

#     ##Looping kolom bintang atas
#     kiri = 1
#     while kiri < (10-(bar-1)):
#         a += ' * '
#         kiri += 1

#     ##Looping kolom bintang bawah
#     kanan = 1
#     while kanan < kiri-1:
#         a += ' * '
#         kanan += 1

#     a += '\n'
#     bar -= 1

# print(a)

#                             *
#                          *  *  *
#                       *  *  *  *  *
#                    *  *  *  *  *  *  *
#                 *  *  *  *  *  *  *  *  *
#              *  *  *  *  *  *  *  *  *  *  *
#           *  *  *  *  *  *  *  *  *  *  *  *  *
#        *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *




# ## Solve It! #4
# a = '   '
# bar = 1

# ##Looping baris

# while bar <= 10:
#     kol = bar

#     ##Looping spasi kosong
    
#     while kol > 1:
#         a += '   '
#         kol = kol - 1

#     ##Looping kolom bintang atas
#     kiri = 0
#     while kiri <= (10-bar):
#         a += ' * '
#         kiri += 1

#     ##Looping kolom bintang bawah
#     kanan = kiri
#     while kanan > 1:
#         a += ' * '
#         kanan -= 1

#     a += '\n'
#     bar += 1

# print(a)

    # *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
    # *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
    #    *  *  *  *  *  *  *  *  *  *  *  *  *  *  * 
    #       *  *  *  *  *  *  *  *  *  *  *  *  * 
    #          *  *  *  *  *  *  *  *  *  *  *
    #             *  *  *  *  *  *  *  *  *
    #                *  *  *  *  *  *  *
    #                   *  *  *  *  *
    #                      *  *  *
    #                         *




## Solve It! #5
a = '   '
bar = 8

##Looping baris

while bar >= 0:
    kol = bar

    ##Looping spasi kosong
    
    while kol > 0:
        a += '   '
        kol = kol - 1

    ##Looping kolom bintang kiri
    kiri = 1
    while kiri <= (10-bar):
        a += ' * '
        kiri += 1

    ##Looping kolom bintang kanan
    kanan = 1
    while kanan < kiri - 1:
        a += ' * '
        kanan += 1

    a += '\n'
    bar += 1


bar = 1

##Looping baris

while bar <= 8:
    kol = bar+1

    ##Looping spasi kosong
    
    while kol > 1:
        a += '   '
        kol = kol - 1

    ##Looping kolom bintang kiri
    kiri = 0
    while kiri < (10-bar):
        a += ' * '
        kiri += 1

    ##Looping kolom bintang kanan
    kanan = kiri
    while kanan > 1:
        a += ' * '
        kanan -= 1

    a += '\n'
    bar += 1

print(a)