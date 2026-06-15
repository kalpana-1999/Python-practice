class Parent:
    def __init__(self,name,hair_color,height):
        self.name=name
        self.hair_color=hair_color
        self.height=height
    def parent_property(self):
        print(f"Parent's name is {self.name},and hair color is{self.hair_color},and his height is {self.height}")

class Child1(Parent):
    def __init__(self,nam)