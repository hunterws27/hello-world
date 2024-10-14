firstFileName = input("Enter the name of the first file:")
secondFileName = input("Enter the name of the second file:")
with open(firstFileName, 'r') as firstFile:
    text = firstFile.read()
text
with open(secondFileName, 'w') as secondFile:
    secondFile.write(text)
firstFile.close()
secondFile.close()
print("The text from the first file has been copied to the second file!")
