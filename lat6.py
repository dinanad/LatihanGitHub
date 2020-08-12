


####FIZZBUZZ
# #  Fizz Buzz is an algorithm function that will log out to the console
# # every number from 1 to “num”.
# # • For each number, if the number is divisible by 3, it’ll log out the word
# # “Fizz” instead of that number.
# # • Next, if the number is divisible by 5, it’ll log out the word “Buzz”
# # instead of that number.
# # • And finally, if a number is divisible by both 3 and 5, we want to logout
# # the word “FizzBuzz” instead of that number.
# # • Beside is the result of fizzBuzz(20) 

# def fizzBuzz(num):
#     for i in range (1, num+1) :
#         if (i % 15 == 0):
#             print('FizzBuzz')
#         elif (i % 5 == 0):
#             print('Buzz')
#         elif (i % 3 == 0):
#             print('Fizz')
#         else:
#             print(i)

# fizzBuzz(20)

# # OUT:
# # 1
# # 2
# # Fizz
# # 4
# # Buzz
# # Fizz
# # 7
# # 8
# # Fizz
# # Buzz
# # 11
# # fizz
# # 13
# # 14
# # FizzBuzz
# # 16
# # 17
# # fizz
# # 19
# # Buzz
##### Syarat yg utama paling atas (3 & 5 =15) baru setelahnya yg lain


####Jika syarat yg diurutkan dalam conditional fizz, buzz, fizzbuzz
###pada output tidak ada FizzBuzz karena 15 sudah dipenuhi oleh kondisi Fizz
# def fizzBuzz(num):
#     for i in range (1, num+1) :
#         if (i % 3 == 0):
#             print('Fizz')
#         elif (i % 5 == 0):
#             print('Buzz')
#         elif (i % 15 == 0):
#             print('FizzBuzz')
#         else:
#             print(i)

# fizzBuzz(20)


# # # OUT :
# # # 1
# # # 2
# # # Fizz
# # # 4
# # # Buzz
# # # Fizz
# # # 7
# # # 8
# # # Fizz
# # # Buzz
# # # 11
# # # Fizz
# # # 13
# # # 14
# # # Fizz
# # # 16
# # # 17
# # # Fizz
# # # 19
# # # Buzz


####Fibonacci
####Jangan lupa pake append karena menambahkan list data 
# def fibo(urut):
#     deret_fibo = [1,1]
#     for i in range (2,urut):
#         deret_fibo.append(deret_fibo[i-2] + deret_fibo[i-1])
#     return deret_fibo[urut-1]

# print(fibo(6))
# ## out: 8



# def fibo(urut):
#     deret_fibo = [1,1]
#     for i in range (2,urut):
#         deret_fibo.append(deret_fibo[i-2] + deret_fibo[i-1])
#     return (f'Deret fibonacci ke-{urut} adalah {deret_fibo[urut-1]}')

# print(fibo(6))
# ## out: input=6, output = 8



###REVERSE LIST IN PLACE
# # This algorithm function will take in a list as a parameter,
# # then it’ll reverse that list and return us the reversed list. 

### Bilangan di dalam list genap
# import math
# def reverseList(theList):
#     for i in range(0, math.floor(len(theList)/2)):
#         theList[i], theList[len(theList)-1-i] = theList[len(theList)-1-i], theList[i]
#     return theList
# print(reverseList([1,2,3,4,5,6,7,8]))
#####out : [8, 7, 6, 5, 4, 3, 2, 1]


#### Bilangan dalam list ganjil
# import math
# def reverseList(theList):
#     for i in range(0, math.floor(len(theList)/2)):
#         theList[i], theList[len(theList)-1-i] = theList[len(theList)-1-i], theList[i]
#     return theList
# print(reverseList([1,2,3,4,5,6,7,8,9]))
# #####out : [9, 8, 7, 6, 5, 4, 3, 2, 1]


# ####BUBLE SORT
# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]
# def bubbleSort(list):
#     for i in range(len(list), 0, -1):
#         for j in range(0, i-1):
#             if (list[j] > list[j+1]):
#                 list[j], list[j+1] = list[j+1], list[j] 
#     return list
# print(bubbleSort(x))
# # # out: [1, 3, 9, 34, 198, 200, 203, 746, 764, 984, 6000]



