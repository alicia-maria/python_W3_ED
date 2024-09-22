print ("Hello, World")

# File handing Functions 
## open() function can take on 2 parameters 
##  1. filename 
##  2. Mode 

# "r" - read
# "a" - append - creates the file if it doesnt exsist 
# "w" - write - creates the file if it doesnt not exsist 
# "x" - create - creates the specific file 
# "t" - text - default value
# "b" - binary mode 

# How to open a file for reading it
f = open("demofile.txt", "rt")
# The code above works because you specified the file , then used "r" to read and defined its with "t" which means text 

# Q What is the function used for opening files?
# A. open()

# Q By default the file is opened in text mode, but you can also open the file in binary mode. which one of the following syntaxes opens the file in binary mode?
#x = open('demofile.txt', "b")

# Q.The defualt opening mode when opening a file with the open() function is "r" for 'reading'
# A. TRUE


#to open files using a file object you must use the following syntax 
f = open("demofile.txt", "r")
print(f.read())

# If the file is located in a different location , you can specifiy path file using the following 
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

# Say you only want to read part of the document or file you can use the following code to define how many characters you want it to read 
f = open("demofile.txt", "r")
print(f.read(5))

# Read lines by using a readline() method 
f = open("demofile.txt", "r")
print(f.readline())

# Closing file by using the following 
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#Q After opening a file with the open() function, which method can be used to read the context ?
#A read()

# To read only one line, we can use another method by using the following 
readline()

# Q. if you call the readline() method two times, it will return the two first lines 
# A. TRUE

## writing to an exsiting file 


f = open("demofile.txt" , "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending 
f = open("demofile.txt" , "r")
print(f.read())

#QWhat happens to the original file content if you open a file like this:
f = open('demofile3.txt', 'w')
#A . The original content will be overwritten 

#how to create a file 
f =open("demofile3.txt" , "w")
f.write("Yay we have created a new file with content")


# How to delete files 
import os
os.remove("demofile3.txt")

#how to make sure the file exsists 
import os
if os.path.exists("demofile3.text") :
    os.remove("demofile3.txt")
else : 
    print("The file does not exsist")
