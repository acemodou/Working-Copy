def printPicnic(picnicItems, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for k, v in picnicItems.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


if __name__ == "__main__":
    picnicItems ={'Sandwiches' : 7, 'apples' : 12, 'oranges' : 12, 'cookies' : 800}
    printPicnic(picnicItems, 12, 5)

