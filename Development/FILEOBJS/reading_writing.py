def main():

    # Open a file for writing and create it if it doesn't exist
    # f = open('textfile.txt', 'w+')

    # Open a file for appending text to the end
    # f = open('textfile.txt', 'a')

    # Write some lines of data to the file
    # for i in range(5):
    #     f.write("This is line " + str(i) + "\r\n")
    
    # f.seek(2)
    # f.write('Hey')
    # Open a file for reading
    # f = open('textfile.txt', 'r')

    # #Check the file mode and if it's what i want then read the entire content
    # if f.mode == 'r':
    #     contents = f.read()
    #     print(contents)
    
    #Check the file mode and if it's what i want then read line by line
    # if f.mode == 'r':
    #     contents = f.readlines()
    #     for x in contents:
    #         print(x)

    # We use for loop to get one line at a time without having to buffer the entire file in memory
    # rstrip will strip any newline or white space at the end of the line
    # f = open('textfile.txt')
    # for line in f:
    #     print(line.rstrip())

    # close the file when done
    # f.close()

    ''' Rt and wt is optional but is better to be explicit in python
    we added the '.' here to avoid printing a new line after the . that's
    why end = ''
    Flush = True to flush the output buffer. 
    you can use outfile.writeline instead of print.
    However the difference is with print() we are able to rewrite the line
    endings with the rstrip() which it does by default.
    If you don't want that you can use the writeline method instead.

    '''
    # infile = open('lines.txt', 'rt')
    # outfile = open('lines-copy.txt', 'wt')
    # for line in infile:
    #     print(line.rstrip(), file=outfile)
    #     print('.', end='', flush=True)
    # outfile.close()
    # print('\ndone')

    # Similar as above except we are printing images here 
    infile = open('pic.jpg', 'rb')
    outfile = open('pic-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # This is my buffer size
        if buf:
            outfile.write(buf)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone')



if __name__ == "__main__":
    main()

    