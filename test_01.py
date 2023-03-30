"""
Create a Plane, Boeing, Airbus classes.
Base class should contain methods to get:  plane name, plane type (A320, B737 etc), 
max_speed (should be the funciotn: base_speed * model_speed_coeficient).
Both plane subclasses should only take model type as input argument.
"""


class Plane:
    BASE_SPEED = 750
    def __init__(self, model_type: str, model_speed_coeficient, name_suffix) -> None:
       self.model_type = model_type
       self.model_speed_coeficient = model_speed_coeficient
       self.name_suffix = name_suffix
      
    def get_plane_name(self):
        return print(self.name_suffix + self.model_type)

    def get_plane_type(self):
        return self.plane_type

    def get_max_preed(self):
        return print(self.BASE_SPEED * self.model_speed_coeficient)


class Boing(Plane):
    NAME_SUFFIX = "B"
    BOEING_TYPE_SPEED_COEF = {
        "737" : 1,
        "747" : 1.2,
        "757" : 1.35,
        "767" : 1.5,
        "777" : 1.8,
        }
    def __init__(self, model_type: str) -> None:
        self.model_type = model_type
        self.coficient = self.get_speed_coeficient()
        super().__init__(model_type = model_type, model_speed_coeficient = self.coficient, name_suffix = self.NAME_SUFFIX)

    def get_speed_coeficient(self):
        return self.BOEING_TYPE_SPEED_COEF.get(self.model_type)
        

my_plane = Boing('747')
my_plane.get_plane_name()
my_plane.get_max_preed()