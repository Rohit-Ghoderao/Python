#Add Two Numbers in Python Using Function
num1 =int(input("Enter the value of num1:"))
num2 =int(input("Enter the value of num2:"))

def sum(num1,num2):
    return num1+num2

add=sum(num1,num2)
print(f'addition of {num1} and {num2} is {add}')