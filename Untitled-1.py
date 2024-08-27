

apple="harry"
print(apple) 
name="subham shashwat"
print(name)
print("apple,"+name)
print(apple[0])
print(apple[1])
print(apple[2])
print(apple[3])
print(apple[4])
apple="harry"
print(apple)
names="Harry,subham"
print(names[0:4])
#string slicing 
# in string slicing we can pick up any letter from a word and we can make any word after that
# for example
NAMES ="SUBHAM,HARRY"
print(NAMES[0:4])
# so it will print SUBH only


# IF WE HAVE TO PRINT LENGHT OF A STRING WE HAVE TO  US LEN()FUNCTION 
# LENGHT OF A STRING
fruit="mango"
mangolen=len(fruit)
print(mangolen)
print(fruit[0:4])
print(fruit[:3])
print(fruit[1:4])
print(fruit[0:-3])
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])
# quick quiz
nm="harry"
print(nm[-4:-2])
# for character code we use (n-1) principle


#"STRINGS METHOD PROVIDE A SET OF BUILT IN WE CAN USE ALTER OR MODIFY THE STRING"
# upper()method convert each and every thing into upper case.
# lower() method convert each and every thing into lower case.
a="Subham Shashwat"
print(len(a))
print(a.upper())
print(a.lower())
# strip()method removes any white spaces before and after the string 
str1="  welcome  "
print(str1.strip)
# restrip method ()will remove all trailing charcater 
a="harry!!!!"
print(a.rstrip("!") )
# the replace()method repalces all occurences of a string with another string 
str2="silver spoon"
print(str2.replace("sp","m"))
# split()method splits the given the string at the specified instances andn returns the separated strings as list items 
str2="silver spoon"
print(str2.split(" "))
# the capitalize()method turns only first charcater into upper case and rest of the character of the string are being turned to lower case
str1="SILver"
capStr1=str1.capitalize()
print(capStr1) 
str2="HEllo World"
CapStr2=str2.capitalize()
print(CapStr2)
# The centre()method alligns the string to the centre as per the parameter given by the user 
str1="welcome to console"
print(str1.center(90))
# we can also provide the caracter (".") in between 
print(str1.center(50,"."))
# count()method the number of times the given value has been occured
str2="Abracgderaaah"
countstr= str2.count("a")
print(countstr)
# endswith()method checks if the string end up with gievn value or not. if yes then true or else return to false 
str1="welcome to the console !!!"
print(str1.endswith("!!!"))
str2="welcome to the console..."
print(str2.endswith("!!!"))
# find()method searches for the first occurnece of the given value and returns the index where it is present 
str1= "my name is subham . i am an honest man "
print(str1.find("is"))
# index()method searches for the first occurnec of the given value and returns the index where it is present
str="he is piyush kumar. piyush is an honest man "
print(str.index("piyush"))
# isalnum()method returns true only if the entire string only consists of A-Z,a-z,0-9.if any other character and punctuation are prrsent , then it returns false
str1="welcometotheworldbaby"
print(str1.isalnum())
# islapha() method returns ture only . if the entire string consist of A-Z,a-z.IF any other chacater or punctuation or number (0-9)are present then it will be false.
str1="Welcometoranchi"
print(str1.isalpha())
# islower() method returns TRue if all the character in the string are lower case, else it returns false 
str1="hello wolrd"
print(str1.islower())
# isprintable()method returns true if all the value within the given strings are printable,if not then t=returns false?
str1="we are living happy in this world"
print(str.isprintable())
# issapce() method returns true only and only if the string conating white spaces, else returns false



# istitle ()returns true only if the first letter of each word of the string is captilalized 
str1="World Health Organization"
print(str1.istitle())
str2="we are not thE Best"
print(str2.istitle())
# isupper()method retuns true i all the character in the string are upper case ,else it returns False
str1="WORLD HEALTH ORGANIZATION"
print(str1.isupper())
# startwith()method check whether string start with given value or not . if Yes then true else returns false
str1="python is a INterpreted language"
print(str1.startswith("python"))
# swapcase()method changes the character casing of the string .
str1="python is a interpreted language "
print(str1.swapcase())
str2="Python IS A VERy Good LANGUAGE"
print(str2.swapcase())
# title() method captalizes each letter of the world within the string 
str1="he is a very good boy and his name is SUBHM "
print(str1.title ())
txt=" "
x=txt.isspace()
print(x)


#14(if and else condtional statement in python)
# IF THE GIEVN INPUT IS TRUE THEN IT WILL FALL UNDER "IF"STATEMENT OTHERWISE IT WILL FALL UNDER ELASE STATEMENT
a=int(input("enter your age:")) 
print("your age is;",a) 
#conditinal operators
#<, >, >=,<=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if (a>18):
    print("you can drive")
    print("yes")
else:
    print("you cannot drive")
    print("no")
    print("yes")
    
