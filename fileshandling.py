# Create a file
myFile = open('myFiles.txt', 'w')

# Write to a file
myFile.write("I love python \n")
myFile.write("I love javascript \n")
myFile.close()


# Append to file
myFile = open('myFiles.txt', 'a')
myFile.write("I kinda like php")

# Read a file
myFile = open('myFiles.txt', 'r+')
text = myFile.read()
print(text)
