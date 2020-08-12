####DICTIONARIES
# d = {
#     'key1' : 'item1',
#     'key2' : 'item2',
#     'kucing' : [3, 'jerapah']
# }

# print(d['key1'])
# print(d['key2'])
# print(d['kucing'])
# print(d['kucing'][1])

# # OUT: 
# # item1
# # item2
# # [3, 'jerapah']
# # jerapah



####DICTIONARIES INSIDE DICTIONARIES
# d = {
#     'key1' : {'key2' : 'item1'},
#     'kucing' : [3, 'jerapah']
# }

# print(d['key1'])
# print(d['key1']['key2'])
# print(d['kucing'])
# print(d['kucing'][1])

# # OUT: 
# # {'key2': 'item1'}
# # item1
# # [3, 'jerapah']
# # jerapah



####TUPLES
##Similar like list, but Tupels value cant be changed
# t = (1, [0, 'test'], {'a1' : True})

# print(t[2]['a1'])
# print(t[1][1])
# t[1][1] = 'akan'
# print(t[1][1])
# t[1][0] = "mark"
# print(t[1])
#OUT:
# # True
# # test
# # akan
# # ['mark', 'akan']

# t[0] = "mark"
# ###error t does not support item assigment karena merupakan data tuples




####SETS doesn't support indexing, there isn't duplicate items in set (every item unique)

# s = {1, 3, 1, 2, 2, 3}

# print(s)
# print(list(s)[2])

# OUT : 
# {1, 2, 3}
# 3



### FILTERING LIST USING SET
# newList = [1, 3, 'test1', 'test2', 2, 3, 'test1']
# s = set(newList)

# print(s)
# print(list(s)[2])
# print(list(s)[2])
# print(list(s)[0])
# print(list(s)[4])

# OUT: 
# {1, 2, 3, 'test1', 'test2'}
# 3

##OUT: urutannya selalu berubah-ubah
# {1, 2, 'test2', 3, 'test1'}
# test2
# test2
# 1
# test1


# ###LIST COMPREHENSION
# listNum = [1, 2, 3, 4, 5]
# listNum = [item * 2 for item in listNum]
# print(listNum)
# #### out : [2, 4, 6, 8, 10]


##LAMBDA EXPRESSIONS

# # version function
# def times2(num):
#     return num*2
# print(times2(2))
# # out : 4


# #version lambda
# x=lambda num: num * 2
# print(x(2))
# # out : 4



###MAP -> perulangan

# ####Without lambda (using function)
# def times2(num):
#     return num*2

# listNum = [1,2,3,4,5]
# listNum = list(map(times2, listNum))
# print(listNum)
# # out : [2, 4, 6, 8, 10]


# ####With lambda 
# listNum = [1,2,3,4,5]
# listNum = list(map(lambda num: num *2, listNum))
# print(listNum)
# # out : [2, 4, 6, 8, 10]




###FILTER

# # ####Without lambda (using function)
# def genap(num):
#     return num % 2 == 0

# listNum = [1,2,3,4,5]
# listNum = list(filter(genap, listNum))
# print(listNum)
# # out : [2, 4]


# ####With lambda 
# listNum = [1,2,3,4,5]
# listNum = list(filter(lambda num: num % 2 == 0, listNum))
# print(listNum)
# # out : [2, 4]



# # ##METHODS FOR SEARCHING
# numList = [1,2,3]
# input = 'x'

# check1 = input in numList
# check2 = 'x' in ['x', 'y', 'z']
# check3 = 'ka' in 'kurakas'

# print(check1)
# print(check2)
# print(check3)

# # # out:
# # # False
# # # True
# # # True



####SOLVE IT
##Buat aplikasi sederhana untuk filtering list(searching) berdasrkan input user 
# BackToMenu = True
# while BackToMenu == True:
    
#     def duplicateFilter(function, iterasi):
#         hasil = []
#         for item in iterasi:
#             if function (item):
#                 hasil.append(item)
#         return hasil

#     x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
#     iterasi = len(x)
#     search = input('search: ')
#     check = duplicateFilter(lambda item : search.lower() in item.lower(), x)
#     print(check)
#     ask = input('Apakah anda mau kembali ke menu awal (y/n)? ')
#     if ask == 'n':
#         print()
#         BackToMenu = False



####ITEM?????? diganti list_x FUNCTION????? diganti fungsi_it
#### tdk ada yg mengatakan bahwa list x merupakan list dari x di program
### karena lambda?????????
BackToMenu = True
while BackToMenu == True:
    
    def duplicateFilter(fungsi_it, iterasi):
        hasil = []
        for list_x in iterasi:
            if fungsi_it(list_x):
                hasil.append(list_x)
        return hasil

    x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
    iterasi = len(x)
    search = input('search: ')
    check = duplicateFilter(lambda list_x : search.lower() in list_x.lower(), x)
    print(check)
    ask = input('Apakah anda mau kembali ke menu awal (y/n)? ')
    if ask == 'n':
        print()
        BackToMenu = False

##oretan
# x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam'] 
# out = [] ###
# search = input('search: ')
# for i in range (len(x)):
#     check = search in x[i]
#     print (x[i])
#     if check == True:
#         out += x[i]
# print(out)
# # # search = ll
# # #out = ['H', 'e', 'l', 'l', 'o', 'H', 'e', 'l', 'l', 'o', 's'] -> output salah

##oretan
# x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
# out ='' ###
# search = input('search: ')
# for i in range (len(x)):
#     check = search in x[i]
#     print (x[i])
#     if check == True:
#         out += x[i]
# print(out)
# # # search = ll
# # # out = HelloHellos -> output salah


##oretan
# x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
# out =[] ###BERHASIL
# search = input('search: ')
# for i in range (len(x)):
#     check = search in x[i]
#     print (x[i])
#     if check == True:
#         out.append(x[i]) #####BERHASIL
# print(out)
# # # search = ll
# # # out = ['Hello', 'Hellos']
# ###INGAT UNTUK LIST DICTIONARY JIKA INGIN MENAMBAHKAN LIST MENGGUNAKAN APPEND



# def duplicateFilter(function, iterasi):
#     hasil = []
#     for item in iterasi:
#         if function (item):
#             hasil.append(item)
#     return hasil

# x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari Ayam']
# iterasi = len(x)
# search = input('search: ')
# check = duplicateFilter(lambda item : search.lower() in item.lower(), x)
# print(check)




# newlist = []
# for item in check:
#     newlist[item] = x[item]
# print(newlist)



# def check(search):
#     sarch_low = search.
#     return 



