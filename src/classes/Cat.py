# 1. define a class Cat
# 2. define a constructor for each Cat object
    # 2.5. define Cat attributes as name, color, age
# 3. define properties for all Cat attributes
    # 3.5. how would you define these with the property function?
    # 3.5. how would you define these with decorators?
# 4. define methods for each Cat object
    # 4.5. define Cat methods as meow(), have_a_birthday()
# [OPTIONAL] 5. define overriding str magic method

class Cat():

    #contructor
    def __init__(self, name, color, age):
        self._name = name
        self._color = color
        self._age = age

    #make name property with property function
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    name = property(get_name, set_name)

    # make color property with decorators 
    @property 
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    @property 
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    def meow(self):
        print("mewwooow")

    def have_a_birthday(self):
        print("Happy B-Day!")
        self.age = self.age + 1
        print(f"You are {self.age}!")

    #str magic method
    def __str__(self):
        return f"name : {self.name}\ncolor: {self.color}\nage: {self.age}"

# objects (instances of a class)
spice = Cat("spice", "orange", 2)
cinnamon = Cat("cinnamon", "brown", 4)
rufus = Cat("rufus", "black", 2)

rufus.meow()
spice.have_a_birthday()
print(rufus)
# spice.name = "Sugar"
# print(spice.name)
# cinnamon.color = "white"
# print(cinnamon.color)
