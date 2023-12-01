class Dog:
    weight_in_pounds = 0 
    bionem = "Canis Familiaris"

    def __init__(self, size):
        self.weight_in_pounds = size 
    
    def make_noise(self):
        if self.weight_in_pounds < 10:
            print("yipyip")
        elif self.weight_in_pounds < 30:
            print("bark")
        else:
            print("woof")
    
    @staticmethod
    def max_dog(self,d1, d2):
        if d1.weight_in_pounds > d2.weight_in_pounds:
            return d1
        return d2 
    
    def max_dog(self, other):
        if self.weight_in_pounds > other.weight_in_pounds:
            return self 
        return other







