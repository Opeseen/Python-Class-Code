# from Classes import car
# from Classes import electric_car

# motor = car("Honda",'CSV', 2020)
# print(motor.car_description())
# motor.meter()
# motor.meter_reading = 1
# motor.meter()

# telsa = electric_car('bmw','x2',2021)
# telsa.get_battery()

# telsa.battery_two.describe_battery_size()
# telsa.battery_two.battery_size = 45
# telsa.battery_two.describe_battery_size()
path = r'C:\Users\Horpeyemi\Documents\Doc\TXT\SQL_chart.txt'
with open(path) as file:
    for line in file:
        print(line.upper())
    # content = file.read()
    # print(content)
    # print(content.rsplit)
