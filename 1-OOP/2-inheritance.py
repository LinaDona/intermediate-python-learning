from oop import Person # import the parent class

# This is the child class
class Worker(Person):

    def __init__(self, name, age, height, salary):
        # altr: super(Worker, Person.__init__(self, name, age, height))
        super(Worker, self).__init__(name, age, height) # super() will call the parent class's ctr
        self.salary = salary

    # overriding the inherited method
    def __str__(self):
        text = super(Worker, self).__str__() # call parent implementation
        text += ", Salary: {}".format(self.salary)
        return text

    def calc_yearly_salary(self):
        return self.salary * 12

worker = Worker("Tom", 30, 180, 30000)
print(worker)
print("Yearly salary of worker {} is {}".format(worker.name, worker.calc_yearly_salary()))
