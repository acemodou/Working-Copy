
class Dog {
private:
    int weight_in_pounds;

public:
    Dog(int size)
    {
        weight_in_pounds = size;
    }

    void make_noise()
    {
        if (weight_in_pounds < 10)
        {
            std::cout << "yipyip" << std::endl;
        }
        else if (weight_in_pounds < 30)
        {
            std::cout << "woof" << std::endl;
        }
        else
        {
            std::cout << "Awwww" << std::endl;
        }
    }


static Dog max_dog(const Dog& d1, const Dog& d2)
{
    if (d1.weight_in_pounds > d2.weight_in_pounds)
    {
        return d1;
    } 
    return d2;
}

};


int main() {

Dog d1(8);
d1.make_noise();
Dog d2(65);
Dog::max_dog(d1, d2);

}


