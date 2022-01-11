#Exercise 15 - Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

#note all inputs must be positive

def exponent(base, exp):
    val = base
    for i in range (1, exp):
        base *= val

    return base

#print(exponent(2, 7))
        

#python I/O and File Handling practice

#Exercise 1 - write a program to accept two numbers from a user

def multi():

    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    
    print(x*y)

#multi()

#Exercise 2 - Display three inputted strings as

def formatter():
    x = (input("Enter String: "))
    y = (input("Enter String: "))
    z = (input("Enter String: "))    
    print(x, y, z, sep = '**')

#formatter()

#Exercise 3 - Convert Decimal number to octal using print() formatting

def octal():

    num = int(input("Enter a number: "))

    print('%o' % num )

#octal()

#Exercise 4 - Display float numbers with 2 decimal places using print()
def floatDisplay():
    num = float(input("Enter a number: "))

    print('%.2f' % num)

#floatDisplay()
    

#Exercise 5 - Accept a list of float numbers as input from the user

def floatList():
    alen = int(input("Enter a number: "))
    v = []
    for i in range(0, alen):
        num = float(input("Enter a number: ")) 
        v.append(num)

    return v

print("User Items: " + str(floatList()))

#file handling notes

# Text File: Text file usually we use to store character data. For example, test.txt
# Binary File: The binary files are used to store binary data such as images, video files, audio files, etc.

#creating and writing files

# with open ('filename.ext', 'w') as fp:
    # fp.write('newline')

#reading files

# with open ('filename.ext', 'r') as fp:
    # fp.read()

#list files from directory

# os.rename('old_file_name', 'new_file_name')
# os.remove('file_path')

#Copy, Rename, Delete Files from Directory

# shutil.copy('src_file_path', 'new_path')
# shutil.move('src_file_path', 'new_path')

#Copy, Delete Directories

# os.listdir('dir_path') #get all files
# shutil.rmtree('path') #remove directory
# shutil.copytree('src_path', 'dst_path') #copy dir



#File Access modes

#r	It opens an existing file to read-only mode. The file pointer exists at the beginning.

#rb	It opens the file to read-only in binary format. The file pointer exists at the beginning.

#r+	It opens the file to read and write both. The file pointer exists at the beginning.

#rb+	It opens the file to read and write both in binary format. The file pointer exists at the beginning of the file.

#w	It opens the file to write only. It overwrites the file if previously exists or creates a new one if no file exists with the same name.

#wb	It opens the file to write only in binary format. It overwrites the file if it exists previously or creates a new one if no file exists.

#w+	It opens the file to write and read data. It will override existing data.

#wb+	It opens the file to write and read both in binary format

#a	It opens the file in the append mode. It will not override existing data. It creates a new file if no file exists with the same name.

#ab	It opens the file in the append mode in binary format.

#a+	It opens a file to append and read both.

#ab+	It opens a file to append and read both in binary format.


#seek() method changes file pointer to specific location to write something there
#The tell() method to return the current position of the file pointer from the beginning of the file.

#read methods

#read()	Returns the file content.
#readline()	Read single line
#readlines()	Read file into a list
#truncate(size)	Resizes the file to a specified size.
#write()	Writes the specified string to the file.
#writelines()	Writes a list of strings to the file.
#close()	Closes the opened file.
#seek()	Set file pointer position in a file
#tell()	Returns the current file location.
#fileno()	Returns a number that represents the stream, from the operating system's perspective.
#flush()	Flushes the internal buffer.

#os.rename() renames file
#os.delete() deletes file



#Exercise 6 - Write all content to a given file into a new file but skip line 5

    






