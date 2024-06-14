from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()
class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    location = Column(String)

    def __init__(self,id, vin, make, model,year,location):
        self.id = id
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.location = location
    def __repr__(self):
        return (self.vin, self.make, self.model, self.year, self.location)



class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, index=True, )
    name = Column(String)
    license = Column(String)
    # vehicle_id =Column (Integer, ForeignKey('vehicle.id'))

    def __init__(self, id, name, license):
        self.id = id
        self.name = name
        self.license = license

    def __repr__(self):
        return (self.name, self.license)

# class Maintenance(Base):
#     __tablename__ = 'maintenances'
#     id = Column(Integer, primary_key=True)
#     vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
#     maintance_type = Column(String)
#     maintance_date = Column(String)

#     def __init__(self, id, vehicle_id, maintance_type, maintainance_date):
#         self.id = id
#         self.vehicle_id = vehicle_id
#         self.maintance_type = maintance_type
#         self.maintance_date = maintainance_date
    
#     def __repr__(self):
#         return (self.id, self.vehicle_id, self.maintance_type, self.maintance_date)
    
        

# class Trip(Base):
#     __tablename__ = 'trips'
#     id = Column(Integer, primary_key=True)
#     vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
#     driver_id = Column(Integer, ForeignKey("driver.id"))
#     trip_start = Column(String)
#     trip_end = Column(String)
#     distance = Column(Float)


