##### Factorial problem######

#input user,use for loop
#5!= 5*4*3*2*1
#n!=n*(n-1)
#n*(n-1)
print("Enter an integer number:")
box=int(input())
print("Number is ",box)
sum=1

if box<0:
    print("ERROR VALUE")
else:
    for i in range(1,box+1):
        sum=sum*i;
print(sum)

###Factoral recursion ############
def factorial(n):
    # single line to find factorial
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1)




print("Factorial of", box, "is",factorial(box))



###Palindrome ############

print("Palindrome\n input a string")
xx=input()
tx=xx[::-1]

if xx==tx:
    print("Input is palindrome")
else:
    print("Input is not palindrome")

###leaper ############

