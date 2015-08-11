class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        

hippo = Animal("Harry", 10) 
sloth = Animal("Jefferey", 4)
ocelot = Animal("Jack", 7)
hippo.description()
print "Health of Harry is", hippo.health
sloth.description()
print "Health of Jeffery is", sloth.health
ocelot.description()


print "Jack's Health is", ocelot.health