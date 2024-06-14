from .__init__ import CONN, CURSOR

class Trip:
    all = {}
    def __init__(self, id= None, vehicle_id = None, driver_id = None, start_time = None, end_time = None, distance= None):
        self.id = id
        self.vehicle_id = vehicle_id
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time
        self.distance = distance
        # self.save()

    def __repr__(self):
        return f"<Trip Trip_id:{self.id}, Vehicle _Id: {self.vehicle_id}, Driver_id: {self.driver_id},>"
    
    @property
    def vehicle_id(self):
        return self._vehicle_id
    
    @vehicle_id.setter
    def vehicle_id(self, value):
        if isinstance(value, int):
            self._vehicle_id = value
        else:
            raise TypeError("vehicle_id must be of type int")
    
    @property
    def driver_id(self):
        return self._driver_id
    
    @driver_id.setter
    def driver_id(self, value):
        if isinstance(value, int):
            self._driver_id = value
        else:
            raise TypeError("driver_id must be of type int")
    
    # @property
    # def start_time(self):
    #     return self._start_time
    
    # @start_time.setter
    # def start_time(self, value):
    #     if isinstance(value, int):
    #         self._start_time = value
    #     else:
    #         raise TypeError("start_time must be of type int")
        
    # @property
    # def end_time(self):
    #     return self._end_time
    
    # @end_time.setter
    # def end_time(self, value):
    #     if isinstance(value, int):
    #         self._end_time = value
    #     else:
    #         raise TypeError("end_time must be of type int")
    
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, value):
        if isinstance(value, int):
            self._distance = value
        else:
            raise TypeError("distance must be of type int")
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS trips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vehicle_id INTEGER NOT NULL,
                driver_id INTEGER NOT NULL,
                start_time INTEGER NOT NULL,
                end_time INTEGER NOT NULL,
                distance INTEGER NOT NULL,
                FOREIGN KEY (vehicle_id) REFERENCES vehicles(id),
                FOREIGN KEY (driver_id) REFERENCES drivers(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS trips
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO trips (vehicle_id, driver_id, start_time, end_time, distance)
            VALUES (?,?,?,?,?)
        """
        CURSOR.execute(sql, (self.vehicle_id, self.driver_id, self.start_time, self.end_time, self.distance))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        if hasattr(self, '_id'):
            sql = """
                UPDATE trips
                SET vehicle_id =?, driver_id =?, start_time =?, end_time =?, distance =?
                WHERE id =?
            """
            CURSOR.execute(sql, (self.vehicle_id, self.driver_id, self.start_time, self.end_time, self.distance, self.id))
            CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM trips
            WHERE id =?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls, vehicle_id, driver_id, start_time, end_time,distance):
        trip = cls(vehicle_id= vehicle_id, driver_id = driver_id, start_time= start_time, end_time= end_time, distance= distance)
        trip.save()
        return trip
    
    @classmethod
    def instance_from_db(cls, row):
        trip = cls.all.get(row[0])
        if trip:
            trip.vehicle_id = row[1]
            trip.driver_id = row[2]
            trip.start_time = row[3]
            trip.end_time = row[4]
            trip.distance = row[5]
        else:
            trip = cls(vehicle_id =row[1], driver_id=row[2], start_time=row[3], end_time=row[4], distance=row[5])
            trip.id= row[0]
            cls.all[trip.id] = trip
        return trip
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM trips
        """
        CURSOR.execute(sql)
        trips = CURSOR.fetchall()
        return [cls.instance_from_db(trip) for trip in trips]
    
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM trips
            WHERE id =?
        """
        CURSOR.execute(sql, (id,))
        trip = CURSOR.fetchone()
        return cls.instance_from_db(trip) if trip else None
    
    

    
    