print("""you enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("there's a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1. take the cake.")
    print("2.scrame at the bear.")

    bear = input("> ")

    if bear == "1":
        print("the  bear eats your face off.")
    elif bear == "2":
        print("the bear eats your legs off.")
    else:
        print(f"well, doing {bear} is probablay better.")


elif door ==  "2":
    print("you stare into the endless abyes at cthulhu's retina.")
    print("1. blueberries.")
    print("2. yellow jacket clothespins.")
    print("3. understanding revolers yelling melodies.")

    insanity = input("> ")
    if insanity == "1" or insanity =="2":
        print("you body survives power babababa.")
    else:
        print("babababa.")

else:
    print("blablabla.")
