all_students = {
    "university" : {
        "university name" : "VDU", 
        "university city" :"Vilnius",
        "groupe direction" : {
            "direction name" : "himanitarian", 
            "direction name" : "mathematics", 
            "groupe" : {
                "groupe name" : "HTM",
                "subgroupe" : {
                    "subgroupe name" : "HTM1",
                    "student" : {
                        "name" : "Tom",
                        "surname" : "Trump",
                        "age" : "30"
                    }
                }
            }
        }
        
    }
        
}

print(all_students)

print(list(all_students.items()))
print(list(all_students.values()))
