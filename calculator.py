def sum(x,y):
    return x+y
def substract(x,y):
    return x+y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print("Select The Operation to be performed:-")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")  
print("4.Division") 

choice=int(input("Enter Number Corresponding To The Operation You Want To Perform:- "))            
x=int(input("Enter First Number:- "))
y=int(input("Enter Second Number:- "))
if choice == 1:
    print(x,"+",y,"=",sum(x,y))
elif choice == 2:
    print(x,"-",y,"=",substract(x,y))
elif choice == 3:
    print(x,"x",y,"=",multiply(x,y))
elif choice == 4:
    print(x,"/",y,"=",division(x,y))        
else :
    print("Wrong Choice")

