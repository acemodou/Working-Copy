from dog import Dog

if __name__ == "__main__":
    dog1 =Dog(9)
    dog2 = Dog(56)
    #dog1.makeNoise()
    new_dog = [i for i in range(3)]
    new_dog[0] = Dog(29)
    new_dog[1] = Dog(1000)
    new_dog[2] = Dog(-3)

    larger_d = Dog.max_dog_compare(new_dog[1], dog1)


    # for i in range(len(new_dog)):
    #     Dog.max_dog(new_dog[i], dog1).makeNoise() #This call will fail because is a static method. we can replace cls with self to call it here






