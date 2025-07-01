# a=5
# b=1
# print(a,'+',b,'=',a+b)
# print(f'{a} + {b} = {a+b}')
# rint(f'{a} - {b} = {a-b}')
# print(f'{a} * {b} = {a*b}')
# print(f'{a} / {b} = {a/b}')

# ---------------------------------------------------------------------------------------------------------------------

# a=int(input('yakum adad'))
# b=int(input('duyum adad'))
# print(f'{a} + {b} = {a+b}')
# print(f'{a} - {b} = {a-b}')
# print(f'{a} * {b} = {a*b}')
# print(f'{a} / {b} = {a/b}')
# print(f'{a} // {b} = {a//b}')

# ----------------------------------------------------------------------------------------------------------------------

# import math
# a=int(input())
# a1=a//1000
# a2=a//100%10
# a3=a//10%10
# a4=a%10
# print(f'{a4}{a3}{a2}{a1}')

# ----------------------------------------------------------------------------------------------------------------------

# n=int(input())
# soat=n//60%24
# minut=n%60
# print(f'{soat} {minut}')

# -----------------------------------------------------------------------------------------------------------------------

# import math
# a=int(input())
# ss=a//3600%24
# daq=a//60%60
# son=a%60
# print(f'{ss}:{daq//10}{daq%10}:{son//10}{son%10}')

# ------------------------------------------------------------------------------------------------------------------------

# a=16
# print(a**(1/2))

# ------------------------------------------------------------------------------------------------------------------------

# import math
# a = input ()
# b = input ()
# x=a
# t=b
# print (t, x)

# -------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# if a>0 and a%2==0:
#     print("positive and even")
# elif a<0 and a%2!=0:
#     print('negative and odd')
# elif a>0 and a%2!=0:
#     print('positive and odd')
# elif a<0 and a%2==0:
#     print('negative and even')

# -------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# if a%5==0 and a%3==0:

#     print('Hello World')
# elif a%3==0:
#     print('Hello')
# elif a%5==0:
#     print('World')

# -------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# b=int(input())
# if a%b==0 and b%a==0:
#     print('YES')  
# elif a%b!=0 and b%a!=0:
#     print('NO')

# -------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# sym=input()
# b=int(input())
# if sym == '+':
#     print(f'{a}{sym}{b}={a+b}')  
# if sym == '-':
#     print(f'{a}{sym}{b}={a-b}') 
# if sym == '*':
#     print(f'{a}{sym}{b}={a*b}') 
# if sym == '/':
#     print(f'{a}{sym}{b}={a/b}') 
# if sym == '%':
#     print(f'{a}{sym}{b}={a%b}') 

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# b=int(input())
# c=int(input())
# poz=0
# neg=0
# zero=0
# if a>0 : poz+=1
# if b>0 : poz+=1
# if c>0 : poz+=1
    
# if a<0 : neg+=1
# if b<0 : neg+=1
# if c<0 : neg+=1 

# if a==0 : zero+=1
# if b==0 : zero+=1
# if c==0 : zero+=1   

# print(f'zero = {zero} pozitive = {poz} neg = {neg}')

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# sym=input()
# b=int(input())
# match sym:
#     case '+':
#         print(a+b)
#     case '-':
#         print(a-b)    
#     case '-':
#         print(a-b) 
#     case '-':
#         print(a-b) 

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())

# match a:
#     case 1:
#         print('Dushanbe')
#     case 2:
#         print('Seshanbe')
#     case 3:
#         print('Chorshanbe')
#     case 4:
#         print('Pashjshanbe')
#     case 5:
#         print('Juma')
#     case 6:
#         print('Shanbe')

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())

# match a:
#     case 1:
#         print('Yanvar')
#     case 2:
#         print('Seshanbe')
#     case 3:
#         print('Chorshanbe')
#     case 4:
#         print('Panjshanbe')

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# b=int(input())
# if a>b:
#     print(1)
# elif b<a:
#     print(2)
# else:
#     print(0)

# --------------------------------------------------------------------------------------------------------------------------

# x=int(input())
# y=int(input())

# if (x>0 and y>0):
#     print(1)
# elif(x<0 and y>0):
#     print(2)
# elif(x<0 and y<0):
#     print(3)
# else:
#     print(4)

# --------------------------------------------------------------------------------------------------------------------------

# i=10
# while i>=0:
#     print(i,end=' ')
#     i-=1

# print()