# ### MEAN -> Mean is the average value of a dataset. 
# x = [ 1,2,3,2,5,2,7,2 ]

# def getMean(list) :
#     sum = 0
#     for item in list:
#         sum += item
#     mean = sum/len(list)
#     return mean
# print(getMean(x))




### MEDIAN -> Median is the middle number of a dataset. 
# from math import floor
# x = [ 1,2,3,2,5,2,7,2]

# def getMedian(list) :
#     list.sort()
#     median = 0
#     if (len(list) % 2 != 0):
#         median = list[floor(len(list)/2)]
#         print('ganjil')
#     else:
#         mid1 = list[int(len(list)/2)-1]
#         mid2 = list[int(len(list)/2)]
#         median = (mid1 + mid2) / 2
#         print('genap')
#     print(list)
#     return median
# print(getMedian(x))




# # ### MODE -> Mean is the average value of a dataset. 
# x = [ 1,2,3,2,5,2,7,2 ]

# def getMode(list) :
#     countList = []

#     ###create count list
#     for num  in list:    ### [ 1,2,3,2,5,2,7,2 ] -> 8 perulangan
#         check = False
#         for list in countList:
#             if (list[0] == num):
#                 list[1] += 1
#                 check =True
#         if (check == False):
#             countList.append([num,0])

#     ###create list of mode/s
#     maxFrequency = 0
#     modes = []
#     for list in countList:
#         if (list[1] > maxFrequency) :
#             modes = [list[0]]
#             maxFrequency = list[1]
#         elif (list[1] == maxFrequency):
#             modes.append(list[0])


#     ###if every value appears same amount of times
#     if (len(modes) == len(countList)):
#         modes = []     
#     return modes
# print(getMode(x))

# #####out : [2]





# ### MODE -> Mean is the average value of a dataset. 
x = [ 1,2,3,2,5,2,7,2 ]

def getMode(list) :
    countList = []

    ###create count list
    for num  in list:    ### [ 1,2,3,2,5,2,7,2 ] -> 8 perulangan sesuai dengan jumlah list tidak berdasarkan i/j (iterasi)
        check = False
        print('\nPerulangan for num in list : '+ str(num) + '\n')      ### num = nomor yang berada di dalam list 1, 2, 3, 2, 5, 2, 7, 2
        
        for freq in countList: ### membuat list di dalam list [num, freq; num, freq; num, freq; dkk]
            print('for freq in countList\t freq=' + str(freq))
            if (freq[0] == num): ####jika list sama dengan num(isi angka di dalam list) maka 
                freq[1] += 1
                check = True
                print('Jika freq[0]/num di perulangan == num di list input maka\t (num, freq[0], freq[1]) ->'  + str(num) + ',' + str(freq[0]) + ',' + str(freq[1]))
                print('countList = ' + str(countList)+ '\n')
        
        if (check == False):
            countList.append([num,0])
            print('Jika freq[0]/num di perulangan != num di list input maka freq=[num,0] -> ' + str(countList))
    
    print('Hasil akhir  perulangan for num in list' + str(countList) + '\n')   ####out: [[1, 0], [2, 3], [3, 0], [5, 0], [7, 0]] -> [list,freq(dimulai dari 0)]

    ###create list of mode/s
    maxFrequency = 0
    modes = []
    for freq in countList:
        print('for freq in countlis -> freq = ' + str(freq))
        if (freq[1] > maxFrequency) :
            modes = [freq[0]]
            maxFrequency = freq[1]
            print('if freq[1] > maxFreq -> (modes, max freq) = ' + str(modes) + ',' + str(maxFrequency))
        elif (freq[1] == maxFrequency):
            modes.append(freq[0])
            print('if freq[1] = maxFreq -> (modes, max freq) = ' + str(modes) + ',' + str(maxFrequency))

    ###if every value appears same amount of times
    if (len(modes) == len(countList)):
        modes = []     
    return modes


print(getMode(x))

#####out : [2]




