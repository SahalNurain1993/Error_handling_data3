#We are using opne(), built in the functionality from python to open files

def open_and_print(file_to_open):

    try:  # tries to run the block of code
        file = open(file_to_open, 'r')
        file_line_list = file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))
        file.close()



    except FileNotFoundError as errmsg:
        print('Hi, file could not be opened, please see below')
        print(errmsg)
    #raise
    print('hey')

open_and_print('order.txt')



