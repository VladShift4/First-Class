import exercise


#Create a Class:
class Dog():
    def __init__(self, name, year):
        self.name = name
        self.year = year

    #Accessor methods
    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_info(self):
        return f"Name: {self.name}, year: {self.year}"

    #Muthator method:
    def new_info(self, set_name, set_year):
        self.name = set_name
        self.year = set_year

    #Operator Overloading
    def __add__(self, otherDog):
        return Dog("Puppy of:" + self.name + " and "  + otherDog.name,
                   self.year + 1)

def main():
    boyDog = Dog("Fufy", 2023)
    girlDog = Dog("Flufy", 2023)
    print(girlDog.get_name())
    print(boyDog.get_name())
    print(girlDog.get_year())
    print(boyDog.get_year())

    puppy = boyDog + girlDog
    print(puppy.get_name())
    print(puppy.get_year())

if main == "__main__":
    main()

# "Create" puppy
main()