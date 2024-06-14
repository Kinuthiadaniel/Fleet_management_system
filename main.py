from models.vehicle import Vehicle
from models.driver import Driver
from models.mainatence import Mainatence
from models.trips import Trip
from cli.cli import (
    exit_program,
    create_vehicle,
    list_vehicles,
    find_vehicle_by_id,
    delete_vehicles,
    update_vehicle,
    create_driver,
    list_drivers,
    find_driver_by_id,
    update_driver,
    delete_driver,
    create_mainatence_record,
    list_mainatence_records,
    find_mainatence_record_by_id,
    update_mainatence_record,
    delete_mainatence_record,
    create_trip,
    list_trips,
    find_trip_by_id,
    update_trip,
    delete_trip,
    trips_by_driver


)



def main():
    while True:
        print("Welcome to the Vehicle Manager")
        print("Please select an option")
        # Driver.drop_table()
        Driver.create_table()
        # Vehicle.create_table()
        # Mainatence.drop_table()
        Mainatence.create_table()
        # Trip.drop_table()
        Trip.create_table()



        menu()
        command = input("> ")
        if command == "0":
            exit_program()
        elif command == "1":
            create_vehicle()
        elif command == "2":
            list_vehicles()
        elif command == "3":
            find_vehicle_by_id()
        elif command == "4":
            update_vehicle()
        elif command == "5":
            delete_vehicles()
        elif command == "6":
            create_driver()
        elif command == "7":
            list_drivers()
        elif command == "8":
            find_driver_by_id()
        elif command == "9":
            update_driver()
        elif command == "10":
            delete_driver()
        elif command == "11":
            create_mainatence_record()
        elif command == "12":
            list_mainatence_records()
        elif command == "13":
            find_mainatence_record_by_id()
        elif command == "14":
            update_mainatence_record()
        elif command == "15":
            delete_mainatence_record()
        elif command == "16":
            create_trip()
        elif command == "17":
            list_trips()
        elif command == "18":
            find_trip_by_id()
        elif command == "19":
            update_trip()
        elif command == "20":
            delete_trip()
        elif command == "21":
            trips_by_driver()

        else:

            print("Invalid command")
    
def menu():
    print("0. Exit program")
    print("1. Create vehicle")
    print("2. List all vehicles")
    print ("3. Find vehicle by id")
    print("4. Update vehicle by id")
    print("5. Delete vehicle by id")
    print("6. Create driver")
    print("7. List all drivers")
    print("8. Find driver by id")
    print("9. Update driver by id")
    print("10. Delete driver by id")
    print ("11. Create Mainatence Record")
    print("12. List all Mainatence Records")
    print("13. Find Mainatence Record by id")
    print("14. Update Mainatence Record by id")
    print("15. Delete Mainatence Record by id")
    print("16. Create Trip")
    print("17. List all Trips")
    print("18. Find Trip by id")
    print("19. Update Trip by id")
    print("20. Delete Trip by id")
    print("21. Trips by Driver")

if __name__ == "__main__":
    main()