with open("hello.txt", "w+") as elo:
    elo.write("Hi there!\n")
    elo.seek(0)
    print(elo.read())

    elo.write("Anyone home?\n")
    elo.seek(0)
    print(elo.read())

