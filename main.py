#
# print ("1. Python Program to calculate the length of a string?")
# a = 'SARAVANAN SAMBANDAM'
# print("length of string function :",len(a))
#
# b = 'shankar'
# print("length of string function :",len(b))
#
# print("____end-of-statment___")
#
# print ("2.Python Program to sum all the items in a list?---")
# list = [12,15,55,66,77,88]
# total=sum(list)
# print('total number in list :',total)
#
# print(min(list))
# list2 = [249,555,666]
# total=sum(list2)
# print('total number in list :', total)
#
# print("----end of stmt--------")
# print("3.python program to multiple all the items in a list?----")
# from functools import reduce #adding the function tools
#
# list4 = [4,7,8] # list
# list_product = reduce ((lambda x,y:x*y),list4)
# print("multiple the numbers: ",list_product)
#
# print("--End of Stmt----")
#
# print("4.python program to get the largest number from the list")
# list5 = [1,2,3,4,5,6]
# print(max(list5))
# print("--End of Stmt----")
#
# print("5.Write a Python program to get the smallest number from a list.")
# list6 = [0,12,3,4,5,5,66,]
# print(min(list6))
# print("--End of Stmt----")
#
# print("6.Write a Python program to count the number of characters in a string\Sample String.")
# string = "SARAVANAN SAMBANDAM";
# count = 0;
# for a in range(0,len(string)):
#     if(string[a]!=""):
#         count = count+1;
# print("total string count : "+str(count));
#
# # first statment
# print("7. Write a Python program to count the number of characters (character frequency) in a string.  Sample String : google.com'")
# def char_frequency(name):
#     dict = {}
#     for i in name:
#         keys = dict.keys()
#         if i in keys:
#             dict[i]+=1
#         else:
#             dict[i]=1
#     return dict
# print(char_frequency('google.com'))
# # second stmt
# print("--------6 stmt -------------")
#
# str = 'mani raju'
# dict = {}
# for a in str:
#     keys = dict.keys()
#     if a in keys:
#         dict[a]+=1
#     else:
#         dict[a]=1
# print(dict)
# print("--End of Stmt----")
#
# print("8.count the number of strings where the string length is 2 or more and the first and last character are same from a given "
#       "list of strings")
# list = ["abc","zyx","aba","local","cdc"]
# a = 0
# for x in list:
#     if len (x)> 1 and x[0]==x[-1]:
#         a += 1
# print(a)
#
# print("--End of 8 Stmt----")

#print("9.Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of "
      # "non-empty tuples.  "
      # "Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]")
# list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# x=list
# def last(x):
#     return x[-1]
# def sort_x_last(tuples):
#     return sorted(tuples,key=last)
# print(sort_x_last(x))
#
# print("-----end of 9 stmt---------")

#print("10.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string. ")

#
# x = str(input("enter the name: "))
# def x_both_end(x):
#     if len(x) < 2:
#         return ""
#     return x[0:2] + x[-2:]
# print(x_both_end(x))
# print("----------end of 10 stmt------------")

# b=str(input("enter the value: "))
# def b_both_ends(b):
#     if len(b) < 2:
#         return ""
#     return b[4:6] + b[-4:-2]
# print(b_both_ends(b))

#print("11.Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.")
#
# x = str(input("enter the value: "))
# def change_char(x):
#     char = x[0]
#     x = x.replace(char,'$')
#     x = char+x[1:]
#     return x
# print(change_char(x))

#print("12.Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string")
"""
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' """
# x = str(input("enter the value: "))
# y = str(input("enter the value: "))
# def chars_mix_up(x,y):
#     x1 = y [:2] + x[2:]
#     y1 = x [:2] + y[2:]
#
#     return x1+' '+y1
# print(chars_mix_up(x,y))

# print("13.Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.")
#
# x = str(input("enter the value: "))
# a = len(x)
# if a > 2:
#     if x[-3:]=="ing":
#         x += "ly"
#     else:
#         x +='ing'
# print(x)

#
# print("14.Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  ")
#
# x = str(input("enter the value: "))
#
# def poor_not(x):
#     a = x.find("poor")
#     b = x.find("not")
#     if a > b and a > 0 and b > 0:
#         x = x.replace(x[a:(b+4)],"good")
#         return x
#     else:
#         return x
# print(poor_not(x))

print("15.Python function that takes a list of words and returns the length of the longest one")
#
# name = str(input("enter the name: "))
# def word_length(name):
#     for a in name:
#         word_length((len(a), a))
#     word_length.sort()
#     return word_length[-1][0], word_length[-1][1]
# print()


#print("16.")
