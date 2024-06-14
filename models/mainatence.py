from .__init__ import CURSOR, CONN

class Mainatence:
    all = {}

    def __init__(self, id=None, vehicle_id=None, mainatence_type = None, mainatence_date = None,):
        if id is not None:
            self.id = id
        self.vehicle_id = vehicle_id
        self.mainatence_type = mainatence_type
        self.mainatence_date = mainatence_date
        # self.save()
    
        

    def __repr__(self):
        return f'<Mainatence_Record {self.mainatence_type}>'


    @property
    def mainatance_type(self):
        return self._mainatance_type
    
    @mainatance_type.setter
    def mainatance_type(self, value):
        if not isinstance(value, str):
            raise TypeError("mainatance_type must be of type str")
        self._mainatance_type = value
    
    @property
    def mainatance_date(self):
        return self._mainatance_date
    
    @mainatance_date.setter
    def mainatance_date(self, value):
        if not isinstance(value, str):
            raise TypeError("mainatance_date must be of type str")
        self._mainatance_date = value


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS mainatenance_records (
                id INTEGER PRIMARY KEY,
                vehicle_id INTEGER,
                mainatence_type TEXT,
                mainatence_date TEXT,
                FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)
               ) """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS mainatenance_records
        """
        CURSOR.execute(sql)
        CONN.commit()
    

    def save(self):
        sql = """
            INSERT INTO mainatenance_records (vehicle_id, mainatence_type, mainatence_date)
            VALUES (?,?, ?)
        """
        CURSOR.execute(sql, (self.vehicle_id, self.mainatence_type, self.mainatence_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE mainatenance_records
            SET vehicle_id =?, mainatence_type =?, mainatence_date =?
            WHERE id =?
        """
        CURSOR.execute(sql, (self.vehicle_id, self.mainatence_type, self.mainatence_date, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM mainatenance_records
            WHERE id =?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, vehicle_id, mainatence_type, mainatence_date):
        record = cls(vehicle_id= vehicle_id, mainatence_type = mainatence_type, mainatence_date= mainatence_date)
        record.save()
        return record

    @classmethod
    def instance_from_db(cls, row):
        record = cls.all.get(row[0])
        if record:
            record.vehicle_id = row[1]
            record.mainatence_type = row[2]
            record.mainatence_type = row[3]
            
        else:
            record = cls(vehicle_id=row[1], mainatence_type=row[2],mainatence_date=row[3])
            record.id= row[0]
            cls.all[record.id] = record
            
        return record
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM mainatenance_records
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM mainatenance_records
            WHERE id =?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None