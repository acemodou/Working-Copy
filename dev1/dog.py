

class Dog:

    weight_in_pounds = 0

    def __init__(self, size):
        self.size = size

    def makeNoise(self):
        if self.size < 10:
            print("yipyipyip")
        elif self.size < 30:
            print("Bark")
        else:
            print("woof. woof")

    #return the larger of Dog1 and Dog2
    @classmethod
    def  max_dog(cls, d1, d2):
        if d1.size > d2.size:
            return cls(d1)
        else:
            return cls(d2)
    def max_dog_compare(self, otherDog):
        if self.size > otherDog.size:
            print(self.size)
            return self
        print(self)
        return otherDog

