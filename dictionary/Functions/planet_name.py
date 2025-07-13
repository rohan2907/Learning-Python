## Find the planet name based on the index
def planet_name(index, /):
    planets = {1:"Mercury", 2:"Venus", 3:"Earth", 4:"Mars", 5:"Jupiter", 6:"Saturn", 7:"Uranus", 8:"Neptune"}
    if 0 <= index < len(planets):
        return planets[index]
    else:
        return "Invalid index"

planet = planet_name(5)
print(f"The planet is {planet}.") 
