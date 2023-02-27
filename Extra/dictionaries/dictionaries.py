"""
User entered integer phone number. Please numbers change to words 
"""

digital_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three"
}

phone = input("Please enter the number: ")
output = ""
for character in phone:
    output = output + digital_mapping.get(character) + " "

print(output)


