# https://github.com/robotautas/kursas/wiki/JSON

"""
{
  "colors": [
    {
      "color": "black",
      "rgb": "255, 255, 255",
      "hex": "#000"
    },
    {
      "color": "white",
      "rgb": "0, 0, 0",
      "hex": "#FFF"
    }

"""
import json
import requests

get_data = requests.get('https://api.meteo.lt/v1/stations/vilniaus-ams')
# print(get_data.text)
# print(type(get_data.text))
# print(get_data.content)
# print(get_data.headers)

to_python_dict = json.loads(get_data.text)
to_python_dict["code"] = 'pakeistas pavadinimas'
to_json = json.dumps(to_python_dict)

with open('/home/zbook_ubuntu/Documents/CodeAcademy/level_02/Lesson_06 Requests/json task_01/example2.json', 'w') as file:
    json.dump(to_json, file)


with open('/home/zbook_ubuntu/Documents/CodeAcademy/level_02/Lesson_06 Requests/json task_01/example2.json', 'r') as file:
    data = json.load(file)

print(type(data))    
print(data)





# with open('/home/zbook_ubuntu/Documents/CodeAcademy/level_02/Lesson_06 Requests/json task_01/json_data.json', 'r') as file:
#     data = json.load(file)

# with open('https://api.meteo.lt/v1/stations/vilniaus-ams', 'r') as file:
#     data = json.load(file)
#     # to_python_dict = json.loads(data)
# print(type(data))

