#Opp,object,class,constructor,method,inheritance,Encapsulation,Palymorphism


######Object###########

class human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age = age
        self.gender=gender


    def char(self):
        print("My name is ",self.name," Age is ",self.age," and i am ",self.gender)





ob=human('Atique',26,'Male')
ob.char()




class Car:
    wheels =5
    #class variable

    def __init__(self):
        #instance variable
        self.com='Audi'
        self.model='A5'


c=Car()
print(id(c))
c0=Car()
print(id(c0))

print(c.com,c.model,c.wheels)

