class my_class:
    def __init__(self,name,age) -> None: 
        self.names = name
        self.ages = age

    def my_method(self):
        print("Hello " + self.names + " your age is " + str(self.ages))

c1 = my_class("surya", 26)
c1.my_method()
#instead of self we can use any different variable like below 
class my_class:
    def __init__(any, name, age) -> None:
        any.names = name
        any.ages = age 

    def my_method(any):
        print("Hello" + any.names + " your age is " + str(any.ages))
    
d1 = my_class("nantha", 28)
d1.my_method()
        


