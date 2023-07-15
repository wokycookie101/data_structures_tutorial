# Glass Animal Collection 
sea_creatures = {"Dolphin", "Sea Horse", "Gold Fish", "Shrimp", "Shark", "Cat", "Sea Turtle", "Orca"}
land_creatures = {"Fox", "Whale",  "Elephant", "Monkey", "Dog", "Raccoon", "Rhino", "Spider"}

sea_creatures.remove("Cat")
land_creatures.remove("Whale")

sea_creatures.add("Whale")
land_creatures.add("Cat")

print(sea_creatures)
print(land_creatures)