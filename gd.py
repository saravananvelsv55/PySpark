# # z = int(input("enter the marks :"))
# # if(z>=35):
# #     print("you are passed")
# # else:
# #     print("you are fail")
# #
# # print("----end the statement------")
# #
# # marks = int(input("enter the marks: "))
# # if (marks >= 35 and marks <=100 ):
# #     print("you are passed")
# # else:
# #     print("you are failed")
# #
# # # n1 = 20
# # # n2 = 30
# # # counter = 19
# # # while n1 <= n2:
# # #     print(n1)
# # #     counter +=1
# # #     if counter == 25:
# # #         break
# # #     n1 += 1
# #
# #
# # x = 50
# # y = 70
# # counter = 0
# # while x <= y:
# #     print(x)
# #     counter += 50
# #     if counter == 60:
# #         break
# #     x += 1
# str = "saravanan"
# dict = {}
# for a in str:
#     keys = dict.keys()
#     if a in keys:
#         dict[a]+=1
#     else:
#         dict[a] = 1
#
# # print(dict)
# #
# #
#
# list1 = [1,3,5,6]
# list2 = [2,4,6,7,8]
#
# list1.append(2.5)
# print(list1)
# list1.append(list2)
# print(list1)
# list1.extend(list2)
# print(list1)
#
# # list = [2,5,6,]
# #
# # list.pop(1)
# # print(list)
#
# name = 'mani'
# x=name.replace('m','s')
# print(x)
#
# a = [1,2,3,4,5]
# a.insert(4,5)
# print(a)
#
# list4 = [1,3,45,6,7]
# list4.remove(3)
# print(list4)

# a=['saravanan','mani','gopi']
# a.remove('gopi')
# print(a)


# name=[1,4,5,6]
# del name[0]
# print(name)

"reverse, sort and insert"

# list = ['saravanan','mani','abi','abdul']
# list.sort()
# print(list)
#
# list1 = ['mani','saravanan']
# list1.reverse()
# print(list1)
#
# list2 = ['mani','saravanan']
# name4 = ['gopi','siva']
# list2.extend(name4)
# print(list2)

# "set"
# name = set(('mani','saravanan','22'))
# print(name)
#
# x = int(input("enter the marks: "))
# if x > 0 and x <= 100:
#     if x >= 35 and x < 90:
#         print("you are passed")
#     if x >= 90:
#         print("you are passed in first class")
# else:
#     print("you are failed")
# print()

# x = int(input("enter the marks: "))
# if x > 35 and x <= 100:
#     if x >= 35 and x < 90:
#         print("You are just Passed")
#     if x >= 90 and x < 94:
#         print("your first class")
#     if x >= 95 and x <100:
#         print("your are college first")
# else:
#     print("you are failed")
#print()
"find the duplicate value"
# string = 'saravanan'
# a = ""
# for name in string:
#     if name not in a:
#         a = a+name
# print(a)


# string = "gandhimathi"
# x = ""
# for name in string:
#     if name not in x:
#         x = x+name
# print(len(x))
# print(x)

#
# string = 'saravanan'
# print(len(string))
#
# name = 'mani'
# print(len(name))

"""list = ["abc","zyx","aba","local","cdc"]"""
#
# list = ["abc","zyx","aea","local","ccd"]
# a = 0
# for x in list:
#     if len(x)>=1 and x[0]==x[-1]:
#         a += 1
#     print(a)
# #
list = ["abc","zyx","aba","local","cdc"]
a = 0
for x in list:
    if len (x)> 1 and x[0]==x[-1]:
        a += 1
print(a)

#string swapping

# name1 = "mani"
# name2 = "saravanan"
# name3 = "rohan"
#
# temp = name1
# name1 = name2
# name2 = name3
# name3 = temp
#
# print("enter the name1: ",format(name1))
# print("enter the name2: ",format(name2))
# print("enter the name3: ",format(name3))
#


# list = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
# def last(n):
#     return n[-1]
# def sort_list_last(tuples):
#     return sorted(tuples,key=last)
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# list = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
# x=list
# def last(x):
#     return x[-1]
# def sort_x_last(tuples):
#     return sorted(tuples,key=last)
# print(sort_x_last(x))
#
# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]
#
#   return str1
#
# print(change_char('saravanan'))

x = input("enter the value: ")
def change_char(x):
    change_char = x
    x = x.replace(change_char,"$")
    x = change_char + x[1:]
print(x)