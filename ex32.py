the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is {number}.")

#same as above
for fruit in fruits:
    print(f"a fruit of type : {fruit}.")

#also we can go through mixed list too.
#notice we have to use {} since we don't know what's in it.
for i in change:
    print(f"i got {i}.")

#we also can build list, firt start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"adding {i} to the lists")
    #append is function that lists understand
    elements.append(i)

for i in elements:
    print(f"elements have {i}")
