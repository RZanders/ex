# x = int(input("ievadi skaitli!"))
# y = int(input("ievadi skaitli!"))

# if x > y:
#     print(x-y)
# else:
#     print(y-x)

# X1  = int(input('Enter value for X-axis :'))
# Y1 = int(input('Enter value for Y-axis :'))


# if X1 > 0 and Y1 > 0:
#     print('1.kv')

# elif X1 < 0 and Y1 > 0:
#     print('2.kv')

# elif X1 < 0 and Y1 < 0:
#     print('3.kv')

# elif X1 > 0 and Y1 < 0:
#     print('4.kv')
# else: 
#     print('plakne')

# x = 123
# sum = 0

# while x > 0:
#     pedejaisCipars = x % 10
#     sum += pedejaisCipars
#     x = x // 10
# print(sum)

# class taisnsturis:
#     def __init__(self, a, b):
#         self.b = b
#         self.a = a
    
#     def laukums(self):
#         return self.a * self.b
    
#     def perimetrs(self):
#         return self.a * 2 + self.b * 2
    
# jaunsTaisnsturis = taisnsturis(12, 10)
# print(jaunsTaisnsturis.laukums())
# print(jaunsTaisnsturis.perimetrs())

# class skaitli:
#     def __init__(self, a, b, c, d, e):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.e = e
#     def summa(self):
#         return self.a + self.b + self.c + self.d + self.e
#     def videjais(self):
#         return (self.a + self.b + self.c + self.d + self.e) / 5

# nez = skaitli(12, 31, 2, 55, 13)
# print(nez.summa())
# print(nez.videjais())

# n = input("ievadi divciparu skaitli:")
# x = ""
# for i in range(1, -1, -1):
#     x += n[i]
# print(x)

# n_reversed = n[::-1]

# print(int(n) + int(n_reversed))


# n = int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# n = int(input("n: "))
# for i in range(n):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()


# 69.uzd

# def printArray(m):
#     for row in m:
#         for elem in row:
#             print(elem, end=" ")
#         print()

# arr = [[0 for _ in range(8)] for _ in range(8)]


# burts = "abcdefg"
# poz = input("pozicija: ")
# y = burts.index(poz[0])
# x = 8 - int(poz[1])
# arr[x][y] = 1

# tornis

# for i in range(8):
#     for j in range(8):
#         if i ==x or j == y:
#             arr[i][j] += 1
            
# laidnis

# for i in range(8):
#     for j in range(8):
#         if i + j == x + y or i - j == y:
#             arr[i][j] += 1

# dāma

# for i in range(8):
#     for j in range(8):
#         if i + j == x + y or i - j == x - y or i==x or j ==y:
#             arr[i][j] += 1

# karalis

# for i in range(8):
#     for j in range(8):
#         if abs(x-i) <= 1 and abs(y-j) <= 1:
#             arr[i][j] += 1

# zirgs

# for i in range(8):
#     for j in range(8):
#         if (abs(x-i) == 1 and abs(y-j) == 2) or (abs(x-i)==2 and abs(y-j) == 1):
#             arr[i][j] += 1

# printArray(arr)

# 70.uzd

# mas = [2, 5, 7, 2, 7, 1, 4, 9, 2]
# n = 3
# print('\n'.join(' '.join(map(str, mas[i:i+n])) for i in range(0, len(mas), n)))

# 19.uzd

# mas = int(input("ievadi skaitli"))
# for i in range(mas):
#     if i**2<mas:
#         print(i**2)
#         i+=1

# 30.uzd

# n = int(input("ievadi skaitli:"))
# for i in range(n+1, 2*n):
#     print(i)

# atzimes =[]
# for i in range(7):
#     row = []
#     atz = int(input("ievadi atzimi" + str(i) + "skolenam"))
#     while atz !=0:
#         row.append(atz)
#         atz = int(input("ievadi atzimi" + str(i) + "skolenam"))
#     atzimes.append(row)

# 17.uzd

# num = int(input("ievadi skaitli:"))
# i = 1
# while i < num:
#   print(i)
#   i += 1


# class paralelskaldnis:
#     def __init__(self, a, b, h):
#         self.a = a
#         self.b = b
#         self.h = h


# 27.uzd

# n = int(input("sk: "))
# while n != 0:
#     m = int(input("sk: "))
#     if m > n:
#         print("Lielāks")
#     else:
#         print("Nav lielāks")
#     n = m

# 41.uzd
# m = [2, 5, 7, 2, 13, 7, 1, 4, 9, 2, 1, 5, 7, 9, 3, 6, 9, 9]
# diction = {}

# for num in m:
#     diction[num] = m.count(num)

# # print(diction)

# sorted_list = sorted(diction, key = diction.get)

# print(sorted_list[-1])


# 44.uzd
# m = [2, 5, 7, 2, 13, 7, 1, 4, 9, 2, 1, 5, 7, 9, 3, 6, 9, 9]
# print("Original List: ", m)
# res = [*set(m)]
# print("List after removing duplicate elements: ", res)


# 45.uzd
# text = "The Serbian tennis star was detained in January over his refusal to be vaccinated against Covid. He was deported from the country 10 days later, despite mounting a successful legal challenge. At times dubbed Fortress Australia, the country had some of the strictest pandemic restrictions in the world. When Djokovic arrived in Australia in January, Covid cases were skyrocketing and government rules required anyone entering the country be vaccinated, unless they had a valid medication exemption."
# text = text.lower()
# text = text.replace(".","").replace("!","").replace(",","").replace(" ","")

# d={}
# import string
# for char in string.ascii_lowercase:
#     d[char] = round(text.count(char) / len(text) * 100, 2)

# for key in d:
#     print(key, d[key])

