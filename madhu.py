# print("1.length of string")
#
# a = str(input("enter the string: "))
# print(len(a))
# print("----end of stmt-----")
#
# print("2.Count characters in string")
#
# b = "saravana"
# print(b.count("a"))
# print("---end of stmt----")
#
# print("3.String slicing")
#
# c = "saravanan"
# print("slicing: ",c[4:])
# print("---end of stmt----")
#
# print("4.Replace first occurance character")
#
# d = str(input("enter the charater: "))
# print(d.replace('m','s'))
# print("---end of stmt----")
#
# print("5.Swapping chars in string")
# def swap(string):
#     return string[-1]+string[1:-1] + string[:1]
# str = input("enter the string: ")
# print(swap(str))
# print("---end of stmt----")
#
# print("6.Append chars to string at end")

# b1 = str(input("enter the first string: "))
# b2 = str(input("enter the second string: "))
# b3 = (b1+" "+b2)
# print("Enter the Append Chars:",(b3))
# print("---end of stmt----")

# print("7.Substring replacement")
# x = "saravanan are good boy"
# print(x.replace("are","is"))
# print("---end of stmt----")
#
# print("8.Length of longest string in python")
#
# str = "saravanan mani"
# print(max(str))
# print("---end of stmt----")

#print("9.nth index character from string")
# int=input("Enter String:")
# print("-3th index value is:",int[-3])

#print("10.First last chars swapping")
# a = str(input("enter the swap char: "))
# print(a[-1:]+a[1:-1]+a[:1])

#print("11.Remove odd index values")
# str=input("Enter a String:")
# str1=""
# i=0
# while(i < len(str)):
#     if(i%2==0):
#         str1=str1 + str[i]
#     i=i+1
# print("str: ",str)
# print(("str1: ",str1))

#print("12.Count words in a string")
# str = input("enter the valure: ")
# x = str.split()
# print(len(x))

#print("13.Upper lower case of a string")

# x = str(input("enter the name: "))
# print(x.isupper())
#
# x1 = str(input("enter the name: "))
# print(x1.islower())

#print("14.Sort unique words alphanumerically")


name = str(input("enter the name: "))
res=name[0]
l = len(name)
mi = int(l/2)
res=res+name[mi]
res=res+name[l-1]
print("first, middle and last worlds: ",res)