# i=0
# while i<=10:
#     print(i,end=' ')
#     i+=1

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# i=0
# sum=0
# while i<=a:
#     sum+=i
#     i+=1
# print(sum)

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# sum=0
# while a>0:    
#      sum+=a%10
#      a=a//10
# print(sum)

# --------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# i=1
# sum=1
# while i<=a:
#     sum*=i
#     i+=1
# print(sum)

# --------------------------------------------------------------------------------------------------------------------------

# for i in range(2,20,3):
#     print(i)

# n=int(input())
# sum=1
# for i in range(1,n+1):
#     sum*=i
# print(i)

# --------------------------------------------------------------------------------------------------------------------------

# n=int(input())

# for i in range(1,11):
#     print(f'{n}*{i}={n*i}')

# --------------------------------------------------------------------------------------------------------------------------


# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# --------------------------------------------------------------------------------------------------------------------------

# n=int(input())
# for i in range(2,n+1):
#     if n%i==0:
#         print(i)
#         break

# --------------------------------------------------------------------------------------------------------------------------

# n=int(input())
# for num in range(1,n+1):
#     print(num,": ",end='')
#     for d in range(1,num+1):
#         if num%d==0:
#             print(d,end=' ')
#     print()

# --------------------------------------------------------------------------------------------------------------------------

# a=[1,2,3,4,5,'text',3.6,True]
# a[3]='hello'  

# for i in range(len(a)):
#     print(a[i])

# --------------------------------------------------------------------------------------------------------------------------

# a=[1,1,2,3,4,5,3,'Amon']

# a.append(6) sar pasledni nevd adad

# a.clear() Udalit kekht

# b=a.copy

# print(a.count(1)) isob kekht cond piv yafch arrayand

# b=[2,3,4]
# a.extend(b)--->>>b dob chud ar a davom
# print(a)

# print(a.index('Amon'))---->>>indexce muayan chud

# a.insert(0.3)
# print(a)


# a=[2,'test',4.8,False]

# # a.append('Hello')
# # print(a)

# b=[False,4.8,'text',2]
# a.extend(b)
# print(a)

# a=[]
# n=int(input())
# for i in range(1):
#     s=input()
#     a.append(s) 
# print(a)
    
# --------------------------------------------------------------------------------------------------------------------------

# jush=('Amon',23,'Dushanbe')
# name,age,city=jush           archidom print cakine ik veta zivevd
# print(age)

# --------------------------------------------------------------------------------------------------------------------------

# fakh=(1,2,3,4,5)

# for i in fakh:
#     print(i)

# for i in range(len(fakh)):
#     print(fakh)

# --------------------------------------------------------------------------------------------------------------------------

# lst=[1,[2,[3,[4,[5],6],7],8],9]
# lst=[1][1][1][2]=7      dam 6 am zokhtkhu dam joyteyam 7 nevd
# print(lst)

# --------------------------------------------------------------------------------------------------------------------------

# lst=[1,2,3,4,5]
# for i in range(len(lst)-1,-1,-1): #yakum -1(az ziboyaf ze) duyum -1 (to damec go 0) seyum -1(har yak krug -1 keyat te tu jushte)
#     print(lst[i])

# --------------------------------------------------------------------------------------------------------------------------

# lst=[1,2,3]
# for i in range(len(lst)):
#     print(lst[i]**2)

# --------------------------------------------------------------------------------------------------------------------------

# lst=[1,2,1]
# lst1=[1,2,1]
# for i in range(len(lst)):
#    lst.reverse()
#    if reversed==lst:
#     print('No palindrom')
#    elif lst==lst1:
#      print('palindrom')

# --------------------------------------------------------------------------------------------------------------------------

# myset={1,2,3,4}
#                 faqiyat  index nadorad elementhora unikalne mekunad (yane ipivat vam dinivisht tayor digata arcond piv canivishe yata best)
# myset={3,4,5,6} 
# discard--- udalit


# --------------------------------------------------------------------------------------------------------------------------

# lst1=[1,2,3,4,4]

# lst2=[1,2,3,4,5]

# set1=set(lst1)  

# if(len(set1)==len(lst1)):
#     print(False)
# else:
#     print(True)

# --------------------------------------------------------------------------------------------------------------------------

# my_amon={
#     'Name':"Ali",
#     'surname':"Valiev",
#     'age':21
# }

# lst1=[1,2,3]
# lst2=[2,4,6]                                                                                                    
# mdict={}

