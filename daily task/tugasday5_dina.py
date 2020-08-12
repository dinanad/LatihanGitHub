# ## Soal 1 Duplicate string 
# ##duplicate_string('NikiZefanya') 
# ##outputnya 
# ##niikkkiiiizzzzzeeeeeefffffffaaaaaaaannnnnnnnnyyyyyyyyyyaaaaaaaaaaa

# a = 'NikiZefanya'
# b = a.lower()
 
# dup = ''

# for i in range (1,c):
#     if i > 1:
#         dup += b[i]*i
#     elif i == 1:
#         dup += b[0]
# print(dup)



# ## Soal 2 Duplicate String strip kapital
# ##duplicate_string_strip('anugrah')
# ##outputnya :
# ##-A-Nn-Uuu-Gggg-Rrrrr-Aaaaaa-Hhhhhhh
    
# c = ' anugrah'
# dupl = ''

# for j in range (len(c)):
#     dupl += '-'
#     dupl += c[j]*j
# print(dupl)

# c = ' anugrah'
# dupl = ''

# for j in range (len(c)):
#     if j > 1:
#         dupl += '-'
#         dupl += c[j]*j

#     elif j == 1:
#         dupl += '-A'
# print(dupl)

# c = 'anugrah'
# dupl = ''

# for j in range (len(c)):
#     if j > 0:
#         dupl += '-'
#         dupl += c[j]*j

#     elif j == 0:
#         dupl += '-A'
# print(dupl)



# ## Soal 3 Fungsi sort ascending
# print(sort_ascending([1,5,6,4,3,2,10,2,11,3,4,6,7]))
# outputnya
# [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 10, 11]

# data = [1,5,6,4,3,2,10,2,11,3,4,6,7]
# sort_ascending = sorted(data)
# print(sort_ascending)



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

#     ##Looping kolom bintang kiri
#     kiri = 0
#     while kiri <= (10-bar):
#         a += ' * '
#         kiri += 1

#     ##Looping kolom bintang kanan
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




# ## Soal No.5 
# a = ''
# x = 8
# bar = x

# ##Looping baris

# while bar >= 0:
#     kol = bar

#     ##Looping spasi kosong
    
#     while kol > 0:
#         a += '   '
#         kol = kol - 1

#     ##Looping kolom bintang kiri
#     kiri = 1
#     while kiri < (x - (bar - 1)):
#         a += ' * '
#         kiri += 1

#     ##Looping kolom bintang kanan
#     kanan = 1
#     while kanan < kiri - 1:
#         a += ' * '
#         kanan += 1

#     a += '\n'
#     bar -= 1


# bar = 1

# ##Looping baris

# while bar <=x:
#     kol = bar+1

#     ##Looping spasi kosong
    
#     while kol > 1:
#         a += '   '
#         kol = kol - 1

#     ##Looping kolom bintang kiri
#     kiri = 0
#     while kiri < (x-bar):
#         a += ' * '
#         kiri += 1

#     ##Looping kolom bintang kanan
#     kanan = kiri
#     while kanan > 1:
#         a += ' * '
#         kanan -= 1

#     a += '\n'
#     bar += 1

# print(a)

                              
# #                       *       
# #                    *  *  *    
# #                 *  *  *  *  * 
# #              *  *  *  *  *  *  *
# #           *  *  *  *  *  *  *  *  *
# #        *  *  *  *  *  *  *  *  *  *  *
# #     *  *  *  *  *  *  *  *  *  *  *  *  *
# #  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
# #     *  *  *  *  *  *  *  *  *  *  *  *  *
# #        *  *  *  *  *  *  *  *  *  *  *
# #           *  *  *  *  *  *  *  *  *
# #              *  *  *  *  *  *  *
# #                 *  *  *  *  *
# #                    *  *  *
# #                       *


