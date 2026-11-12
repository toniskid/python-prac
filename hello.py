
class Car:
    def __init__(self,colour: str, horsepower: int) -> None:
        self.colour = colour
        self.horsepower = horsepower


volvo: Car = Car("red" , 200)
print(volvo.colour)
print(volvo.horsepower)


    
