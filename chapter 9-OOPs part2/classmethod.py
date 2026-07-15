class person:
    name = "unknown"

    @classmethod            # change in attributes in class
    def changename(cls,name):
        cls.name = name

p1 =person()
p1.changename("tarun")
print(p1.name)
print(person.name)