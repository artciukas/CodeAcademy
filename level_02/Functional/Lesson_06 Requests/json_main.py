import json

# JSON (JavaScript Object Notation) - yra atviro standarto duomenų perdavimo ir saugojimo formatas.
"""
Python	JSON
dict	   Object
list	   Array
tuple	   Array
str	   String
int	   Number
float	   Number
True	   true
False	   false
None	   null
"""
##############################
# """
# .loads() JSON -> PYTHON

data = '''{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson",
        "boolean": "null"
     } 
  ]   
}'''

data_dict = json.loads(data)
print(data_dict)
print(type(data_dict))
# """

# .dumps() PYTHON -> JSON
new_json = json.dumps(data_dict, indent=2)
print(new_json)
# indent=2 reiškia, kad norėsime rezultato gražiai atspausdinto, su dviejų tarpų indentacija.
# {
#   "student": [
#     {
#       "id": "01",
#       "name": "Tom",
#       "lastname": "Price",
#       "gender": "male"
#     },
#     {
#       "id": "02",
#       "name": "Kyle",
#       "lastname": "Thameson",
#       "gender": "male"
#     }
#   ]
# }

# .load() užkrauti JSON objektą iš failo, darome taip:
with open('example.json', 'r') as file:
    data = json.load(file)

print(data)

# .dump() leidžia įrašyti python žodyną į failą:
with open('example2.json', 'w') as file:
    json.dump(data, file, indent=2, sort_keys=True)
# sort_keys išrūšiuoja atributus (keys) pagal abėcelę