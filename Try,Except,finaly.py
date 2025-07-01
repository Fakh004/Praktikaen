# a=0
# b=5
# try:
#     b/a
#     print('code has not error')
# except ZeroDivisionError:
#     print('we cold not devide by zero')
# except TypeError:
#     print('TypeError')
# else:
#     print("exept didnt work")
# finally:
#     print('it is finally')
    


# while True:
#     try:
#         a=int(input())
#         sym=input()
#         b=int(input())
#         if sym=='+':
#             print(f'{a} + {b} = {a+b}')
#         if sym=='-':
#             print(f'{a} - {b} = {a-b}')
#         if sym=='*':
#             print(f'{a} * {b} = {a*b}')
#         if sym=='//':
#             print(f'{a} // {b} = {a//b}')
#         if sym=='/':
#             print(f'{a} / {b} = {a/b}')
#         if sym=='%':
#             print(f'{a} % {b} = {a%b}')
#     except ZeroDivisionError:
#         print('Ba 0 taqsim karda nameshavad')
#     except TypeError:
#         print('TypeError')
#     except Exception as ex:
#         print(ex)

#-----------------------------------------------------------


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