# for i in range(len(lst2)):
#     mdict[lst1[i]]=lst2[i]

# mdict[lst1[0]]=lst2[0]
# mdict[lst1[1]]=lst2[1]
# mdict[lst1[2]]=lst2[2]

# print(mdict)

# n=int(input())

# mdict={}
# for i in range(1,n+1):
#     mdict[i]=i**2
# print(mdict)


# n=int(input())
# mdict={}
# for i in range(n):
#     a=input("enter key ")
#     b=input('enter value ')
#     mdict[a]=b
# print(mdict)

# mdict={}
# a=input()
# for i in range(len(a)):
#     mdict[a]=len(a)
# print(mdict)

# fruits=['apple','banana',"orange"]                                                                                                   
# mdict={}
# for i in range(len(fruits)):
#     mdict[fruits[i]]=i
# print(mdict)

# mdict={
#     'a':4,
#     'b':9,
#     'c':6,
#     'd':11
# }
# items=mdict.items()
# max_key=''
# max_value=0
# for i in items:
#     if i[1]>max_value:
#         max_value=i[1]
#         max_key=i[0]
# print(max_key)


# mdict={
#     'a':4,
#     'b':9,
#     'c':6,
#     'd':11
# }
# items=mdict.items()
# sum=0
# for i in items:
#     sum+=i[1]
# print(sum)

# string='hello'
# for i in range(1,4,2):
#     print(string[i],end=' ')

# --------------------------------------------------------------------------------------------------------------------------


# string='heLlo hello world'

'__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
'__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 
'upper', 'zfill'
# a=string.upper() gula kekht arfen 
# print(a)
# lst=['a','b','c','d']
# str1=' '.join(lst)
# print(str1)


# cars={'8585AB04':'Rang Rover',
#       "0008DD04":'Prado 2'     
# }
# while True:
#     n=input('Choose the action: ')
#     match n:
#         case 'add':
#             key=input('Enter number of car you want to add: ')
#             value=input('Enter model of your car:')
#             cars[key]=value
#             print(cars)
#         case 'Update':
#             key=input("Enter car number you want to update: ")
#             if key in cars:
#                  value=input('Enter new model of your car:')
#                  cars[key]=value
#                  print(cars)
#             else:
#                 print('There is no car with this number!')
#                 print(cars)
#         case 'show all':
#             print(cars)
#         case 'Show':
#             key=input('Enter car number you want to see: ')
#             if key in cars:
#                 print(cars[key],key)
#             else:
#                 print('There is no car whith this number!')
#         case 'Delete':
#             key=input('Enter car number you want to delete: ')
#             if key in cars:
#                 cars.pop(key)
#                 print('Deleted successfully.')
#             else:
#                 print('There is no car whith this number!') 

# --------------------------------------------------------------------------------------------------------------------------

# lst=[]
# id=1
# while True:
#     n=int(input('''
# 1 ---> add new student
# 2 ---> get list of student
# 3 ---> get by id
# 4 ---> update by id
# 5 ---> delete by id
# 6 ---> exit
#     choose your option --> '''))
#     mdict={}
#     if n==1:
#         name=input('enter name of student -> ')
#         surname=input('enter surname of student -> ')
#         age=input('enter age of student -> ')
#         course=input('enter course of student -> ')
#         mdict={
#             'id':id,
#             'name':name,
#             "surname":surname,
#             'age':age,
#             'course':course
#         }
#         id+=1
#         lst.append(mdict)
#         print('new student added sucsessifully ')
#     if n==2:
#         for i in lst:
#             print(f'''
# id        ---> {i['id']}
# name      ---> {i['name']}
# surname   ---> {i['surname']}
# age       ---> {i['age']}
# course    ---> {i['course']}

# -----------------------------------
# ''')
#         if n==3:
#             bol=True
#             id1=int(input('enter id of student for get --> '))
#             for i in lst:
#                 if i['id']==id1:
#                     bol=False
#                     print(f'''
# id        ---> {i['id']}
# name      ---> {i['name']}
# surname   ---> {i['surname']}
# age       ---> {i['age']}
# course    ---> {i['course']}

# -----------------------------------
# ''')
#         if bol==True:
#             print(f'id {id} not found ')

