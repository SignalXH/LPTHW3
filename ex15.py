from sys import argv
#import variable argumet from sys module, and define two variable name in argv
script, filename = argv
#call open function to open the file
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

#call function read() on txt
print("Type theb filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
