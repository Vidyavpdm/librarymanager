import uuid

class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        
        namespace_uuid = uuid.UUID('00000000000000000000000000000000')  
        
        # Generate UUID3 based on the object's name and namespace UUID
        self.id = str(uuid.uuid5(namespace_uuid, self.name))

    def __str__(self):
        return f"person<{self.name},{self.id}>"

person = Person("vidya", "pdm8767", "6752672167278")
print(person)
