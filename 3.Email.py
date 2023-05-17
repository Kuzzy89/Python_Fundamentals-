class Person:
    kind = "kur4e"

    def __init__(self, firstname):
        self.firstname = firstname


p1 = Person("Ivan")
p2 = Person("Gosho")

print(Person.kind)
print(p1.kind)
p1.kind = "haiver"
print(p1.kind)
print(Person.kind)
Person.kind = "ahhhhaaa"
print(Person.kind)
print(p1.kind)