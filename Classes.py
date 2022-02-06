print(1+2)
def Function():
    a = 5*3
    b = 3 + 4
    return a + b

print(Function())

def Function():
    a = 5*3
    b = 3 + 4
    print(a + b)
Function()

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self,nick):
        self.nick = 'mario'
        print(self.nick.title() + " Is Now Sitting")
    
    def roll_over(self):
        print(self.name.title() + " Roll Over")
    
my_dog = Dog('wille',9)
print(my_dog.name.title())
print(str(my_dog.name.upper())+ " Is Now", my_dog.age, 'Years Old')
print(my_dog.sit('man'))
print(my_dog.name + " Is coming")

my_dog.roll_over()

# my_dog.sit()

# your_dog = Dog('lucky',10)
# print(your_dog.sit())

class car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.meter_reading = 0
    
    def car_description(self):
        answer = self.make.upper() +" " + self.model + " " + str(self.year)
        return answer
    
    def meter(self):
        print("the car speadometer is".upper(),self.meter_reading)

    def update_meter(self,newMeter):
        self.meter_reading = newMeter
    
    def AdditionalUpdate(self,addition):
        self.addition = addition
        if addition >= self.meter_reading:
            self.meter_reading = addition
            #print(self.addition)
        else:
            print("You can't roll back")
    
    def incrementalUpdate(self,increment):
        self.meter_reading += increment
            
result = car('Toyota','Camry',2016)
print(result.car_description())
result.meter_reading = 1
result.meter()
result.update_meter(2)
result.meter()
result.AdditionalUpdate(4)
result.meter()
result.incrementalUpdate(100)
result.meter()
result.incrementalUpdate(200)
result.meter()

class battery():
    def __init__(self):
        self.battery_size = 10
    
    def describe_battery_size(self):
        print("the car has ".upper() + str(self.battery_size) + " updated".upper())

    def GetRanged(self):
        if self.battery_size == 10:
            range = 100
            print("the new Get_Ranged is now".title(),range)
        else:
            range = 200
            print("the new GetRanged has now been updated to".upper(),range)
        
        # print(range)

class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 70
        self.battery_two = battery()
    
    def get_battery(self):
        print(self.make.upper() + " Has " + str(self.battery) + "Km Battery")

    def meter(self):
        # return super().meter()
        print("the car new meter is overridden".upper())

my_telsa = electric_car('telsa','A83','2019')
print(my_telsa.car_description())
my_telsa.get_battery()
# print(my_telsa.meter())
my_telsa.meter()

my_telsa.battery_two.describe_battery_size()

my_telsa.battery_two.GetRanged()

my_telsa.battery_two.battery_size = 20
my_telsa.battery_two.GetRanged()