##n=1
##sum=0
##while n <=100:
##    if n%7!=0:
##        sum=sum+n
##        n=n+1
##print("the sum of the series=",sum)
##n=1
##sum=0
##while n<=100:
##   if n%7!="0":
##    sum=sum+n
##    n=n+1
##print("the sum of the series=",sum) 
##n=2
##sum=0
##while n<=100:
##    if n%8!="0":
##        sum=sum+n
##        n=n+1
##print("the number of the series=",sum)
##num1=int(input("num1:"))
##num2=int(input("num2:"))
##num3=int(input("num3:"))
##if(num1>num2 and num1>num3):
##    print(num1,"is greater than others.")
##elif(num2>num1 and num2>num3):
##    print(num2,"is greater than others.")
##else:
##    print(num3,"is greater than others.")
##               
import math
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if (a+b)>c and(b+c)>a and(c+a)>b:
    s=(a+b+c)/2
    area=math.sqrt (s*(s-a)*(s-b)*(s-c))
    print("the triangle is:",area)
else:
        print("triangle is not possible.")
                    
