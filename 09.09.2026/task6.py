class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            parts = line.split()
            record = dict(zip(self.FIELDS, parts))
            self.lst_data.append(record)

    def select(self, a, b):
        return self.lst_data[a:b+1].copy()

db = DataBase()
db.insert(["1 Сергей 35 120000", "2 Ольга 28 95000"])
print(db.select(0, 1))