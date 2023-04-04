import json

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
        "boolean": "None"
     } 
  ]   
}'''

data_dict = json.loads(data)
print(data_dict)
print(type(data_dict))