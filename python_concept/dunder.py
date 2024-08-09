class Person:
    #init is a fnx varable which will execute itsdelf when we use the class for the first time
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __del__(self): # these fnx will delete the object at the end of file
        print("deleted :)")
        pass;
p =Person("Mike",25);
print(f"{p.name}")
print("lets do")
#del p#will delete the p from class
#del p.name# wil delete the name of p from class

