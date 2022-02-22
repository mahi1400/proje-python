
#-----------------------------------------
#محاسبه ی مساحت متوازی الاضلاع
base = float(input("length of base: "))
height = float(input('measurement of height: '))
area = base * height
print("Area is:", area)
#-----------------------------------------
#برنامه ای که سه عدد را از ورودی گرفته و به ترتیب صعودی چاپ نماید
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
if a > b:
 temp = a
 a = b
 b = temp
if a > c:
 temp = a
 a = c
 c = temp
if a > c:
 temp = a
 a = c
 c = temp
if b > c:
 temp = b
 b = c
 c = temp
print("Sorted is ", a, b, c)
#----------------------------------
#بازی سنگ کاغذ قیچی

    
import random
    i = random.randint(0,2) #entekhab kamputer
    choises=["sang","kagaz","geychi"]
    print("1-sang \n 2-kagaz \n 3-geychi")
    inp =int(input("Enter a number : "))
    inp =inp-1
    print("-------------------")
    print("camputer choise : (0)".format(choises[i]))
    if inp == 0 and i == 2 or inp == 1 and i == 0 or inp == 2 and i == 1 : #WIN
        print("WIN")
    elif inp == 0 and i == 1 or inp == 1 and i == 2 or inp ==2 and i == 0: #LOSE
        print("LOSE")
    elif inp == i :
        print("SAME")
#----------------------



        


