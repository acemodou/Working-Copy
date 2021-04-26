
def phone_book():
        counter = 0
        print("Enter input: ")
        n = int(input())
        name_numbers = [input().split() for _ in range(n)] #To do validate phone number
        phone_contact = {name: contact for name, contact in name_numbers}
        print(phone_contact)

        while True:
            try:

                if counter == n:
                    break
                print("Search phone number")
                counter +=1
                check_contact = input()
                if check_contact in phone_contact:
                    print(check_contact + "=" + phone_contact.get(check_contact))
                else:
                    print("Not found")
            except: break




if __name__=="__main__":
    phone_book()
