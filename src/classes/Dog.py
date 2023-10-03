class Pup():
    def __init__(self, name, wags_tail, is_good_boy = True):
        #will be properties
        self._name = name
        self._wags_tail = wags_tail
        #attribute
        self.is_good_boy = is_good_boy
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 3:
            self._name = name
        else: 
            raise Exception ("Name must be a string with more than 3 characters!")
    @property 
    def wags_tail(self):
        return self._wags_tail
    @wags_tail.setter
    def wags_tail(self, wags_tail):
        if wags_tail == True or wags_tail == False:
            self._wags_tail = wags_tail
        else:
            raise Exception("tail wagging must be a boolean!")
        
    def summon_pup(self):
        print(f"come here, {self.name}")
    
    def __str__(self):
        return f"name: {self.name}\nis good boy: {self.is_good_boy}\nwags tail: {self.wags_tail}"

herschel = Pup("name", True)
prenup = Pup("prenup", True, False)
springfrost = Pup("spring frost", False)

# springfrost.wags_tail = True
# print(springfrost.wags_tail)
# prenup.name = "gummy"
print(prenup)
springfrost.summon_pup()