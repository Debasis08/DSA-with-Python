# file = open('read.txt', 'r')

# #content = file.read()

# #print(content)

# # Above both lines can be written as:
# print(file.read()) # to read the whole file
# file.close()


# file = open('read.txt', 'r')
# print(file.read(5)) # to read the first 5 chars of file
# file.close()


# file = open('read.txt', 'r')
# print(file.readline()) # to read the one line of file
# file.close()


file = open('read.txt', 'r')
print(file.readline()) # to read the one line of file
print(file.read(5)) # to read the first 5 chars of file
file.close()