b=int(input("enter your budget"))
print("your budget is;",b)
if(b>1800):
    print("you an buy a pair of nike shoes")
    print("yes")
else:
    print("you cannot buy a pair of nike shoes")
    print("error")
appleprice=10
budget=200
if(budget-appleprice > 50):
    print("Alexa, add 1kg Apples to the cart.")
else:
    print("Alexa,do not add apples to the cart.")
# elif STATEMENT(some times programmer wants to evaluate more than one condition,and this can be done using an elif  statement)
num=int(input("enter the value of num: "))
if(num<0):
    print("number is negative")
elif(num==0):
    print("number is zero")
elif(num==999):
    print("number is special")
else:
    print ("number is postive.")
    print("I am Happy now ")

# num=0
# if (num<0):
#     print("number is negative .")
# elif(num==0):
#     print("number is zero")
# else:
#     print("number is postive")
# # nested if statement
# # we can use if, if else ,elif statement inside other if sttemnet as well 
# num=18
# if (num<0):
#     print("number is negative")
# elif(num>0):
#     if num(num<=10):
#         print("number is between 1-10")
#     elif (num>0):
#         if(num<=10):
#             print("number is between 1-10")
#         elif(num>10 and num<=20):
#             print("number is between 11-20")
#         else:print("number is greater than 20")
#     else:
#         print("number is zero")
# FOR LOOPS IN PYTHON 

name = "Abhishek"
for i in name:
    print(i)
if (i =="b"):
    print("This is something special!")
colors=["red","green","blue","yellow"]
for color in colors :
    print(color)
    for (i) in color:
        print(i)
# Range loop (): range function helps in printing a loop for whatever range we want
# loop:- matlv ek ek karke sab print hoga 
for k in range (8):  
    print(k)
    for x in range(9, 200):
        print(x)
for y in range (1,8,2):
            print(y)
            for n in range (1,12,3):
                 print(n)
                 for z in range (1,12,2):
                      print(z)
                #  start = 1
                # condition =<12
                # increment= 
                 for l in range (1,11):
                      print("2*",l,"=",2*l)
                    #   reverse range funtion 
for s in range(10,0,-1):
    print(s)
    # 1.
    for t in range (100,-1,-2):
         print(t)
         for v in range (1,11):
              print("2*",v,"=",2*v)
              for b in range (1,11):
                   print("2*",b,"=",2*b)
# string function 

w="welcome"
n=w.lower()
print(n) 
y="MY NAME IS SUBHAM SHASHWAT"
u=y.lower()
print(u)
i="subham shashwat"
o=i.upper()
print(o)
p="Welcome to Wscubetech"
k=p.title()
print(k)
l="welcome to wscubetech"
h=l.capitalize()
print(h)

# python string function
# find(it helps in finding the postion of letter )
w="welcome"
print(w.find("e"))
print(w.find('el'))
print(w.find('e'))
print(w.find('e',2))
print(w.find('z'))
# index= agar isme ka letter string mein nahi hota hai tab wo error de deta hai 
w="welcome "
print(w.index('e'))
# isalpha= (agar isme alphabet hoga tab hee true hoga nahi ti false ho jaayega)
w="welcome"
print(w.isalpha())
v="welcome 1,2,3"
print(v.isalpha())
# Isdigit=(isme agar koi digit hoga tab hee ye true hoga nahi to false ho jayega)
z="1,2,3,4,5"
print(z.isdigit())
# isalnum=(isme koi bhi digit ho ya alphabets ho , wo true hee hoga)
e="welcome 123"
print(e.isalnum())
v="welcome @123"
print(v.isalnum())

# ord()and chr()python function 
# this takes in an intergers 'i'and converts it to a character c,so it returns a character string
# Converts intergers 65to ASCII chacter ('A')
# y=chr(65)
# print(type(y),y)
# example
a=65
print(chr(a))

a=66
print(chr(a))

# ord()function:-
# this takes a single unicode character (string lenght 1) and returns an integers , so the format is :
# convert ASCII unicode character 'A' to 65
# y=ord('A')
# print(type(y),y)
# example
h='A'
print(ord(h))

# PYTHON STRING ()METHOD

# the format ()method fromats the specified value (S)and insert them inside the string's placeholder .
# the place holder is defined using curly brackets :{}

txt1="welcome to {fname}{lname}".format(fname="wscube tech", lname="TECH")
print(txt1)
txt2="welcome to {0}{1}".format("wscube","tech")
print(txt2)
txt2="welcome to {}{}".format("wscube","tech")
print(txt2)

# EXAMPLE
w="welcome{}to{}wscubetech".format("hello","20")
print(w)

w="welcome {b:>10}to {a}wscubetech".format(a=30,b=40)
print(w)

# logical important
# --------10{b:10}
# 10--------[b:<10]
# ----10----[b:^10]
# --------10[b:>10]

