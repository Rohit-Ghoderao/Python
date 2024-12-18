VarA = 25 
VarB = 5

import operator
sum = operator.add(VarA,VarB)
sub = operator.sub(VarA,VarB)
mul = operator.mul(VarA,VarB)
div = operator.mod(VarA,VarB)

print(f"the sum of {VarA} and {VarB} is {sum}")
print(f"the sub of {VarA} and {VarB} is {sub}")
print(f"the mul of {VarA} and {VarB} is {mul}")
print(f"the div of {VarA} and {VarB} is {div}")