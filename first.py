# print ("heloo world")



# if False:
#     print('man avlin hastam dar in khat ')
#     print('man dovomi hastam dar in line ') اینها اگه پشت سر هم بدون فاصله باشند ترو درست مییکنه 

# print('man false ahstam ') دومی فالس میشه با یک فاصله خودش درست میکنه فالس 



# a=  input('thas is your first name:   ')
# print(a,'salam ')



# a=  int(input('pelease enter your age '))
# b= int(input('pelease enter your age '))
# c= a+b
# print(c)
# print(type(c))



# age= int(input("pelease enter your age "));
# day= ' days your life ';
# sen =age *365 ;
# print( str (sen)+ str(day));
# hour= ' hours is your moment';
# h=sen*24;
# print( str(h)+hour);
# min=' minutes is your life ';
# m=h*60;
# print (str(m)+min );
# sec= ' second is down your life ';
# s=m*60;
# print (str(s)+sec );



# number = int(input(" enter a nbumber : "))
# if number % 2 == 0:
#     print("zoj ")
# else:
#     print("fard ")



# adad = int(input(' number enter kon '))
# if 20>=adad>=17:
#     print('momtaz shodi ')
# elif 16>=adad>=10:
#     print('bad nabodi ')
# else :
#     print('ridi')



# for i in range(1, 11):
#     print(i)



# a=str(input(''))
# print(len(a))



# people =(('ata',18),('momsom',55),('amo esa ',56),('memraj',30))
# for name , son in people :
#  print(f"{name} is {son} years old ") 
# «در این بخش، people یک تاگل (Tuple) است. حلقه for مقادیر name و son را از داخل people دریافت می‌کند. سپس این مقادیر را پردازش کرده و در نهایت نتیجه را دوباره در people قرار می‌دهد. بعد از آن با استفاده از print خروجی را نمایش می‌دهیم.»



# a=0
# while a<=100:
#     print(f"a is {a}")
#     a+=2



# for i in range(10):
#     print (i , "\n")



# for a in range(1,20,2,):
#     print(f"{a} adad")



# l = ("ata hoseinnezhad")
# for i in range (len(l)):
#     print(i,l[i])



# esm =('ata ', 'mata','shata')
# fam=('mir', 'sir', ' tir ')
# sen=(12,55,45)
# for x in zip(esm, fam , sen):
#     print(x)



# from random  import randint
# print(randint(1,6))
# from random  import randint
# print(randint(1,6))



# def hello (name ):
#     for i in range(3):  
#         print(f" oh salam {name}")
# hello('ata')
# hello('ata')
# hello('ata')    



# def say_hello_n_time( name, n ,a):
#     for i in range(a):
#         return(a)

# say_hello_n_time("ata ",9,5)
# say_hello_n_time("jafar1",54,8)



tasks =[]
def display_menu():
    print("\n1.add task")
    print("2. edit task ")
    print( "3.delete task ")
    print("4.show task ")
    print( "5.exit")

while True:
    display_menu()
    choice = input("select your option :  ")
    if choice== "1":
        task =  input("enter task :")
        tasks.append(task)
        print("Task added successfully")
    elif choice == '2':
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[task_index] = new_task
                    print("Task edited successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to edit.")
    elif choice == '3':
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            try:
                task_index = int(input("Enter task index to delete: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks.pop(task_index)
                    print("Task deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to delete.")
    elif choice == "4":
        if tasks:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
        else:
            print("No tasks available.")
    elif choice =="5":
        print("taks is close ")        
        break
    else:
        print("your taks is not defined ") 




        



