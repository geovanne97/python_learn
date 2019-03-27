try:
    f = open("simple.txt","w")#this will work, but if i change the second parameter
                              #to "r" i can not write in the file just read, and then i will go to the except print
    f.write("test")
except IOError:#you dont need to specify the error
    print("could not find this file")
finally:
    print("i always work independing if the try work or not")
#else:this will print if the try work
#    print("sucess")
#    f.close()
