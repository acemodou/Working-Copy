
# def phone_book():
#         counter = 0
#         print("Enter input: ")
#         n = int(input())
#         name_numbers = [input().split() for _ in range(n)] #To do validate phone number
#         phone_contact = {name: contact for name, contact in name_numbers}
#         print(phone_contact)

#         while True:
#             try:

#                 if counter == n:
#                     break
#                 print("Search phone number")
#                 counter +=1
#                 check_contact = input()
#                 if check_contact in phone_contact:
#                     print(check_contact + "=" + phone_contact.get(check_contact))
#                 else:
#                     print("Not found")
#             except: break

def phone_book():
    ''' Enter name and number to store in dictionary '''
    x = int(input("How many names and number to store in contacts: "))
    name_number = [input('Enter name and number: ').split() for _ in range(x)]
    phoneBook = {name:number for name, number in name_number}

    ''' Lookup Number by Name '''
    for _ in range(x):
        search_contact = input('What contact are you looking for ?:')
        print(search_contact +'='+phoneBook.get(search_contact, 'Not Found'))
    
        


if __name__=="__main__":
    phone_book()
