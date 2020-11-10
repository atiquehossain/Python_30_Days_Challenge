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




