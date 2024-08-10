class Person:
    #init is a fnx varable which will execute itsdelf when we use the class for the first time
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __del__(self): # these fnx will delete the object at the end of file
        print("deleted :)")
        pass;
    def __str__(self):# it will run when only self is called we can also use __repr__ as a alt
        return self.name;
p =Person("Mike",25);
print(f"{p.name}")
print("lets do")
print(p);
#del p#will delete the p from class
#del p.name# wil delete the name of p from class




class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):# we also have __sub__ __mul__ __div__
        return Vector(self.x+other.x,self.y+other.y)
    def __len__(self):
        # it will run when we find the len of self
        return 2
    def __call__(self):
        return 'these will be executed when we call the object '
v1=Vector(10,20)
v2=Vector(50,60)
v3=v1+v2; # if we use these then class does not knows that x is to be added with x and y with y 
print(v1)
print(v3.x);
print(v3.y);
print(len(v1))
print(v1())