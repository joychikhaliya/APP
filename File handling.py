
filename = "1st.txt"

# First creating the file via w mode, basically it is being overwritten .
file = open(filename, "w")
file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.close()
print(" File written - overwritten). \n")

# Read the file and print its contents
file = open(filename, "r")
content = file.read()
file.close()
print("Current file contents: \n")
print(content)

# Appending the file, which will add the new line to the end of the file, not overwritting it.
file = open(filename, "a")
file.write("This line was appended.\n")
file.close()
print(" New line appended. ")

# verifying if it worked.
file = open(filename, "r")
content = file.read()
file.close()
print( " File contents after appending: \n")
print(content)


#  File written - overwritten
#
# Current file contents: 
#
# This is the first line.
# This is the second line.
#
#  New line appended. 
#  File contents after appending: 
#
# This is the first line.
# This is the second line.
# This line was appended.
