import pyperclip


#TODO: Store the text 
# TODO: Paste the text from the clipboard
#TODO:  Add bullet's to the text after splitting it with new line 
#TODO: Copy the text 

text = 'Lists of nimals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

# text = pyperclip.paste()

#Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)