#     if n==4:
#         bol=True
#         id1=int(input('enter id of student for update --> '))
#         for i in lst:
#             if i['id']==id1:
#                 bol=False
#                 name=input('enter name of student -> ')
#                 surname=input('enter surname of student -> ')
#                 age=input('enter age of student -> ')
#                 course=input('enter course of student -> ')
#                 i['name']=name
#                 i['surname']=surname
#                 i['age']=age
#                 i['course']=course

#--------------------------------------------------------------------------------------------------------------------------

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# # factorial(5)=5*factorial(4)
# # factorial(5)=5*factorial(3)
# # factorial(5)=5*factorial(2)
# # factorial(5)=5*factorial(1)
# # factorial(1)=1

# print(factorial(5))

#--------------------------------------------------------------------------------------------------------------------------

# def sum(a):
#     if a==1:
#         return 1
#     return a+sum(a-1)
# print(sum(5))

#--------------------------------------------------------------------------------------------------------------------------

# def sum(a,b):
#     return a**b
# print(sum(5,3))


# def sum(a,b):
#     if b==1:
#      return a
#     return a*sum(a,b-1) 
# print(sum(2,4))

#--------------------------------------------------------------------------------------------------------------------------

# def daraja(a):
#     if a==0:
#         return 1
#     return 2*daraja(a-1)
# print(daraja(3))

#--------------------------------------------------------------------------------------------------------------------------

# summ=lambda a,b:a+b
# print(summ(4,5))

#--------------------------------------------------------------------------------------------------------------------------

# summ = lambda a:a.title()
# print(summ('Hello'))

#--------------------------------------------------------------------------------------------------------------------------

# my_list=[1,2,3,4,5,6]

# func=lambda a:a**2

# int_list=map(func,my_list)

# print(list(my_list))

#--------------------------------------------------------------------------------------------------------------------------

# def outer(a):
#     def inner(b):
#         nonlocal a
#         return a+b
#     return inner

# func=outer(5)
# print(func(8))

#--------------------------------------------------------------------------------------------------------------------------

# def outer(a):
#     def inner(b):
#         nonlocal a
#         return b**a
#     return inner

# sque=outer(2)
# cube=outer(3)
# pow4=outer(4)
# print(sque(6))
# print(cube(4))
# print(pow4(2))

#--------------------------------------------------------------------------------------------------------------------------

# def fakh(n):
#     def inner(x):
#         nonlocal n
#         return n*x
#     return inner
# double=fakh(2)
# print(double(5))

# triple=fakh(3)
# print(triple(4))

#--------------------------------------------------------------------------------------------------------------------------

# def remember_last():
#     n=None
#     def inner(a):
#         nonlocal n
#         res=n
#         n=a
#         return res
#     return inner
# func=remember_last()
# print(func(10))
# print(func(20))
# print(func(30))
# print(func(50))
# print(func(5))

#--------------------------------------------------------------------------------------------------------------------------

# def last(ss):
#     def inner(a):
#         nonlocal ss
#         ss+=a
#         return ss
#     return inner
# func=last(5)
# print(func(10))
# print(func(20))

#--------------------------------------------------------------------------------------------------------------------------

# def mona(n,m):
#     def inner(a):
#         return a>=n and a<=m
#     return inner   
# func=mona(10,20)
# print(func(15))
# print(func(25))

#--------------------------------------------------------------------------------------------------------------------------

# def limit(n):
#     def inner():
#         nonlocal n
#         res=n
#         n=n-1
#         if n>0:
#             return 'Vizov Razreshen'
#         return "Litit error"
#     return inner
# limit1=limit(2)
# print(limit1())
# print(limit1())
# print(limit1())

#--------------------------------------------------------------------------------------------------------------------------

# def sum(num1,num2):
#     print(num1+num2)
# def sub(num1,num2):
#     print(num1-num2)
# def mult(num1,num2):
#     print(num1*num2)
# def div(num1,num2):
#     print(num1/num2)
# def pow(num1,num2):
#     print(num1**num2)

# while True:
#     num1=int(input())
#     sign=input()
#     num2=int(input())

#     match sign:
#         case "+": sum(num1,num2)
#         case "-": sub(num1,num2)
#         case "*": mult(num1,num2)
#         case "/": div(num1,num2)
#         case "^": pow(num1,num2)
#         case "_":
#              print("Invalid sign")
#              continue

#--------------------------------------------------------------------------------------------------------------------------

# a=int(input())
# if  a>2 and a%2==0:
#     print("YES")
# else:
#     print("NO")

#--------------------------------------------------------------------------------------------------------------------------

