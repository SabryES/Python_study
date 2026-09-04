'''
fd = open("Files/file.txt")


# print(fd.read()) #read file
# print(fd.read(4)) ##read four charachters

# print(fd.readline()) #read 1 line
# print(fd.readlines()) #return list of lines

## can't read multiple times it will read only first time and second time read empty as cursor at EOF to fix it reset cursor by seek()
firstTime = fd.read()
fd.seek(0)
secondTime = fd.read()
print("First read",firstTime)
print("Secind read",secondTime)

fd.close()
'''
'''
##trying write
fd=open("Files/file2.txt","wt+")
fd.write("Sabry ahmed \n")
fd.write("Embedded systems engineer \n")

fd.close()
'''
color=['red','tang','green']
with open("Files/file3.txt","w+") as fd3:
    fd3.write(" ".join(color))


