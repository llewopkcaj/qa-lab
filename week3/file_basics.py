def write_and_read(path):
    with open(path, "w+") as elo:
        elo.write("Hi there!\n")
        elo.seek(0)
        first = elo.read()

        elo.write("Anyone home?\n")
        elo.seek(0)
        second = elo.read()

    return first, second

