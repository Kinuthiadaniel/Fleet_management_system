from .__init__ import CURSOR, CONN

class Vehicle:
    all = {}

    def __init__(self, id=None, vin = None, make=None, model = None, year= None, location=None):
        if id is not None:
            self.id = id
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.location = location
        # self.save()
       

    def __repr__(self):
        return f'<Vehicle {self.vin}>'

    # @property
    # def id(self):
    #     return self._id

    # @id.setter
    # def id(self, value):
    #     if isinstance(value, int):
    #         self._id = value
    #     else:
    #         raise TypeError("id must be of type int")

    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be of type str")
        if not (2 <= len(value) <= 256):
            raise ValueError("Title must be between 2 and 256 characters")
        self._vin = value

    @classmethod
    def create_table(cls):
        sql= """
            CREATE TABLE IF NOT EXISTS vehicles(
            id INTEGER PRIMARY KEY,
            vin VARCHAR,
            make TEXT,
            model TEXT,
            year INTEGER,
            location TEXT
            )
            """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS vehicles
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO vehicles (vin, make, model, year, location)
            VALUES (?, ?, ?, ?,?)
        """
        CURSOR.execute(sql, (self.vin, self.make, self.model, self.year, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        if hasattr(self, '_id'):
            sql = """
                UPDATE vehicles
                SET vin = ?, make = ?, model = ?, year = ?, location = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (self.vin, self.make, self.model, self.year,self.location, self.id))
            CONN.commit()

    def delete(self):
            sql = """
                DELETE FROM vehicles
                WHERE id =?
            """
            CURSOR.execute(sql, (self.id,))
            CONN.commit()
            del type(self).all[self.id]
            self.id = None

    @classmethod
    def create(cls, vin, make, model, year, location):
        vehicle = cls(vin=vin, make=make, model=model, year=year, location=location)
        vehicle.save()
        return vehicle
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM vehicles
        """
        CURSOR.execute(sql)
        vehicles = CURSOR.fetchall()
        return [cls.instance_from_db(vehicle) for vehicle in vehicles]
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM vehicles
            WHERE id =?
        """
        CURSOR.execute(sql, (id,))
        vehicle = CURSOR.fetchone()
        return cls.instance_from_db(vehicle) if vehicle else None

    
    @classmethod
    def instance_from_db(cls, row):
        vehicle = cls.all.get(row[0])
        if vehicle:
            vehicle.vin = row[1]
            vehicle.make = row[2]
            vehicle.model = row[3]
            vehicle.year = row[4]
            vehicle.location = row[5]
        else:
            vehicle = cls(vin =row[1], make=row[2], model=row[3], year=row[4], location=row[5])
            vehicle.id= row[0]
            cls.all[vehicle.id] = vehicle
        return vehicle
    
    def trips_by_vehicle(self):
        from models.trips import Trip
        sql = """
            SELECT *
            FROM trips
            INNER JOIN vehicles on trips.vehicle_id = vehicles.id
            WHERE trips.vehicle_id =?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [Trip.instance_from_db(row) for row in rows]
    
    def service_record(self):
        from models.mainatence import Mainatence
        sql = """
            SELECT *
            FROM mainatenance_records
            INNER JOIN vehicles on mainatenance_records.vehicle_id = vehicles.id
            WHERE mainatenance_records.vehicle_id =?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [Mainatence.instance_from_db(row) for row in rows]
    