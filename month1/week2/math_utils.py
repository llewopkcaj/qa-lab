def add(a, b):
    return a + b


def mean(*numbers):
    return sum(numbers) / len(numbers)


def describe_person(name, **attributes):
    describer = f"{name} has the following attributes:\n"
    for key, value in attributes.items():
        describer += f"- {key}: {value}\n"
    return describer


print(describe_person("Alice", age=30, city="New York", profession="Engineer"))
