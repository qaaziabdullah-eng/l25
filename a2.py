class vehicle:
    def __init__(self,name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

BMW=vehicle("BMW",200,100)
print("vehicle name:",BMW.name)
print("vehicle max speed:",BMW.max_speed)
print("vehicle mileage:",BMW.mileage)
print("\n")
audi=vehicle("audi",120,150)
print("vehicle name:",audi.name)
print("vehicle max speed:",audi.max_speed)
print("vehicle mileage:",audi.mileage)
