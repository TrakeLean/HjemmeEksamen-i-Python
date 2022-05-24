import random
import string

NUMBER_OF_SPACES = 10
NUMBER_OF_ADD_AND_REMOVE_ITERATIONS = 50


class Car():
    def __init__(self):
        self.registration_number = self.make_registrationNumber()
        self.year = random.randint(1950,2022)
        
        
        
    def make_registrationNumber(self):
        registrationNumber=""
        registrationNumber+="".join(random.choice(string.ascii_uppercase) for _ in range(2))
        registrationNumber+="".join(random.choice(string.digits) for _ in range(5))
        return registrationNumber


class PassengerCar(Car):
    def __init__(self):
        super().__init__()
        self.type = "Passenger Car"
        self.weight = random.randint(1100,2400)
        self.seats = random.randint(2,7)

class Van(Car):
    def __init__(self):
        super().__init__()
        self.type = "Van"
        self.weight = random.randint(1500,3500)
        self.load = random.randint(700,1800)

class ElectricCar(PassengerCar):
    def __init__(self):
        super().__init__()
        self.type = "Electric Car"
        self.capacity = random.randint(69,420)
        self.registration_number = self.make_registrationNumber()
        
    def make_registrationNumber(self):
        registrationNumber="EL"
        registrationNumber+="".join(random.choice(string.digits) for _ in range(5))
        return registrationNumber
        
class FossilCar(PassengerCar):
    def __init__(self):
        super().__init__()
        self.type = "Fossil Car"
        self.capacity = random.randint(300,1000)
    
    
class Garage():
    def __init__(self):
        self.places = []
        self.free_spaces = self.available_places()
    
    
    
    def print_garage(self):
        for position,vehicle in enumerate(self.places):
            if vehicle==None:
                print(f"At Position: {position} vehicle: None")
            else:
                print(f"At Position: {position} vehicle: {vehicle.registration_number},{vehicle.type}")
             
    def available_places(self):
        free_spaces = []
        for position,vehicle in enumerate(self.places):
            if vehicle==None:
                free_spaces.append(position)
        #print(free_spaces)
        return free_spaces
    
    def is_space_available(self, position):
        if self.places[position]==None:
            return True
        else:
            return False
    
    def add_vehicle(self, vehicle): 
        if len(self.free_spaces)>0:
            self.places.insert(random.choice(self.free_spaces),vehicle)
            print(f"Vehicle: {vehicle.registration_number} has been placed in the garage")
            return True
        return False
    
    def remove_vehicle(self, reg_number):
        for vehicle in self.places:
            if vehicle!=None and vehicle.registration_number == reg_number:
                self.places.remove(vehicle)
                return True
        return False
    
    def locate_vehicle(self, reg_number):
        for position,vehicle in enumerate(self.places):
            print(position,vehicle)
            if vehicle!=None and vehicle.registration_number==reg_number:
                return position
        return -1
    




def make_vehicle():
    if (random.randint(1,4) < 4):
        if (random.random()>0.5):
            car = ElectricCar()
        else:
            car = FossilCar()
    else:
        car = Van()
    return car
          
            
if __name__ == "__main__":
    garage = Garage()
    for _ in range(NUMBER_OF_SPACES):
        if random.random() > 0.2:
            garage.places.append(make_vehicle())
        else:
            garage.places.append(None)
            pass
    print("--- PLACED CARS ---")
    garage.print_garage()
    garage.free_spaces = garage.available_places()
    
    
        #adds new and remove vehicles randomly
    for x in range(NUMBER_OF_ADD_AND_REMOVE_ITERATIONS):
        #print(f"--- ITERATION {x} ---")
        if random.random()>0.5:
            for position in range(NUMBER_OF_SPACES):
                if garage.is_space_available(position)==False:
                    vehicle=garage.places[position]
                    if garage.remove_vehicle(vehicle.registration_number):
                        print(f"Vehicle: {vehicle.registration_number} have been removed from the garage")
                    else:
                        print("This shouldnt happen, but vehicle are not removed...")
                    break
        else:
            if garage.add_vehicle(make_vehicle()):
                pass
            else:
                print("No spaces left...")
                
