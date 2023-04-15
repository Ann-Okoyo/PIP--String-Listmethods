message= "Ann is the best in Python"
print(message)


text="I love Python"
print(text)

text2="smart lady"
text3=text2.capitalize()
print(text3)

class3 ="ANITA B"
class4=class3.casefold()
print(class4)

# 
# count()	Returns the number of times a specified
# value occurs in a string  
class6 = "5 ,6 ,5, 5 ,9,7,4"
class7=class6.count("5")
print(class7)

class8 ="7, 8, 9, 9, 9, 9,2"
clas10=class8.count("9")
print(clas10)


# encode()	
# Returns an encoded version of the string
text8 ="smart people work hard"
text9=text8.encode()
print(text9)

text10="Hardwork beats talent"
text11=text10.encode()
print(text11)

# endswith()	Returns true if the string 
# ends with the specified value
text12="Coding needs practice"
text13=text12.endswith("practice")
print(text13)

text14="She codes"
text15=text14.endswith("coding")
print(text15)


# find()	Searches the string for a specified value and
#  returns the position of where it was found
# name="I love to play music a lot."
# namex =name.find()
# print(namex)

nlis = ['python',3.14,2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print(nlis)
print(len(nlis))

# slicing 
print(nlis[0:2])
print(nlis[8:13])
print(nlis[2:4])

# extend
print(nlis.extend(["smart","big ","happy"]))


list = ["Ann","Joan","Cynthia"]
list.append("Jeff")
print(list)

fruits = ["Banana","Apple","Mango","Banana"]
fruits2=fruits.append("Strawberries")
print(fruits2)


#insert 
clothes =["skirt","dress","top","shirt"]
clothes2=clothes.insert(4,3)
print(clothes2)