# a=input()
# if len(a)>4:
#     print(a[0]+str(len(a)-2)+a[-1])
# else:
#     print(a)

#--------------------------------------------------------------------------------------------------------------------------

# n=int(input())
# cnt=0
# while a>0:
   
#     a=map(int,input().split())
#     if a[0]==1 and a[1]==1 or a[0]==1 and a[2]==1 or a[1]==1 and a[2]==1:
#         cnt+=1
#     n-=1
# print(cnt)

#--------------------------------------------------------------------------------------------------------------------------

# n=int(input())
# x=0
# while n>0:
#     a=input()
#     if '++' in a:
#         x+=1
#     elif '--' in a:
#         x-=1
#     n-=1
# print(x)

#--------------------------------------------------------------------------------------------------------------------------

# def my_decarator(func):
#     def inner():
#         print('Before func')
#         func()
#         print('After func')
#     return inner

# @my_decarator
# def say_hello():
#     print('Hello world')

# say_hello()

#--------------------------------------------------------------------------------------------------------------------------

# def my_decarator(func):
#     n=1
#     def inner():
#         nonlocal n
#         print(n)
#         func()
#         n+=1
#     return inner

# @my_decarator    decortor yane dopolnyat kekht
# def say_hello():
#     print('Hello world')

# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()

#--------------------------------------------------------------------------------------------------------------------------

# def my_print(*args):
#     for i in args:
#         print(i,end=' ')
# my_print(1,2,3,4,5,6)

#--------------------------------------------------------------------------------------------------------------------------

# def my_sum(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print (my_sum(1,20))

#--------------------------------------------------------------------------------------------------------------------------

# def my_sum(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# my_sum(name="Ali",Age=23)

#--------------------------------------------------------------------------------------------------------------------------

# def func(*args,**kwargs):
#     for i in args:
#         print(i,end=' ')
#     print()
#     for k,v in kwargs.items():
#         print(k,v)
# func(1,3,6,'hello',name='Ali',surname='Vali')

#--------------------------------------------------------------------------------------------------------------------------

# id=1
# lst=[]
# def creat(name,surname,age,course,city):
#     global id
#     dct={
#         'id':id,
#         'name':name,
#         'surname':surname,
#         'age':age,
#         "course":course,
#         'city':city
#     }
#     id+=1
#     lst.append(dct)
#     print("New student added successfully")

# def get_all():
#         for i in lst:
#             print(f'''
# id        ---> {i['id']}
# name      ---> {i['name']}
# surname   ---> {i['surname']}
# age       ---> {i['age']}
# course    ---> {i['course']}

# -----------------------------------
# ''')
# def get_by_id():
#      id=int(input('Enter student id ---> '))
#      for i in lst:
#         if i['id']==id:
#             print(f'''
# id        ---> {i['id']}
# name      ---> {i['name']}
# surname   ---> {i['surname']}
# age       ---> {i['age']}
# course    ---> {i['course']}

# -----------------------------------
# ''')

# def update_student():
#     update_id = int(input('Enter student ID to update --> '))
#     for student in lst:
#         if student['id'] == update_id:
#             student['name'] = input('Enter new name --> ')
#             student['surname'] = input('Enter new surname --> ')
#             student['age'] = input('Enter new age --> ')
#             student['course'] = input('Enter new course --> ')
#             student['city'] = input('Enter new city --> ')
#             print('Student updated successfully')
#             return
#     print('Student not found')
        
# def delete_student():
#     id=int(input('Enter student id for delete --> '))
#     for i in lst:
#         if i['id']==id:
#             lst.remove(i)
#             print(f'Student with id {id} deleted successfully')
#             return
#     print(f'Student with id {id} not found')


# while True:
#     n=int(input('''
# 1 ----> add new student
# 2 ----> get list of all students
# 3 ----> get student by id
# 4 ----> update students info by id
# 5 ----> delete student's info by id
# 6 ----> exit
#     chose your option -->'''))
#     if n==1:
#         creat(input('Enter name of student--> '),
#               input('Enter surname of student '),
#               input('Enter age of student '),
#               input('Enter course of student--> '),
#               input('Enter adress of student--> '))
#     if n==2:
#         get_all()
#     if n==3:
#         get_by_id()
#     if n==4:
#         update_student()
#     if n==5:
#         delete_student()
#     if n==6:
#         break

#--------------------------------------------------------------------------------------------------------------------------