# LIST[] DATA TYPE 
# This data types are changable {mutable}"data delete ya change ho sakta hai "
l=[1,2,3,4,5]
print(type(l))
print(l[2])
#MIX list :-
l=[2,3,"hello",[3,4,5]]
# Q1:how to get "hello"
print(l[2])
# how yo get "4"
print(l[3][2])
#Q3:How to get'3'from list ?
print(l[0:2])
# EXAMPLE

l=[1,2,3,4,5,6]
print(l[0:6:2])

l=[1,2,3,4,5,6,]
print(l[-1: :-1])

# LIST [data types] are Mutable ,[] , multiple values 

l=[10,30,40,50,"hello"]
print(l[2],l[4])
print(l[0:2])
print(l[0::2])
print(l[3:])
print(l[-1::-2])
print(l[-1: :-1])

# LIST ITERATION=mtlb hota hai ki agar list mee 10 elements hai to unko alag alag karke kaise dekhe 
l=[10,20,30,40,50]
t=len(l)
print(t)
for n in range (t):
     print(l[n])
    #  2nd method = for how to do list iteration using loop
for a in l:
     print (a)   
# revrse Iteration :-
l=[20,40,90,80 ]
t=len(l)  
for n in range (t-1,-1,-1):
     print(l[n]) 
 
l=[10,20,30,40,50,60]
t=len(l)
for n in range (t-1,-1,-1):
     print(l[n])

# LIST COMPREHENSION :-
# list comprehension is an elegnat way to define and create list based on existing lists 
# list comprehenion is generally more compact and faster than normal funtion and loops for creating list 
# example 
l=[]
for a in range (1,101):
     l.append (a)
     print(l)
     n=[m for m in range (1,101)]
     print(n)
     n=[h for h in range (1,101)if h%2==0]
     print(n)
s="hello"
d=[g for g in s]     
print(d)

# 29 list function
# function for delete element from list 
l=[20,30,40,50]
print(l)
#DELETE FUNCTION 
L=[20,30,40,50]
del l[1]


# now we are performing "pop" function
# there is a very big difference between "POP"&"del" function as "pop"function can also return the deleted term but "del"function does not return any deletd term 
# example :-1
K=[20,30,40,50]
K.pop(2)
print(K)

# NOW WE ARE PERFORMING "REMOVE" FUNCTION 

list=[50,70,80,90]
list.remove(70)
print(list)

# Now we are performing "clear screen " function:-

# list=[10,20,30,40,50]
# list.clear(3)
# print(list) 

# NOW WE ARE PERFROMING "UPDATE LIST FUNCTION " :-
L=[20,30,40,50]
L[0]=90
print(L)
# yaha par "0"postion pe 90 insert ho jaayega 

# INSERT FUNCTION :-
L=[20,30,40,50]
L.insert(0,10)
print(L)
 
#  append()fumction:-
# ye values hamesha append hoga mtlv iska hamesha addition hota hai 
L=[20,30,40,60]
L.append(70)
print(L)

# EXTEND FUNCTION :-
# extend function is differnet 
l=[20,30,40,50]
n=[70,60]
l.append(n)
print(l)


# MORE LIST FUNCTION :-
# 1.> count() ye function kitne number of times wo value aaya hai list mein usko bata deta hai 
L=[10,20,30,40,10,10,10,10]
a=L.count(10)
print(a)

# 2.> max() highest value dega aapke list ka 
L=[10,20,30,89,99]
m=max(L)
print(m)

# aplhabetical case :-
n=['hello','world']
D=max(n)
print(D)

# 3.>min()function :-
L=[10,20,30,40,70,80]
h=min(L)
print(h)
#  and alphabet ke kam number pe jo aata hai wo aayega phele 

l=['hello','world']
print(min(l))

# sort function
#  SORTING KARME ME HELP KARTA HAI 
L=[10,20,30,40]
L.sort()
print(L)

# REVERSE FUNCTION 
L=[10,20,30,40,50,60,99,88,676,6799]
L.reverse()
print(L)

# INDEX function 
L=[10,20,30,40,50]
a=L.index(20)
print(a)


# ZIP FUNCTION:- {same time pe '2' list ko iterate karna hai }
L=[10,20,30,40]
L1=[2,3,4,5,6,7]
for a,b in zip(L,L1):
     print(a,b)
#  programe to convert string to a list:-

n=input("enter the value")
print(n)
L=n.split()
print(L)
# user define module 
# 1.simple function
# 2.return type function 
# 3.function with argument






























# var=input("enter your name " ,)
# var1=input("enter your age ",)
# print("My name is", var, "my age is ",var1)
# print(f"my name is {var}and my name is {var1}")

value1=value2=value3="hello"
print(value1)
print(value2)
print(value3)
#assign value to varible and print again 
value1=99
value2="hello world"
value3="hello python"
print(value1)
print(value2)
print(value2)