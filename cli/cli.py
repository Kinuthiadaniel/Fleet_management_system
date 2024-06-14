from models.vehicle import Vehicle
from models.driver import Driver
from models.mainatence import Mainatence
from models.trips import Trip

def exit_program():
    print("Goodbye!")
    exit()

def create_vehicle():
    vin = input("Enter VIN: ")
    make = input("Enter vehicle Make: ")
    model = input("Enter vehicle Model: ")
    year = int(input("Enter Vehicle Year: "))
    location = input("Enter current vehicle Location: ")
    try:
        vehicle = Vehicle.create(vin=vin, make=make, model=model, year=year, location=location)
        print(f"Vehicle {vehicle} created")
    except Exception as e:
        print(f"Error creating vehicle: ", e)

def list_vehicles():
    vehicles = Vehicle.get_all()
    for vehicle in vehicles:
        print(vehicle)

def find_vehicle_by_id():
    id = int(input("Enter vehicle ID: "))
    try:
        vehicle = Vehicle.find_by_id(id)
        print(vehicle)
    except Exception as e:
        print(f"Error finding vehicle: ", e)

def update_vehicle():
    id = int(input("Enter vehicle ID: "))
    vin = input("Enter VIN: ")
    make = input("Enter vehicle Make: ")
    model = input("Enter vehicle Model: ")
    year = int(input("Enter Vehicle Year: "))
    location = input("Enter current vehicle Location: ")
    vehicle = Vehicle.find_by_id(id)
    vehicle.vin = vin
    vehicle.make = make
    vehicle.model = model
    vehicle.year = year
    vehicle.location = location
    vehicle.update()
    print(f"Vehicle {vehicle} updated")
def delete_vehicles():
    id = int(input("Enter vehicle ID: "))
    vehicle = Vehicle.find_by_id(id)
    vehicle.delete()
    print(f"Vehicle {vehicle} deleted")


def create_driver():
    first_name = input("Enter Driver First Name: ")
    last_name = input("Enter Driver Last Name: ")
    license = input("Enter Driver License: ")
    try:
        driver = Driver.create(first_name=first_name, last_name=last_name, license=license)
        print(f"Driver {driver} created")
    except Exception as e:
        print(f"Error creating driver: ", e)

def list_drivers():
    drivers = Driver.get_all()
    for driver in drivers:
        print(driver)

def find_driver_by_id():
    driver_id = int(input("Enter driver ID: "))
    driver = Driver.find_by_id(driver_id)
    print(driver)

def delete_driver():
    id = int(input("Enter driver ID: "))
    driver = Driver.find_by_id(id)
    driver.delete()
    print(f"Driver {driver} deleted")


def update_driver():
    id = int(input("Enter driver ID: "))
    first_name = input("Enter Driver First Name: ")
    last_name = input("Enter Driver Last Name: ")
    license = input("Enter Driver License: ")
    driver = Driver.find_by_id(id)
    driver.first_name = first_name
    driver.last_name = last_name
    driver.license = license
    driver.update()
    print(f"Driver {driver} updated")

def create_mainatence_record():
    vehicle_id = int(input("Enter vehicle ID: "))
    mainatence_type = input("Enter mainatence_type: ")
    mainatence_date = input("Enter mainatence_date: ")
    try:
        record = Mainatence.create(vehicle_id=vehicle_id, mainatence_type=mainatence_type, mainatence_date=mainatence_date)
        print(f"Record {record} created")
    except Exception as e:
        print(f"Error creating record: ", e)

def list_mainatence_records():
    records = Mainatence.get_all()
    for record in records:
        print(record)

def find_mainatence_record_by_id():
    vehicle_id = int(input("Enter vehicle id: "))
    record = Mainatence.find_by_id(vehicle_id)
    print(record)

def update_mainatence_record():
    id = int(input("Enter record ID: "))
    vehicle_id = int(input("Enter vehicle ID: "))
    mainatence_type = input("Enter mainatence_type: ")
    mainatence_date = input("Enter mainatence_date: ")
    record = Mainatence.find_by_id(id)
    record.vehicle_id = vehicle_id
    record.mainatence_type = mainatence_type
    record.mainatence_date = mainatence_date
    record.update()
    print(f"Record {record} updated")

def delete_mainatence_record():
    id = int(input("Enter record ID: "))
    record = Mainatence.find_by_id(id)
    record.delete()
    print(f"Record {record} deleted")


def create_trip():
    vehicle_id = int(input("Enter vehicle ID: "))
    driver_id = int(input("Enter driver ID: "))
    start_time = input("Enter start time: ")
    end_time = input("Enter end time: ")
    distance = int(input("Enter distance: "))
    try:
        trip = Trip.create(vehicle_id=vehicle_id, driver_id=driver_id, start_time=start_time, end_time=end_time, distance=distance)
        print(f"Trip {trip} created")
    except Exception as e:
        print(f"Error creating trip: ", e)

def list_trips():
    trips = Trip.get_all()
    for trip in trips:
        print(trip)

def find_trip_by_id():
    id = int(input("Enter trip ID: "))
    trip = Trip.find_by_id(id)
    print(trip)

def update_trip():
    id = int(input("Enter trip ID: "))
    vehicle_id = int(input("Enter vehicle ID: "))
    driver_id = int(input("Enter driver ID: "))
    start_time = int(input("Enter start time: "))
    end_time = int(input("Enter end time: "))
    distance = int(input("Enter distance: "))
    trip = Trip.find_by_id(id)
    trip.vehicle_id = vehicle_id
    trip.driver_id = driver_id
    trip.start_time = start_time
    trip.end_time = end_time
    trip.distance = distance
    trip.update()
    print(f"Trip {trip} updated")

def delete_trip():
    id = int(input("Enter trip ID: "))
    trip = Trip.find_by_id(id)
    trip.delete()
    print(f"Trip {trip} deleted")

def trips_by_driver():
    driver_id = int(input("Enter driver ID: "))
    driver = Driver.find_by_id(driver_id)
    trips = driver.trips_by_driver()
    for trip in trips:
        print(trip)



    