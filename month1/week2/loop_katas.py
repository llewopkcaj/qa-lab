def sum_1_to_100():
    total = 0
    for x in range(1, 101):
        total += x
    return total


def every_third_0_to_30():
    return list(range(0, 31, 3))


def enumerate_with_index(items):
    out = []
    for index, value in enumerate(items, start=1):
        out.append(f"{index}: {value}")
    return out


def countdown_from_10():
    el = 10
    out = []
    while el >= 0:
        out.append(el)
        el -= 1
    return out


def find_first_multiple_of_7(limit: int):
    for i in range(1, limit + 1):
        if i % 7 == 0:
            return i
    else:
        return None


if __name__ == "__main__":
    print(sum_1_to_100())
    print(every_third_0_to_30())
    print(enumerate_with_index(["a", "b"]))
    print(countdown_from_10())
    print(find_first_multiple_of_7(20))
    print(find_first_multiple_of_7(5))
