class Student():
    def __int__(self, name, id, email, units, address):
        self.name = name
        self.id = id
        self.email = email
        self.units = units
        self.address = address

    def getId(self):
        return self.id

    def setId(self, newId):
        return self.id == newId

    def getUnits(self):
        for unit in self.units:
            print(unit)

    def setUnits(self, newUnits):
        return newUnits
