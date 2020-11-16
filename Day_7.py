####linear search
pos =-1
def search(list,n):
    i=0

    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True;
        i=i+1
    return False

list =[5,8,4,6,9,2]
n=9

if(search(list,n)):
    print("Found",pos)
else:
    print("Not found",pos)

#####Binary Search
posb=-1

def listbinary(binarylistk,k):
    l=0
    u=len(binarylistk)-1

    while l<u:
        mid=(l+u)//2

        if binarylistk[mid]==k:
            globals()['posb']=mid
            print("found",posb+1)
            break
        else:
            if list[mid]<k:
                l=mid;
            else:
                u=mid;




bl=[1,2,34,56,78,658,56886,685682,85686522,11111111111111]

k=2
listbinary(bl,k)


############Recursion




def fact(n):
    if(n==0):
        return 1
    return fact(n-1)

result=fact(6)
print(result)






