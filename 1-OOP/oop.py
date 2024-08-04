class Person:
    nbr_of_ppl = 0 # this is a CLASS VARIABLE. It is the same across all instances of this class.

    def __init__(self, name, age, height):
        self.name = name # creating an attribute name
        self.age = age
        self.height = height
        Person.nbr_of_ppl += 1
    
    ''' 
    what is the string "equivalent" of your object? 
    aka: what should be the string when your object is casted into a string 
    '''
    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def __del__(self): # what happens when your object is deleted?
        print("Object with name {} is deleted!".format(self.name))
        Person.nbr_of_ppl -= 1

    def imJustAMethod(self):
        local_var = 0 # this var is local to this method, it can't be accessed by other methods
        self.name = "I'm Just a Girl"
        
    
    def getOlder(self, years):
        self.age += years

# only run the following code if it runs at TOP LEVEL (when this file is not an imported module)
if __name__ == "__main__":
    person = Person("Reina", 22, 166)
    person2 = Person("someone", 0, 0)
    print() # print empty line
    print(person)
    print() # print empty line
    print("Number of people is: {}".format(Person.nbr_of_ppl))
    person.getOlder(3)
    print() # print empty line
    print(person)
    print() # print empty line
    del person2
    print() # print empty line
    print("Number of people is: {}".format(Person.nbr_of_ppl))
    print() # print empty line
