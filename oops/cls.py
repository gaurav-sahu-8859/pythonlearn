# # oop-object oriented programming
# classes and object,inheritance,polymorphysm,encapsulation,abstraction

class animal:
    # name="dog"
    # sound="bark"
    def __init__(self,name,sound):#constructor
        # print("i am constructor")
        self.name=name
        self.sound=sound
        
    def __str__(self):
        return f"name:{self.name},\nsound:{self.sound}"


class dog(animal):
    def __init__(self,name,sound,ispet):#constructor override
        animal.__init__(self,name,sound)
        self.ispet=ispet

    def __str__(self):
        return f"{super().__str__()},\nispet:{self.ispet}"
   

class cat(animal):
    def __init__(self, name, sound,isswim):
        super().__init__(name, sound)
        self.isswim=isswim

    def __str__(self):
        return f"{super().__str__()},\nisswim:{self.isswim}"
    
    

# a1=animal("dog","bark")
# a2=animal("cat","mews")
a1=dog("tomy","bark",True)
a2=cat("billi","mews",True)

# print(a1.name)
# print(a1.sound)

# print(a2.name)
# print(a2.sound)
print(a1)
print(a2)


# # task
# make class vehical
# make inherited class car, plain, boat
