#Python Program to Find the Factorial of a Number
#n=n(n-1)

Userinput=int(input("Enter your Number: "))

Factorial=1

for i in range (1,Userinput+1):
    Factorial=Factorial*i
    
print(f'The factorial of {Userinput}is {Factorial}')    

