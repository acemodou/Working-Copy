class FirstHundredGenerator:
    def __init__(self) -> None:
        self._number = 0 
    
    def __next__(self):
        if self._number < 100:
            current = self._number
            self._number += 1
            return current
        else:
            raise StopIteration()

class FirstHundredIterable: 
    def __iter__(self):
        return FirstHundredGenerator() 


class AnotherIterable:
    def __init__(self) -> None:
        self._cars = ["Mazda", "Benz"]
    
    def __len__(self):
        return len(self._cars)

    def __getitem__(self, i):
        return self._cars[i]


car = AnotherIterable()
print(car[0])

# print(sum(FirstHundredIterable()))
            
        