#We are using opne(), built in the functionality from python to open files

try:  #tries to run the block of code
    file = open('order.txt', 'r')
    file_line_list = file.readlines()
    print(file)
    print(file_line_list)
    print(type(file_line_list))
    for line in file_line_list:
        print(line.rstrip('\n'))  #reduces the space between objects in a list

    file.close() #if you don't clsoe it, you can cause a lock in the file -  similar top trying to delete a file that is open
except FileNotFoundError as errmsg:  # if it fails, it runs this block of code
    print('Hi, file could not be opened, please see below')
    print(errmsg)
    raise # sends the default error and crucially, it stops the code - it will not print the hey below
    print('hey')