#math module import
import math


print("Python 10 day challenge ")
x="Let's start"
print(x)
#Variable
intvar=2
floatvar=2.28
stringvar="Atique Hossain"
#VAriable print
print("Integer is",intvar,"float is ",floatvar,"String is",stringvar)
a,b,c=1,2,"Hello"
print("Multiple assignment",type(a),type(b),type(c))
#python String
print(stringvar[6:14])

#math function
print(math.acos(0.5))
print(math.sqrt(b))
print(math.isqrt(1000))
# Return value of x * (2**i)
print(math.ldexp(9, 3))
print(math.log(10,2))
print(math.pow(2,3))
print(math.remainder(9,2))
# Print the value of Euler e
print (math.e)
# Print the positive infinity
print (math.inf)

# Print the negative infinity
print (-math.inf)
####input####
print("Input a number")
xx=float(input())
print("Number is",xx)
print("Input second number")
xxx=float(input())
print("Number is",xxx)
if xx>xxx:
    print("1st number is grater")
elif xx==xxx:
    print("Numbers are equal")
else:
    print("second number is greater the 1st number")
print("1st number is grater") if xx>xxx else print("Numbers are equal") if xx==xxx else print("second number is greater the 1st number")

