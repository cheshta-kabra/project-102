file=input('Enter the file name')
f = open(file)
fileLines = f.readlines()
for line in fileLines:
    print(line)

Wordfound = 'NO'
introString = input("Enter Your String: ")
searchString = input("Enter The Word You Want to Search: ")
words = introString.split()
for word in words:
    if word == searchString:
        Wordfound = 'Yes'

if Wordfound == 'Yes':
    print("Word Found!")
else:
    print("Not Found!")