#list file
list=['Name','subject','CSE'];
print(list)
print("list1,2" ,list[1:])
print("For loop :")
for x in list:
    print(x)
if 'CSE' in list:
    print("Ys CSE in the list")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for xx in range(1,10):
    print(xx)

for xxx in range(2, 30, 3):
  print(xxx)

list1=['red','big','tasty']
list2=['apple','banana','cherry']
for x1 in list1:
    for y1 in list2:
        print(x1,y1)

def myfun(fname,lname):
    print(fname,"",lname)
myfun("Atique","Hossain")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_fun(x11):
  return 5 * x11

print(my_fun(3))
print(my_fun(5))
print(my_fun(9))

def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement


def my_func(n):
    return  lambda a:a*n

myd= my_func(2)
print(myd(11))