from .__init__ import CURSOR, CONN

class Driver:
    all = {}

    def __init__(self, id=None, first_name=None, last_name=None, license=None):
        if id is not None:
            self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.license = license
        # self.save()
        

    def __repr__(self):
        return f'<Driver {self.first_name}>'


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("first_name must be of type str")
        self._first_name = value
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("last_name must be of type str")
        self._last_name = value
    
    @property
    def license(self):
        return self._license
    
    @license.setter
    def license(self, value):
        if not isinstance(value, str):
            raise TypeError("license must be of type str")
        self._license = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS drivers (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                license TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS drivers
        """
        CURSOR.execute(sql)
        CONN.commit()
    

    def save(self):
        sql = """
            INSERT INTO drivers (first_name, last_name, license)
            VALUES (?,?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.license))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE drivers
            SET first_name =?, last_name =?, license =?
            WHERE id =?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.license, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM drivers
            WHERE id =?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, first_name, last_name, license):
        driver = cls(first_name= first_name, last_name = last_name, license = license)
        driver.save()
        return driver

    @classmethod
    def instance_from_db(cls, row):
        driver = cls.all.get(row[0])
        if driver:
            driver.first_name = row[1]
            driver.last_name = row[2]
            driver.license = row[3]
            
        else:
            driver = cls(first_name=row[1], last_name=row[2],license=row[3])
            driver.id= row[0]
            cls.all[driver.id] = driver
            
        return driver
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM drivers
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM drivers
            WHERE id =?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None