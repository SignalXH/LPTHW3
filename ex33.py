def lprint(n):
    i = 0
    number = []

    while i < n:
        print(f"at the top i is {i}")
        number.append(i)

        i = i + 1
        print("Numbers now are: ", number)
        print(f"at the bottom i is {i}")

    print("numbers:")

    for num in number:
        print(num)

lprint(99)
