class Planet:

    def __init__(self, name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):

            print("name, planet type, and star must be strings")

        if name == "" or planet_type == "" or star == "":

            print("name, planet_type, and star must be non-empty strings")

        self.name = name
        self.planet_type = planet_type
        self.star =  star
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet_1 = Planet(7, "Earth", "main")
print(planet_1.__str__())
print(planet_1.orbit())

planet_2 = Planet("Jupiter", "gala", "mus")
print(planet_2.__str__())
print(planet_2.orbit())

planet_3 = Planet("Mars", "Elon", "Musk")
print(planet_3.__str__())
print(planet_3.orbit())


     