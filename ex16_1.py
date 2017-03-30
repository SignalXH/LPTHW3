from sys import argv

script, filename = argv
target = open(filename)

print("display what is in it !")
print(target.read())

target.close()
