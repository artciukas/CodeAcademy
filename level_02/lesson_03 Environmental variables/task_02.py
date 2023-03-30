"""

write a function that accepts an encoded string as a parameter. 
This string will contain a first name, last name, and an id.Values in the string can be separated by any number of zeros. 
The id is a numeric value but will contain no zeros. 
The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
An example input would be “Robert000Smith000123”. 
The function should return the following using that input:{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }


"""

new_list = []
dictionary_output = {}


def decoder(name: str) -> dict["first_name":str, "last_name": str, "id": int]:
    names = name.split("0")
    for list_item in names:
        if list_item != "":
            new_list.append(list_item)

    dictionary_output["first_name"] = new_list[0]
    dictionary_output["last_name"] = new_list[1]
    dictionary_output["id"] = int(new_list[2])

    return dictionary_output


print(decoder(name='Robert000000Smith000000123'))