import urllib.request


"""
Problem 1 --------- Write a program that reads a String from the keyboard. The program should then
construct a URL for http://www.X.com/, replacing X with the String read in, and
print the first five lines of the Web page at that URL in REVERSE ORDER; i.e.,
the fifth, fourth, third, second, and first lines.
"""

def print_url_in_reverse_order():
    print(("Please enter the name of a company (without spaces): "))
    input_line = input()
    url = f'http://www.{input_line}.tax/'

    try:
        # open the url and read the content 
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')

        # split the content into lines 
        lines = content.splitlines()

        # print the first five lines in reverse order 
        for i in range(len(lines)-1, len(lines)-6, -1):
            print(lines[i])
    except urllib.error.HTTPError as e:
        print("An error occurred:", e)
    except urllib.error.URLError as e:
        print("Failed to reach the server:", e)

# print_url_in_reverse_order()


"""
Write a program called "Nuke2.java" containing a class called Nuke2 whose main
method reads a string from the keyboard and prints the same string, with its
second character removed. (That’s character number 1, since Java numbers
characters in a string starting from zero.) In other words, after you run
"java Nuke2", if you type in the string "skin", the program will print "sin".
"""

class Nuke2:
    
    @staticmethod
    def read_string():
        input_line = input("Enter a string: ")
        if len(input_line) >= 2:
            modify_string = input_line[:1] + input_line[2:]
            print(modify_string)
        else:
            print("input string should have atlest two characters")



Nuke2.read_string()
